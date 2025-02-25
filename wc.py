# import pickle
import sys
from string import punctuation
import argparse
import os
import pickle

wordDict = {}

def wordfreq(fname, stripPunc, toLower) :
    with open(fname) as f:
        ## let's just get all the words at once.
        words = f.read().split()
        for word in words :
            if stripPunc :
                word = word.strip(punctuation)
            if toLower :
                word = word.lower()
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1
    return wordDict

if __name__== '__main__':
    # if len(sys.argv) < 2:
    #     print("Usage: wordfreq {--strip --convert -pfile=outfile} file")
    #     sys.exit(-1)
    #     fname = sys.argv[-1]
    #     strip = '--strip' in sys.argv
    #     convert = '--convert' in sys.argv
    #     wd = wordfreq(fname, stripPunc=strip, toLower=convert)
    #     pickled = False
    #     for arg in sys.argv:
    #         if arg.startswith('--pfile'):
    #             ofile = arg.split('=')[1]
    #             pickle.dump(wd, open(ofile, 'w'))
    #             pickled = True
    #     if not pickled:
    #         print(wd)
    # else:
    # parser = argparse.ArgumentParser("Reading a file")
    # parser.add_argument('file', help= 'Path of file you want to read')
    parser = argparse.ArgumentParser('Reading a directory')
    parser.add_argument('directory', help ='Directory you want to read')
    parser.add_argument('--strip', action='store_true', help='Strip punctuation')
    parser.add_argument('--convert', action='store_true', help='Convert to lowercase')
    parser.add_argument('--load', type=str, help='Load frequency distribution from file')
    parser.add_argument('--save', type=str, help='Save frequency distribution to file')
    parser.add_argument('-s', action='store_true', help='Sort words according to increasing frequency')
    # global_wd = {}

    args = parser.parse_args()

    if args.load:
        with open(args.load, 'rb') as f:
            wordDict = pickle.load(f)
            print('Inside load')
            print(wordDict)

    dir = args.directory
    for root, dirs, files in os.walk(dir):
        for file in files:
            full_path = os.path.join(root, file)
            strip = '--strip' in sys.argv
            convert = '--convert' in sys.argv
            wd = wordfreq(full_path, stripPunc=strip, toLower=convert)
    # print(wd)
    if(args.s):
        sorted_wordDict = sorted(wordDict.items(), key=lambda x:x[1])
        print('Words sorted in increasing order of frequency are below')
        print(sorted_wordDict)
    pickled = False
    for arg in sys.argv:
        # if arg.startswith('--load'):
        #     # ofile = arg.split('=')[1]
        #     #         pickle.dump(wd, open(ofile, 'w'))
        #     with open(args.load, 'rb') as f:
        #         wordDict = pickle.load(f)
        #     print('Inside load')
        #     print(wordDict)
        #     pickled = True
        if arg.startswith('--save'):
            print('Inside save')
            with open(args.save, 'wb') as f:
                pickle.dump(wordDict, f)
            pickled = True


    if not pickled:
        print('Not pickled')
        print(wordDict)

    # if args.save:
    #     with open(args.save, 'wb') as f:
    #         pickle.dump(wordDict, f)