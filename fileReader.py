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
TILE_SIZE = 4
TILES_NUMBER = 25
TILES_PER_ROW = 5
TILE_NAMES = {0: "OUTER_BOUNDARY", 1: "EL_SHAPE", 2: "FULL_BLOCK"}
PRINT_ASSIGNMENT = False

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

        newLandScape([int][int][int]): graph of the landScape, in form of each tile is a matrix
            e.g.: [[[2,2,1,3],[0,2,1,3],[2,1,0,0],[0,3,2,0]],[[0,0,0,0],...],...]
            namely: [[[2,2,1,3],  [[0,0,0,0],
                      [0,2,1,3],   [0,0,0,0],
                      [2,1,0,0],   [0,0,0,0],
                      [0,3,2,0]],  [0,0,0,0]], ...
                      ...            ...              ...     ]
            The order of tiles is from left to right, top to bottom

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
            numOfTiles = (len(landScape) // TILE_SIZE) * (len(landScape[0]) // TILE_SIZE)  # 25
            numOfTilesPerRow = len(landScape) // TILE_SIZE  # 5
            newLandScape = [[[] for _ in range(TILE_SIZE)] for _ in range(numOfTiles)]
            for tile in range(numOfTiles):
                for row in range(TILE_SIZE):
                    for col in range(TILE_SIZE):
                        newLandScape[tile][row].append(landScape[tile//numOfTilesPerRow * TILE_SIZE + row][tile%numOfTilesPerRow * TILE_SIZE + col])
            return newLandScape, tiles, targets
    except FileNotFoundError:
        logging.error('FileNotFoundError:' + fileName)
        return [[[]]], [0, 0, 0], [0, 0, 0, 0]


if __name__ == '__main__':
    print(readTxt('input1.txt'))


