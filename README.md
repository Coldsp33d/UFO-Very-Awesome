# UFO-Very-Awesome
CSCI 599 - Assignment 2 - featuring data from the British Council of UFO 
## Named Entity Recognition
The tika-ner folder contains the required jars (tika-app and tika-core-nlp) in the target folder. They have been built from the source and would be required for performing named entity recognition on the UFO Data Set. The open nlp models have also been added on to the repository under - org\apache\tika\parser\ner\opennlp.
Two batch files have been addded to run NER on http://people.apache.org/committer-index.html (OpenNLP + TIKA) and http://www.hawking.org.uk (CoreNLP + Tika) and the outputs are being written in two files - ner_core_nlp_output.txt and ner_open_nlp_output.txt. The batch files can be executed directly to see the results and it doesn't require and other dependency to be downloaded separately. This has been done just for the purposes of demonstration and any of the artifacts and binaries would not be a part of the final deliverable. (Reference - https://wiki.apache.org/tika/TikaAndNER)