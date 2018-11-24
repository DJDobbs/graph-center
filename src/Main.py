import FloydWarshall as fw
import GraphCenter as gc

# N is used to represent infinity. This must always be greater than any edge weight in the graph.
N = 999999999

# Graphs are represented by an adjacency matrix.

# The center of this graph should be 3.
# testGraph = [[0, N, N, 1],
#               [N, 0, N, 1],
#               [N, N, 0, 1],
#               [1, 1, 1, 0]]

# The center of this graph should be 1.
# testGraph = [[0, 1, N, N],
#               [1, 0, 1, N],
#               [N, 1, 0, 1],
#               [N, N, 0, 1]]

# The center of this graph should be 4.
testGraph = [[0, N, N, N, 1],
              [N, 0, N, N, 2],
              [N, N, 0, N, 1],
              [N, N, N, 0, 2],
              [1, 2, 1, 2, 0]]

def main():
    shortestPaths = fw.findShortestPaths(testGraph)
    centerNode = gc.findCenter(shortestPaths)
    print("The center of this graph is node " + str(centerNode) + ".")

main()