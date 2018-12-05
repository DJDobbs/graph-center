# This function returns a new matrix that shows the shortest path between every pair of nodes.

def findShortestPaths(graphMatrix):
    shortestPaths = graphMatrix
    graphOrder = len(graphMatrix)

    for k in range(graphOrder):
        for i in range(graphOrder):
            for j in range(graphOrder):
                if (shortestPaths[i][k] + shortestPaths[k][j]) < shortestPaths[i][j]:
                    shortestPaths[i][j] = shortestPaths[i][k] + shortestPaths[k][j]

    return shortestPaths
