# DAGstratification_algorithm

Python script to determine order and heirarchy in directed graphs containing Nodes and Edges.

## Contents of repo
- Stratification.py (commented and cleaned up python script)
- StratificationRAW.py (rough and uncommented python script)
- SampleInput[x] (Sample inputs)

## Explanation
Explained here: http://www.sciencedirect.com/science/article/pii/S0012365X03000785

Credit to Discrete Mathematics textbook (2003) by Gary Chartrand, Teresa Haynes, Michael Henning, Ping Zhang.

Specifically taken from Stratification and "Domination in Graphs seciton"

## Input
Script takes inputs from command line in following format

[Number of edges]
n[Edge]

For example:

  3
  
  1 2
  
  2 3
  
  3 2
  
  [3 edges, with 1->2, 2->3, 3->2]
