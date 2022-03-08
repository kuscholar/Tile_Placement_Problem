'''
purpose: for tile placement actions, such as calculating bushes
Created date: 2/26/2022
Author: Kusch
'''
from fileReader import *
from csp import *
import copy



class UniversalDict:
    """A universal dict maps any key to the same value. We use it here
    as the domains dict for CSPs in which all variables have the same domain.
    >>> d = UniversalDict(42)
    >>> d['life']
    42

    {Any: [0, 1, 2]}
    """

    def __init__(self, value): self.value = value

    def __getitem__(self, key): return self.value

    def __repr__(self): return '{{Any: {0!r}}}'.format(self.value)

class Tiles(CSP):
    '''
    when class Tiles is initialized, the inputs are landScape, tiles;
    there should be functions such as check current visible bushes, check current available tiles, etc.

    input format:
        landScape([int][int]): graph of the landScape, input as a matrix
        tiles([int])： list of the numbers of three kinds of tiles;
            tiles[0]: # of outer_boundary
            tiles[1]: # of el_shape
            tiles[2]: # of full_block
        targets([int]): target number of four kinds of colored bushes visible
            targets[0]: # of color 1
            targets[1]: # of color 2
            targets[2]: # of color 3
            targets[3]: # of color 4
    '''
    def __init__(self, landScape, tiles, targets):
        self.landScape = landScape
        self.tiles = tiles
        self.targets = targets
        self.visibleBushes = [0, 0, 0, 0]  # a list of int, recording the numbers of visible bush colors in the order of 1,2,3,4
        self.availableTiles = tiles  # a list of int, recording the numbers of available tiles in the order of outer, el, full
        for cell in range(TILES_NUMBER):
            self.initVisibleBushes(self.visibleBushes, self.bushesInCell(self.landScape[cell]))
        CSP.__init__(self, list(range(len(landScape))), UniversalDict(list(range(len(tiles)))), UniversalDict(list(range(len(tiles)))),
                         self.tile_constraint)

    def tile_constraint(self, A, a, B, b, assignment):
        """
        constraints for tile placement, generally it's only the placement of tiles should not exceed the target and the number of tiles that we have
        :param A: var
        :param a: val
        :param B: var2
        :param b: assignment[var2]
        :return: boolean, whether this satisfies the constraints
        """
        # for i in range(len(self.tiles)):
        #     if self.availableTiles[i] < 0:
        #         return False
        # for i in range(len(self.visibleBushes)):
        #     if self.visibleBushes[i] < self.targets[i]:
        #         return False
        availableTiles = self.currAvailableTiles(assignment)
        for i in range(len(self.tiles)):
            if availableTiles[i] < 0:
                return False
        visibleBushes = self.currVisibleBushes(assignment)
        for i in range(len(self.visibleBushes)):
            if len(assignment) == len(self.landScape):
                if visibleBushes[i] != self.targets[i]:
                    return False
        return True

    def updateVisibleBushes(self, cellNumber, typeOfTile, isAssign, visibleBushes):
        """
        change this function to handle local variables instead
        :param cellNumber:
        :param typeOfTile:
        :param isAssign: a boolean, whether this is an assignment operation or not, allows this update to handle both ways
        :return: void, just update self.visibleBushes
        """
        cell = self.landScape[cellNumber]
        coveredBushes = self.bushesCovered(cell, typeOfTile)
        if isAssign:
            for i in range(len(coveredBushes)):
                visibleBushes[i] -= coveredBushes[i]
        else:
            for i in range(len(coveredBushes)):
                visibleBushes[i] += coveredBushes[i]

    def bushesCovered(self, cell, typeOfTile):
        bushes = [0, 0, 0, 0]
        if typeOfTile == 0:
            for i in range(len(cell[0])):
                color = cell[0][i]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            for i in range(len(cell[3])):
                color = cell[3][i]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            color = cell[1][0]
            if color != 0: bushes[color - 1] += 1
            color = cell[2][0]
            if color != 0: bushes[color - 1] += 1
            color = cell[1][3]
            if color != 0: bushes[color - 1] += 1
            color = cell[2][3]
            if color != 0: bushes[color - 1] += 1
            return bushes

        elif typeOfTile == 1:
            for i in range(len(cell[0])):
                color = cell[0][i]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            for i in range(1, len(cell)):
                color = cell[i][0]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            return bushes
        else:
            return self.bushesInCell(cell)

    def currAvailableTiles(self, assignment):
        # availableTiles = self.availableTiles
        currAvailableTiles = []
        for i in range(len(self.availableTiles)):
            currAvailableTiles.append(self.availableTiles[i])
        for tile in assignment.values():
            currAvailableTiles[tile] -= 1
        return currAvailableTiles

    def currVisibleBushes(self, assignment):
        currVisibleBushes = []
        # currVisibleBushes = self.visibleBushes   -> if the refered type is not primary type, the assign will be the reference, which will influence the original variable
        for i in range(len(self.visibleBushes)):
            currVisibleBushes.append(self.visibleBushes[i])
        for cell in assignment.keys():
            self.updateVisibleBushes(cell, assignment[cell], True, currVisibleBushes)
        return currVisibleBushes


    # these are overriding functions in csp.py

    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val
        self.nassigns += 1
        # self.availableTiles[val] -= 1
        # self.updateVisibleBushes(var, val, True)

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            val = assignment[var]
            del assignment[var]
            # self.availableTiles[val] += 1
            # self.updateVisibleBushes(var, val, False)

    def nconflicts(self, var, val, assignment):
        """# Return the number of conflicts var=val has with other variables.
            Return the number of conflicts this landScape have if var:val assigned"""
        count = 0
        self.assign(var, val, assignment)

        currAvailableTiles = self.currAvailableTiles(assignment)
        currVisibleBushes = self.currVisibleBushes(assignment)

        for i in range(len(self.tiles)):
            if currAvailableTiles[i] < 0:
                count += 1
        for i in range(len(self.visibleBushes)):
            # if currVisibleBushes[i] < self.targets[i] + 3:  # 5 is just a random number , should be the number of bushes if assign here
            #     if currVisibleBushes[i] != self.targets[i]:
            if len(assignment) == len(self.landScape):
                if currVisibleBushes[i] != self.targets[i]:
                    count += 1

        self.unassign(var, assignment)
        return count
        # Subclasses may implement this more efficiently
        # def conflict(var2):
        #     return var2 in assignment and not self.constraints(var, val, var2, assignment[var2])
        #
        # return count(conflict(v) for v in self.neighbors[var])


    def display(self, assignment):
        """Show a human-readable representation of the CSP."""
        # Subclasses can print in a prettier way, or display with a GUI
        print(assignment)

        # These are for constraint propagation

    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        """Start accumulating inferences from assuming var=value."""
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    # above are overriden functions



    def initVisibleBushes(self, visibleBushes, bushesInCell): # tested working fine on 2/27/2022
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

