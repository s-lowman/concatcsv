#!/usr/bin/env python

import pandas as pd
import glob

def concatCSV(dirpath):
    csvfiles = glob.glob(dirpath + '/*.csv')
    df = pd.concat((pd.read_csv(f) for f in csvfiles))
    df.to_csv('concat.csv', index=False)

def countLinesInFiles(dirpath):
    csvfiles = glob.glob(dirpath + '/*.csv')
    i = 0
    numLines = 0
    for f in csvfiles:
        with open(f, 'r') as f:
            for i, l in enumerate(f):
                if i == 0:
                    continue
                numLines += 1
                pass
    return numLines

def countFiles(dirpath):
    csvfiles = glob.glob(dirpath + '/*.csv')
    return len(csvfiles)

def countLines():
    i = 0
    with open('concat.csv', 'r') as f:
        for i, _ in enumerate(f):
            pass
    if i == 0:
        return 0
    return i + 1

if __name__ == '__main__':
    import sys
    print('Concatenating CSV files in directory: ' + sys.argv[1])
    concatCSV(sys.argv[1])
    print('Done')
    print('')
    print('Summary:')
    print('csv files concatenated in file: concat.csv')
    print('Number of lines in source files: ' + str(countLinesInFiles(sys.argv[1])))
    print('Number of files concatenated: ' + str(countFiles(sys.argv[1])))
    print('Number of lines in combined file (including header): ' + str(countLines()))
