# Text-Processing

functions helps exlporing and preparing Chinese LDA dataset

class Corpus: 
    function parse(): able to parse the input files char-wise or word-wise (the word is based on thulac) 
    function clean_corpus(): reserve/eliminate the input dict document from the input corpus document
    
class Dict: 
     function save_dict(): create and save dict from input corpus files
     function plot_dict(): plot the dict tf or df or both distribution & save the top words in each bin
     function prep_stopwords(): generated stopwords file from the resulf of save_dict()

preprocess utils: 
     helper function readFile(): efficiently read each line from given input file directory. Return in str format or list format
     

Note:
* all the functions in Corpus and Dict receive a list of inp/outp file directories as function parameter
* current design: prepare file directories in xxTester, then pass the directories to corresponding function
    
