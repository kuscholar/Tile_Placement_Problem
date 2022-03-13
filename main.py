'''
Purpose: main function for the tile placement problem.
Create Date: 2/21/2022
Author: Kusch
'''
import fileReader
from csp import *
from tiles import *
from time import time

DEFAULT_FILE = 'input1.txt'
def main(file_name: str):
    landScape, tiles, targets = fileReader.readTxt(file_name)
    tiles = Tiles(landScape, tiles, targets)
    time_start = time()
    result = backtracking_search(tiles)
    time_end = time()
    print("---" * 30)
    print("Final assignment: ", result)

    tilesUsed, visibleBushes = checkResult(result, tiles)
    print("Tiles available: ", tiles.availableTiles)
    print("Tiles used: ", tilesUsed)
    print("Target bushes: ", tiles.targets)
    print("Visible bushes: ", visibleBushes)
    print("Time used: ", round(time_end - time_start, 4))
    print("Detailed assignment: ")
    printDetailedAssignment(result)


def printDetailedAssignment(result):
    """
    print the assignment in the same way as shown in the project document: from top to bottom, from left to right
    :param result:
    :return:
    """

    for tile in range(TILES_NUMBER):
        col = tile // TILES_PER_ROW
        oldIndex = tile % TILES_PER_ROW * TILES_PER_ROW + col

        typeOfTile = result[oldIndex]
        tileName = TILE_NAMES[typeOfTile]
        print(tile, tileName)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_str = input("Input file name: ")
    if input_str == '':
        input_str = DEFAULT_FILE
    main(input_str)