# ______________________________________________________________________________
# Constraint Propagation with AC3


def no_arc_heuristic(csp, queue):
    return queue


def dom_j_up(csp, queue):
    return SortedSet(queue, key=lambda t: neg(len(csp.curr_domains[t[1]])))


def AC3(csp, assignment, queue=None, removals=None, arc_heuristic=dom_j_up):
    """[Figure 6.3]"""
    if queue is None:
        queue = {(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]}
    csp.support_pruning()
    queue = arc_heuristic(csp, queue)
    checks = 0
    while queue:
        (Xi, Xj) = queue.pop()
        revised, checks = revise(csp, assignment, Xi, Xj, removals, checks) # here added another variable for constraints, is for Tiles class
        if revised:
            if not csp.curr_domains[Xi]:
                return False, checks  # CSP is inconsistent
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.add((Xk, Xi))
    return True, checks  # CSP is satisfiable


def revise(csp, assignment, Xi, Xj, removals, checks=0): # here added another variable for constraints, is for Tiles class
    """Return true if we remove a value."""
    revised = False
    for x in csp.curr_domains[Xi][:]:
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        # if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
        conflict = True
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y, assignment): # here added another variable for constraints, is for Tiles class
                conflict = False
            checks += 1
            if not conflict:
                break
        if conflict:
            csp.prune(Xi, x, removals)
            revised = True
    return revised, checks

