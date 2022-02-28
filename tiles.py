'''
purpose: for tile placement actions, such as calculating bushes
Created date: 2/26/2022
Author: Kusch
'''
from fileReader import *

class Tiles:
    '''
    when class Tiles is initialized, the inputs are landScape, tiles;
    there should be functions such as check current visible bushes, check current available tiles, etc.
    '''
    def __init__(self, landScape, tiles):
        self.landScape = landScape
        self.tiles = tiles
        self.visibleBushes = [0, 0, 0, 0]  # a list of int, recording the numbers of visible bush colors in the order of 1,2,3,4
        self.availableTiles = tiles  # a list of int, recording the numbers of available tiles in the order of outer, el, full
        for cell in range(TILES_NUMBER):
            self.updateVisibleBushes(self.visibleBushes, self.bushesInCell(self.landScape[cell]))

    
    def updateVisibleBushes(self, visibleBushes, bushesInCell): # tested working fine on 2/27/2022
        '''
        once upon a cell, update the total number of bush colors by adding up the bush colors inside the current cell
        :param visibleBushes: the global variable inside the class, to record the total numbers of bush colors
        :param bushesInCell: the local variable to record the numbers of bush colors in the current cell
        :return: a void function, just update self.visibleBushes
        '''
        for color in range(len(visibleBushes)):
            self.visibleBushes[color] += bushesInCell[color]

    def bushesInCell(self, cell): # tested working fine on 2/27/2022
        '''
        count the numbers of bush colors
        :param cell: a 4x4 cell inside a landScape
        :return: the numbers of bush colors in the order of color 1,2,3,4
        '''
        bushes = [0, 0, 0, 0]
        for row in range(len(cell)):
            for col in range(len(cell[0])):
                color = cell[row][col]
                if color == 0:
                    continue
                bushes[color - 1] += 1
        return bushes

if __name__ == '__main__':
    '''
    test if Tiles is initialized correctly
    '''
    testLandScape = [[[2, 2, 1, 3], [0, 2, 1, 3], [2, 1, 0, 0], [0, 3, 2, 0]],
                     [[0, 3, 4, 0], [2, 2, 0, 0], [0, 2, 2, 4], [1, 0, 1, 1]],
                     [[4, 2, 2, 4], [0, 1, 0, 1], [3, 2, 2, 2], [4, 1, 3, 4]],
                     [[0, 4, 0, 0], [2, 2, 0, 2], [1, 2, 2, 0], [2, 1, 0, 0]],
                     [[0, 2, 4, 3], [3, 4, 4, 4], [0, 1, 1, 0], [0, 1, 4, 1]],
                     [[4, 2, 3, 4], [2, 4, 1, 0], [4, 3, 1, 4], [2, 1, 1, 1]],
                     [[4, 4, 0, 2], [1, 1, 1, 4], [3, 3, 1, 4], [4, 4, 3, 4]],
                     [[2, 0, 0, 3], [1, 0, 1, 3], [0, 1, 1, 1], [4, 2, 0, 3]],
                     [[2, 3, 0, 2], [0, 3, 2, 0], [4, 2, 2, 4], [0, 3, 0, 3]],
                     [[0, 2, 3, 2], [4, 0, 1, 2], [1, 4, 3, 4], [4, 4, 0, 0]],
                     [[1, 0, 0, 3], [0, 1, 3, 1], [0, 3, 0, 2], [1, 3, 1, 1]],
                     [[0, 3, 2, 2], [3, 2, 3, 2], [3, 4, 3, 3], [4, 4, 4, 2]],
                     [[4, 3, 3, 2], [1, 0, 0, 1], [1, 0, 0, 1], [0, 4, 4, 3]],
                     [[4, 0, 0, 0], [4, 3, 2, 1], [2, 3, 3, 0], [4, 1, 1, 2]],
                     [[1, 4, 3, 0], [2, 4, 1, 3], [2, 1, 2, 3], [2, 3, 2, 3]],
                     [[2, 1, 0, 1], [4, 2, 0, 0], [3, 1, 4, 3], [3, 2, 2, 4]],
                     [[1, 1, 0, 1], [2, 3, 2, 1], [0, 1, 4, 4], [3, 1, 1, 4]],
                     [[2, 1, 3, 2], [1, 1, 4, 0], [1, 1, 3, 1], [1, 0, 0, 3]],
                     [[2, 3, 3, 4], [4, 4, 3, 2], [1, 1, 0, 0], [1, 2, 3, 2]],
                     [[0, 0, 3, 4], [2, 0, 2, 3], [2, 1, 2, 0], [2, 2, 3, 4]],
                     [[0, 2, 2, 1], [0, 1, 4, 3], [3, 2, 1, 2], [4, 0, 3, 4]],
                     [[3, 3, 1, 1], [0, 0, 1, 1], [0, 3, 1, 1], [0, 4, 3, 4]],
                     [[0, 0, 0, 3], [3, 3, 0, 4], [3, 4, 2, 4], [3, 2, 2, 2]],
                     [[0, 4, 4, 2], [3, 4, 4, 4], [0, 3, 0, 2], [1, 4, 3, 4]],
                     [[2, 2, 4, 4], [4, 1, 1, 1], [0, 0, 4, 1], [3, 0, 0, 1]]]
    testLandScape2 = \
    [[[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 2]], [[3, 0, 3, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[1, 0, 1, 0], [2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    testLandScape3 = [[[] for _ in range(TILE_SIZE)] for _ in range(TILES_NUMBER)]
    for tile in range(TILES_NUMBER):
        for row in range(TILE_SIZE):
            for col in range(TILE_SIZE):
                testLandScape3[tile][row].append(0)

    testTiles = [6,7,12]
    test = Tiles(testLandScape, testTiles)
    print(test.visibleBushes)
