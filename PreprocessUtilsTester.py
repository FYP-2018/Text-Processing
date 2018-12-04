import re
import thulac

from PreprocessUtils import readFile


def readFileTester():
    dir = '/Users/user/Desktop/dataset/HKNEWS_full/FULL/full/full_char_title.txt'
    
    formats = ['plain', 'list']
    for f in formats:
        file = readFile(dir, format=f)
        for i in range(5):
            print(next(file))
        print('\n\n')


if __name__ == '__main__':
     readFileTester()

