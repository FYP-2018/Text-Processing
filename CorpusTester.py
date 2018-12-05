import os
import glob

import thulac

from Corpus import Corpus
from PreprocessUtils import readFile

def Corpus_parse_tester():
    # preparing inps and outps
    user_dict = '/Users/user/Desktop/dataset/HKNEWS_full/hk_words/dict.txt.big.txt'
    
    corp_inp_dirs = []
    dict_inp_dirs = []
    outp_dirs = []
    root_dir = '/Users/user/Desktop/dataset/HKNEWS_full/Categories/'
    dict_dir = os.path.join(root_dir, 'dict_no_sw')
    new_dir = os.path.join(root_dir, 'cleaned')
    
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    for f in glob.glob(os.path.join(root_dir, '*.txt')):
        cate_name = f.split('/')[-2]
        inp_name = f.split('/')[-1]
        
    
        if '_title.txt' not in inp_name:
            corp_inp_dirs.append(f)
            dict_inp_dirs.append(os.path.join(dict, inp_name[-4] + '_dict.txt'))
            outp_dirs.append(os.path.join(new_dir, inp_name))


    # parsing files
    corp = Corpus()
    corp.clean_corpus(corp_inps=inp_dirs,
                      dict_inps=dict_inp_dirs,
                      outps=outp_dirs,
                      dict_type='keep')


def Corpus_clean_tester():
    corp_inp_dirs = []
    dict_inp_dirs = []
    outp_dirs = []
    root_dir = '/Users/user/Desktop/dataset/HKNEWS_full/Categories/thulac'
    dict_dir = os.path.join(root_dir, 'dict_no_sw')
    new_dir = os.path.join(root_dir, 'cleaned')
    
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    for f in glob.glob(os.path.join(root_dir, '*.txt')):
        cate_name = f.split('/')[-2]
        inp_name = f.split('/')[-1]
        
        
        if '_title.txt' not in inp_name:
            corp_inp_dirs.append(f)
            dict_inp_dirs.append(os.path.join(dict_dir, inp_name[:-4] + '_dict_left.txt'))
            outp_dirs.append(os.path.join(new_dir, inp_name))


    # parsing files
    corp = Corpus()
    corp.clean_corpus(corp_inps=corp_inp_dirs,
                      dict_inps=dict_inp_dirs,
                      outps=outp_dirs,
                      dict_type='keep')

if __name__ == '__main__':
    Corpus_clean_tester()
    # Corpus_parse_tester()


