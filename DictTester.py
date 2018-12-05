import os
import glob
import math

import thulac

from Dict import Dict


def DictCount_savedict_tester():
    # preparing inps and outps
    user_dict = '/Users/user/Desktop/dataset/HKNEWS_full/hk_words/dict.txt.big.txt'
    
    inp_dirs = []
    outp_dirs = []
    root_dir = '/Users/user/Desktop/dataset/HKNEWS_full/Categories/thulac'
    
    new_dir = os.path.join(root_dir, 'dict')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    
    for f in glob.glob(os.path.join(root_dir, '*.txt')):
        inp_name = f.split('/')[-1][:-4]  # get the input name without .txt
        
        if '_dict.txt' not in inp_name:
            inp_dirs.append(f)
            outp_dirs.append(os.path.join(new_dir, inp_name + '_dict.txt'))
    
    # preparing dicts
    d = Dict()
    d.save_dict(inp_dirs, outp_dirs,
                record_freq=True,
                record_df=True)


def DictCount_plotdict_tester():
    root_dir = '/Users/user/Desktop/dataset/HKNEWS_full/Categories/thulac'
    
    inp_dirs = []
    outp_dirs = []
    
    new_dir = os.path.join(root_dir, 'dict_plot')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    
    for f in glob.glob(os.path.join(root_dir, 'dict', '*.txt')):
        inp_name = f.split('/')[-1][:-4]  # get the input name without .txt
        
        if '_title' not in inp_name:  # only cares about the dict for content
            inp_dirs.append(f)
            outp_dirs.append(os.path.join(new_dir, inp_name))

    d = Dict()
    d.plot_dict(inp_dirs, outp_dirs,
                tf_thred=2,
                df_thred=2)

def DictCount_prep_stopwords_tester():
    root_dir = '/Users/user/Desktop/dataset/HKNEWS_full/Categories/thulac'
    
    inp_dirs = []
    outp_dirs = []
    
    new_dir = os.path.join(root_dir, 'dict_no_sw')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    
    for f in glob.glob(os.path.join(root_dir, 'dict', '*.txt')):
        print(f)
        inp_name = f.split('/')[-1]

        if '_title' not in inp_name:  # only cares about the dict for content
            inp_dirs.append(f)
            outp_dirs.append(os.path.join(new_dir, inp_name))
                
    d = Dict()
    d.prep_stopwords(inp_dirs, outp_dirs,
                        tf_range=(2, math.inf),
                        df_range=(2, 11),
                        save_true_dict=True)


if __name__ == '__main__':
    # DictCount_prep_stopwords_tester()
    # DictCount_plotdict_tester()
    # DictCount_savedict_tester()