# ______________________________________________________________________________
# CSP Backtracking Search @ overriden functions
# Inference

def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    csp.support_pruning()
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b, assignment):  # here added another variable for constraints, is for Tiles class
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    return True


def mac(csp, var, value, assignment, removals, constraint_propagation=AC3):
    """Maintain arc consistency."""
    return constraint_propagation(csp, assignment, {(X, var) for X in csp.neighbors[var]}, removals) # here added another variable for constraints, is for Tiles class


def backtracking_search(csp, select_unassigned_variable=mrv,
                        order_domain_values=lcv, inference=mac):
    """

    :param csp:
    :param select_unassigned_variable:
    :param order_domain_values:
    :param inference:
    :return:
    """

    def backtrack(assignment):
        # if len(assignment) == len(csp.variables) and checkResult(assignment, csp)[1] == csp.targets:
        if len(assignment) == len(csp.variables):
            return assignment

        var = select_unassigned_variable(assignment, csp)
        # print(assignment)
        # while not len(assignment) == len(csp.variables):
        for value in order_domain_values(var, assignment, csp):
            if 0 == csp.nconflicts(var, value,
                                   assignment):  # this means if we assign var and value here, how many conflicts we get
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    result = backtrack({})
    # assert result is None or csp.goal_test(result)
    return result

def checkResult(result, tiles):
    """
    Check if the result is correct, which should have the correct number of tiles used, and target numbers of bushes visible
    :param result: Dict of the final assignment
    :param tiles: Type of the class Tiles
    :return:
    """
    def updateVisibleBushes(cellNumber, typeOfTile, visibleBushes):

        cell = tiles.landScape[cellNumber]
        coveredBushes = bushesCovered(cell, typeOfTile)
        for i in range(len(coveredBushes)):
            visibleBushes[i] -= coveredBushes[i]


    def bushesCovered(cell, typeOfTile):
        bushes = [0, 0, 0, 0]
        if typeOfTile == 0:
            for i in range(len(cell[0])):
                color = cell[0][i]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            for i in range(len(cell[3])):
                color = cell[3][i]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            color = cell[1][0]
            if color != 0: bushes[color - 1] += 1
            color = cell[2][0]
            if color != 0: bushes[color - 1] += 1
            color = cell[1][3]
            if color != 0: bushes[color - 1] += 1
            color = cell[2][3]
            if color != 0: bushes[color - 1] += 1
            return bushes

        elif typeOfTile == 1:
            for i in range(len(cell[0])):
                color = cell[0][i]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            for i in range(1, len(cell)):
                color = cell[i][0]
                if color == 0:
                    continue
                bushes[color - 1] += 1
            return bushes
        else:
            return bushesInCell(cell)

    def bushesInCell(cell):

        bushes = [0, 0, 0, 0]
        for row in range(len(cell)):
            for col in range(len(cell[0])):
                color = cell[row][col]
                if color == 0:
                    continue
                bushes[color - 1] += 1
        return bushes

    tilesUsed = [0, 0, 0]
    visibleBushes = copy.deepcopy(tiles.visibleBushes)

    for cellNumber in result.keys():
        tilesUsed[result[cellNumber]] += 1
        updateVisibleBushes(cellNumber, result[cellNumber], visibleBushes)

    return tilesUsed, visibleBushes


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

    testTiles = [6, 7, 12]
    testTargets = [18, 19, 16, 17]
    test = Tiles(testLandScape, testTiles, testTargets)
    print(testLandScape, testTiles, testTargets)
    print(backtracking_search(test))
