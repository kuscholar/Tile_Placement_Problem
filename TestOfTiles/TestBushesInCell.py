"""
FileName：TestBushesInCell.py
Author：kuscholar
Version：0.1
Date Created：2022-02-27
Introduction：
    Test cases to ensure functions in Tiles are working as expected
History：
    2022-02-27: created File
"""

import unittest
import sys
from pip import main
sys.path.append("..")
from tiles import *

class TestBushesInCell(unittest.TestCase):
    """
    This function should return the numbers of colors inside a cell, in the order of color 1,2,3,4
    """


    def test_bushes_in_cell1(self):
        """
        test for special cases: 0 to 0, or max to max, or max to 0, or 0 to max
        """

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

        testCells = Tiles(testLandScape,[1,1,1])
        
        self.assertEqual(testCells.bushesInCell(testCells.landScape[0]), [3, 5, 3, 0]) 

if __name__ == "__main__":
    """
    if all tests passed, there will not be a fail
    """
    unittest.main()