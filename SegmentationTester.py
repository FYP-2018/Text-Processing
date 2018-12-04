import os
import glob

import thulac

from Segmentation import ChineseParser
from PreprocessUtils import readFile

def ChineseParser_tester():
    # preparing inps and outps
    user_dict = '/Users/user/Desktop/dataset/HKNEWS_full/hk_words/dict.txt.big.txt'
    
    inp_dirs = []
    outp_dirs = []
    root_dir = '/Users/user/Desktop/dataset/HKNEWS_full/Categories/'
    
    for f in glob.glob(os.path.join(root_dir, '*', '*.txt')):
        cate_name = f.split('/')[-2]
        inp_name = f.split('/')[-1]
        if '_prev.txt' not in inp_name and '_id.txt' not in inp_name:
            new_dir = os.path.join(root_dir, cate_name, 'thulac')
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
        
            inp_dirs.append(f)
            outp_dirs.append(os.path.join(new_dir, inp_name))

    # parsing files
    cp = ChineseParser()
    cp.parse(inp_dirs=inp_dirs,
             outp_dirs=outp_dirs,
             type='word',
             user_dict=user_dict)


if __name__ == '__main__':
     ChineseParser_tester()


