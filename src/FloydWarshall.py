# This function should return a matrix that shows the shortest distances between every node.

def findShortestPaths(adjacenyMatrix):
    graphOrder = len(adjacenyMatrix)

    for k in range(graphOrder):
        for i in range(graphOrder):
            for j in range(graphOrder):
                if (adjacenyMatrix[i][k] + adjacenyMatrix[k][j]) < adjacenyMatrix[i][j]:
                    adjacenyMatrix[i][j] = adjacenyMatrix[i][k] + adjacenyMatrix[k][j]

    return adjacenyMatrix
