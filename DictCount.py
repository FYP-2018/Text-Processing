import os
import math
from collections import defaultdict
import matplotlib.pyplot as plt
from PreprocessUtils import readFile


class Dict():
    def __init__(self):
        pass
    
    
    def _zero_list(self, length):
        """
        A function passing to defaultdict
        
        Args:
            param1 (int): length of list the returned function will generate
        Return:
            a function defining the initial state for defaultdit
        """
        return lambda: [0] * length
    
    
    def save_dict(self, inps, outps, record_tf=False, record_df=False):
        # the default value for each KEY:
        length = max(1, record_tf + record_df)
        
        for inp, outp in zip(inps, outps):
            print(inp, outp)
            word_dict = defaultdict(self._zero_list(length))
            
            num_articles = 0
            for line in readFile(inp, format='list'):
                for word in line:
                    word_dict[word][0] += 1
                
                if record_df:
                    num_articles += 1
                    for word in set(line):
                        word_dict[word][-1] += 1
            
            with open(outp, 'w', encoding='utf-8') as fout:
                if num_articles != 0:
                    fout.write(str(num_articles) + '\n')

                for k, v in word_dict.items():
                    if not record_tf and not record_df:
                        fout.write(k + '\n')
                    else:
                        v = [str(vi) for vi in v]
                        fout.write(k + ' ' + ' '.join(v) + '\n')
            
            print("prepared dict with {} words".format(len(word_dict)))
    
    
    def plot_dict(self, inps, outp_dirs, bins=50, tf_thred=0, df_thred=0, df_type='count'):
        """
        
        Args:
            inps: a list of pathes to the files
            outp_dirs: a list of pathes to the directories! (cannot be the path to a file)
            
            df_type: 'count' or 'ratio'
        """
        if df_type == 'ratio':
            df_thred = float(df_thred)/num_articles

        for i, inp in enumerate(inps):
            plt.clf()  # clear figure for each plot
            
            words = []
            for line in readFile(inp, format='list'):
                if len(line) == 1:  # the first line:
                    print(line)
                    num_articles = int(line[0])
                    continue  # not adding first line into dict
            
                for j in range(1, len(line)):
                    line[j] = int(line[j])
                    if df_type == 'ratio' and j == 2:
                        line[j] = round(float(line[j]) / num_articles, 4)

                if line[1] > tf_thred:
                    if len(line) == 2 or line[2] > df_thred:
                        words.append(line)
        
            with open(outp_dirs[i] + '_stat.txt', 'w', encoding='utf-8') as fout:
                for j in range(1, len(words[0])):
                    print(j)
                    words = sorted(words, reverse=True, key=lambda w: w[j])  # sort according to tf
                    
                    # plot current value distribution
                    values = [w[j] for w in words]
                    plt.subplot(1, len(words[0]) - 1, j)
                    if j == 1:
                        plt.hist(values, bins=bins, range=(0, max(values) / 10))
                    elif j == 2:
                        plt.hist(values, bins=bins, range=(0, 10))

                    
                    # record the most tf 10 words in each bins
                    total_words = len(words)
                    bin_width = total_words // bins
                    for bin_i in range(bins):
                        sta_idx = bin_i * bin_width
                        end_idx = min(bin_i * bin_width + 10, len(words))
                        record_words = []
                        for word in words[sta_idx:end_idx]:
                            word = [str(w) for w in (word[:j] + word[j+1:])]
                            record_words.append('-'.join(word))
                        
                        fout.write("[{} to {}]: {}\n".format(values[sta_idx],
                                                             values[end_idx],
                                                             '  '.join(record_words)))
                    fout.write("\n")
                plt.savefig(outp_dirs[i] + '_plot.png')
                print(inp + " is ploted")


    def prepare_stopwords(self, inps, outps, tf_range=(0, math.inf), df_range=(0, math.inf),
                          save_true_dict=False):
        '''
        def _scale_to_int(v, n):
            assert (v >= 0), "ratio is less than 0!")
            if v <= 1 and isinstance(v, float):
                return int(v * n)
            elif v >= 1:
                return v

        tf_range[0] = _scale_to_int(tf_range[0], )
        tf_range[0] = _scale_to_int(tf_range[0])
        tf_range[0] = _scale_to_int(tf_range[0])
        tf_range[0] = _scale_to_int(tf_range[0])
        '''
        
        for inp, outp in zip(inps, outps):
            f = open(outp, 'w', encoding='utf-8')
            if save_true_dict:
                f_leftvocab = open(outp[:-4] + '_left.txt', 'w', encoding='utf-8')
            
            inpf = readFile(inp, format='list')
            num_articles = next(inpf)
            print(num_articles)
            for line in inpf:
                if len(line) != 3:
                    raise ValueError("Expect input dictionary contains both tf and df")

                word, tf, df = line
                tf, df = int(tf), int(df)
                
                if tf <= tf_range[0] or tf >= tf_range[1] or df <= df_range[0] or df >= df_range[1]:
                    f.write(word + '\n')
                elif save_true_dict:
                    f_leftvocab.write(word + '\n')
                    
            f.close()
            if save_true_dict:
                f_leftvocab.close()

            print("stopwords for {} is generated".format(inp))

