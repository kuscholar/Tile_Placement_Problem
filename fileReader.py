'''
purpose: as named, fileReader, to read input files, and output as needed
Created date: 2/21/2022
Author: Kusch
'''
import logging
import os
import re

# parameters for input file, subject to change if the format changes
LS_LINE_START = 2 # landscape line start
LS_LINE_END = 21
TILES_LINE = 24
TARGETS_LINE = 27

def readTxt(fileName: str):
    '''

    :param name:
        fileName(str): the name of the input file (.txt), it could be with or without the suffix
    :return:
        landScape([int][int]): graph of the landScape, output as a matrix
        tiles([int])： list of the numbers of three kinds of tiles;
            tiles[0]: # of outer_boundary
            tiles[1]: # of el_shape
            tiles[2]: # of full_block
        targets([int]): target number of four kinds of colored bushes visible
            targets[0]: # of color 1
            targets[1]: # of color 2
            targets[2]: # of color 3
            targets[3]: # of color 4
        solutions([int]): TBD, for assertion later, can leave it for now
    '''
    landScape = [[] for _ in range(LS_LINE_END - LS_LINE_START + 1)]
    if os.path.splitext(fileName)[1] != '.txt':
        fileName += '.txt'
    try:
        with open('input/' + fileName, 'r') as f:
            contents = f.readlines()
            for line in range(LS_LINE_START, LS_LINE_END + 1):
                for num in range(0, len(contents[line]) - 1, 2):
                    if contents[line][num] == ' ':
                        landScape[line-2].append(0)
                    else:
                        landScape[line-2].append(int(contents[line][num]))
            temp = re.findall(r'\d+', contents[TILES_LINE])
            tiles = list(map(int, temp))
            targets = []
            for line in range(TARGETS_LINE, TARGETS_LINE + 4):
                targets.append(int(contents[line][2:4]))
            return landScape, tiles, targets
    except FileNotFoundError:
        logging.error('FileNotFoundError:' + fileName)
        return [[]], [0, 0, 0], [0, 0, 0, 0]


if __name__ == '__main__':
    print(readTxt('input1.txt'))


