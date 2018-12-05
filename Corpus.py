import thulac
from PreprocessUtils import readFile


class Corpus():
    def __init__(self):
        pass
    
    
    def _load_thulac(self, user_dict=None):
        print("initializing thulac...")
        if user_dict == None:
            self.thu = thulac.thulac(seg_only=True)
        else:
            self.thu = thulac.thulac(user_dict=user_dict, seg_only=True)

    
    def parse(self, inp_dirs, outp_dirs, type='word', user_dict=None):
        """
        Args:
            param1 (str): a list of input files directories
            param2 (str): a list of expected onput files directories
            param3 (:obj:`str`, optional):
                options for parsing criteria, 'word'/'char'
                Defaults to word.
                'word' - segment
                'char'  - return each line of doc as a list of word
        """
        if len(inp_dirs) != len(outp_dirs):
            raise ValueError("Number of input directories should be same with output directories")
                
        if type != 'word' and type != 'char':
            raise ValueError("Invalid parsing type! Need to be either 'word' or 'char'")


        if type == 'word':
            self._load_thulac(user_dict=user_dict)
            for inp_dir, outp_dir in zip(inp_dirs, outp_dirs):
                print("converting {} to {}".format(inp_dir, outp_dir))
                self.thu.cut_f(inp_dir, outp_dir)

        elif type == 'char':
            for inp_dir, outp_dir in zip(inp_dirs, outp_dirs):
                print("converting {} to {}".format(inp_dir, outp_dir))
                
                fout = open(outp_dir, 'w', encoding='utf-8')
                for line in readFile(inp_dir, format='plain'):
                    line = ' '.join(line)  # since str is intrinsically a list of char
                    fout.write(line.strip() + '\n')
                fout.close()
            num_files = len(len(inp_dirs))
            print("processed {} docs in {}".format(num_files, fdir))

        print("Finished Parsing")


    def clean_corpus(self, corp_inps, dict_inps, outps, dict_type='keep'):
        """
            Process the input corpus accoding to dict: either keep the words in dict
            or remove the words in dict
            
            Args:
            param 1, 2, 3 (list): a list of file directory for corpus, dict, and output corpus
            param 4 (str): 'keep' or 'remove'
                'keep': only keep the words in dict
                'remove': remove the words in dict from original corpus
        """
        for corp_inp, dict_inp, outp in zip(corp_inps, dict_inps, outps):
            print(corp_inp)
            with open(dict_inp, 'r', encoding='utf-8') as dict_f:
                dict = [w.strip() for w in dict_f.readlines()]
            print("{} words in loaded dict".format(len(dict)))

            num_file = 0
            with open(outp, 'w', encoding='utf-8') as outp_f:
                for line in readFile(corp_inp, format='list'):
                    if dict_type == 'keep':
                        line = [w for w in line if w in dict]
                    elif dict_type == 'remove':
                        line = [w for w in line if w not in dict]
            
                    if num_file % 50 == 0:
                        print("{} files processed".format(num_file))
                    num_file += 1
                    outp_f.write(' '.join(line) + '\n')
