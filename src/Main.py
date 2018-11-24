import FloydWarshall as fw
import GraphCenter as gc

# N is used to represent infinity. This should be greater than any edge weights in the graph.
N = 9999

# Graphs are represented by an adjacency matrix.

# The center of this graph should be 3.
testGraph1 = [[0, N, N, 1],
              [N, 0, N, 1],
              [N, N, 0, 1],
              [1, 1, 1, 0]]

# The center of this graph should be 1.
testGraph2 = [[0, 1, N, N],
              [1, 0, 1, N],
              [N, 1, 0, 1],
              [N, N, 0, 1]]

# The center of this graph should be 4.
testGraph3 = [[0, N, N, N, 1],
              [N, 0, N, N, 2],
              [N, N, 0, N, 1],
              [N, N, N, 0, 2],
              [1, 2, 1, 2, 0]]

def main():
    shortestPaths = fw.AllPairsShortestPath(testGraph1)
    centerNode = gc.findCenter(shortestPaths)
    print(centerNode)

main()