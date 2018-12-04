import thulac
from PreprocessUtils import readFile


class ChineseParser():
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

