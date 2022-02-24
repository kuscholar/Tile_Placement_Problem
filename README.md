# Tile_Placement_Problem
Project 2 for AI, find solution for tile placement problem using CSP algorithm

Algorithm
Write a CSP algorithm to solve this problem. 
The CSP algorithm should have the following components:

• Search algorithm to solve the CSP.

• Heuristics (min remaining values, least constraining value).

• Constraint propagation using AC3.

# AC3 sudo code:

  Input:
     A set of variables X
     A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, the possible values of x
     A set of unary constraints R1(x) on variable x that must be satisfied
     A set of binary constraints R2(x, y) on variables x and y that must be satisfied

  Output:
     Arc consistent domains for each variable.

    function ac3 (X, D, R1, R2)
         // Initial domains are made consistent with unary constraints.
         for each x in X
             D(x) := { vx in D(x) | vx satisfies R1(x) }   
         // 'worklist' contains all arcs we wish to prove consistent or not.
         worklist := { (x, y) | there exists a relation R2(x, y) or a relation R2(y, x) }

         do
             select any arc (x, y) from worklist
             worklist := worklist - (x, y)
             if arc-reduce (x, y) 
                 if D(x) is empty
                     return failure
                 else
                     worklist := worklist + { (z, x) | z != y and there exists a relation R2(x, z) or a relation R2(z, x) }
         while worklist not empty

    function arc-reduce (x, y)
         bool change = false
         for each vx in D(x)
             find a value vy in D(y) such that vx and vy satisfy the constraint R2(x, y)
             if there is no such vy {
                 D(x) := D(x) - vx
                 change := true
             }
         return change



Reference: https://en.wikipedia.org/wiki/AC-3_algorithm
