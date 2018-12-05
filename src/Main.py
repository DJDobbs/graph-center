import FloydWarshall as fw
import GraphCenter as gc

# N is used to represent infinity. This must always be greater than any edge-weight in the graph.
N = 999999999

# Graphs are represented by an adjacency matrix.
# The numbers in the matrix represent the weight of the edge that connects the two nodes.
# The edge-weight of any node to itself is 0.
# The edge-weight of any pair of nodes that are not connected is N. (infinity)
# Test graphs can be uncommented individually to show that the algorithm is working.

# Test Graph 1: The center of this graph should be 3.
graphMatrix = [[0, N, N, 1],
               [N, 0, N, 1],
               [N, N, 0, 1],
               [1, 1, 1, 0]]

# Test Graph 2: The center of this graph should be 1.
# graphMatrix = [[0, 1, N, N],
#                [1, 0, 1, N],
#                [N, 1, 0, 1],
#                [N, N, 0, 1]]

# Test Graph 3: The center of this graph should be 4.
# graphMatrix = [[0, N, N, N, 1],
#                [N, 0, N, N, 2],
#                [N, N, 0, N, 1],
#                [N, N, N, 0, 2],
#                [1, 2, 1, 2, 0]]

def main():
    shortestPaths = fw.findShortestPaths(graphMatrix)
    centerNode = gc.findCenter(shortestPaths)
    print("The center of this graph is node " + str(centerNode) + ".")

main()
