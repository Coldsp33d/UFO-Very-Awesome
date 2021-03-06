# import statements
import os
import time
import http
import selenium

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# filepath definitions
mediaFile = 'Data/scraped_data.txt'
imageFile = 'Data/scraped_img_urls.txt'

def getElements(pageNo):
    # method to scrape data from a given page on ufostalker
    eventData = {}
    table_elements = driver.find_elements_by_css_selector('table')
    if table_elements is None or len(table_elements) <= 1:
        return

    tbody = table_elements[0].find_elements_by_css_selector('tbody')
    table1_data = (tbody[0].text)
    output = table1_data.split('\n')

    eventData[pageNo] = {}
    eventData[pageNo]['SightedOn'] = output[1].strip('Date of the Sighting ')
    eventData[pageNo]['ReportedOn'] = output[2].strip('Date Submitted ')

    tbody = table_elements[1].find_elements_by_css_selector('tbody')
    table2_data = (tbody[0].text)

    output = table2_data.split('\n')
    eventData[pageNo]['demographics'] = output

    tbody = table_elements[4].find_elements_by_css_selector('tbody')
    table4_data = (tbody[0].text)
    output = table4_data.split('\n')

    eventData[pageNo]['sighting_specifics'] = output
    tbody = table_elements[7].find_elements_by_css_selector('tbody')
    table7_data = (tbody[0].text)

    eventData[pageNo]['description'] = output[0]
    link = 'https://www.mufoncms.com/'
    elements = driver.find_elements_by_css_selector('td.ng-scope')

    eventData[pageNo]["url"] = []
    for anchorTag in elements:
        href = anchorTag.find_elements_by_css_selector('a')
        eventData[pageNo]["url"].append(str(href[0].get_attribute("href")))
        write_to_file(imageFile, href[0].get_attribute("href"))

    write_to_file(mediaFile, json.dumps(eventData))

    print(eventData)

def write_to_file(filepath, data):
    with open(filepath, 'a+') as f:
        f.write(data + '\n')

chrome_options = Options()
chrome_options.add_extension('Data/Resources/1.2.6_0.crx') #anonymox
chrome_options.add_extension('Data/Resources/3.27.0_0.crx') #adblock
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)
driver.wait = WebDriverWait(driver, 30)

cur, end = 72000, 82000  # need to change this
retries = 0
while cur <= end:
    print("Current Page" + str(cur))
    try:
        url = 'http://www.ufostalker.com/event/'
        eventOccurence = url + str(cur)
        driver.get(eventOccurence)
        time.sleep(1)
        getElements(cur)
        cur += 1
        retries = 0
    except (
        http.client.RemoteDisconnected, 
        IndexError, 
        ConnectionResetError, 
        selenium.common.exceptions.NoSuchWindowException,
        selenium.common.exceptions.WebDriverException
    ):
        print('Error!')
        retries += 1
        if retries >= 3:
            cur, retries = cur + 1, 0
            
driver.close()
