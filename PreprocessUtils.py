import re
import thulac

from fire import Fire

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def check_length(fdirs):
    for fdir in fdirs:
        fin = open(fdir, 'r', encoding='utf-8')
        print(fdir, ': ', len(fin.readlines()))
        fin.close()


def _clean_sentence(sent):
    sent = sent.lower()
    filtrate = re.compile(u'[^\u4E00-\u9FA5\a-z]')  # non-Chinese unicode range
    context = filtrate.sub(r'', sent)  # remove all non-Chinese characters

    return context


def char_base_parsing(fdir, outp_dir):
    num_files = 0
    
    fout = open(outp_dir, 'w', encoding='utf-8')
    with open(fdir, 'r', encoding='utf-8') as f:
        num_files = 0
        for line in f.readlines():
            print(line)
            line = _clean_sentence(line)
            line = ' '.join(line)
            
            fout.write(line.strip() + '\n')
            print(line)
            num_files += 1
    fout.close()
    print("processed {} docs in {}".format(num_files, fdir))


def word_base_parsing(fdirs, outp_dirs):
    num_files = 0
    print("initializing thulac...")
    thu = thulac.thulac(user_dict='./hk_words/word_only_dict.txt.big.txt', seg_only=True)
    
    for fdir, outp_dir in zip(fdirs, outp_dirs):
        fdir = fdir + '.txt'
        cache_dir = outp_dir + '_prev.txt'
        outp_dir = outp_dir + '.txt'
        
        print("converting {} to {}".format(fdir, outp_dir))
        print("processing input...")
        
        thu.cut_f(fdir, cache_dir)
        
        print("removing stop words...")
        fout = open(outp_dir, 'w', encoding='utf-8')
        with open(cache_dir, 'r', encoding='utf-8') as f:
            num_files = 0
            while True:
                line = f.readline()
                if not line:
                    break
                
                if len(line) < 4:  # \n
                    continue
                
                fout.write(line)
                num_files += 1

        fout.close()
        print("processed {} docs in {}".format(num_files, fdir))


def _tmp_clean_file(fdir, outp_dir):
    fout = open(outp_dir, 'w', encoding='utf-8')
    with open(fdir, 'r', encoding='utf-8') as f:
        num_files = 0
        
        for line in f.readlines():
            line = _clean_sentence(line)
            stopwords = stopwordslist('./hk_words/stopwords_traditionalChinese.txt')
            
            outstr = []
            for word in line.split(" "):
                if word not in stopwords:
                    outstr.append(word)
            fout.write(' '.join(outstr) + '\n')
            
            num_files += 1

    fout.close()
    print("processed {} docs in {}".format(num_files, fdir))


# from here
def readFile(fpath, format='plain'): # tested
    """
    A function which memory-efficiently reads one line of text file each time
    \n is always removed for each line
    
    Args:
        param1 (str): the path of doc file you want to read from
        param2 (:obj:`str`, optional):
            options for returned value, 'plain'/'list'
            Defaults to plain.
            'plain' - return each line of doc file without any processing
            'list'  - return each line of doc as a list of word
    Returns:
        A generator, which produce one line of text file in requried format
    """
    
    if format != 'plain' and format != 'list':
        raise ValueError("Invalid Mode for readFile! Need to be either 'plain' or 'list'")

    with open(fpath, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            
            if format == 'plain':
                yield line.strip()
            elif format == 'list':
                yield line.strip().split()
