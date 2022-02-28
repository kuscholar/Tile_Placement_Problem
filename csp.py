'''
purpose: The main constraint satisfaction problem algorithm, integrating AC3 algorithm
Created date: 2/27/2022
Author: Kusch
'''
from tiles import *


class CSP:

'''
workflow:
    1. initialize the CSP algorithm with given landScape, tiles, and targets
    2. Calculate original visible bushes by using functions imported from tiles.py
    3. Heuristics: choose the first variable by using MRV, choose the next value by selecting the least constraining value
    4. Reduce the search space by implementing the AC3 algorithm
    5. Use Backtracking algorithm to search for a possible solution
'''
    def __init__(self, landScape, tiles, targets):
        self.landScape = landScape
        self.tiles = tiles
        self.targets = targets
        self.colors = self.landScape.

