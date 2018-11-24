# This function should use the shortest distances to find and return the graph's most central node.

def findCenter(shortestPaths):
    graphOrder = len(shortestPaths)
    eccentricities = []
    centerNode = 0

    for i in range(graphOrder):
        eccentricities.append(0)
        for j in range(graphOrder):
            if (i != j) and shortestPaths[i][j] > eccentricities[i]:
                eccentricities[i] = shortestPaths[i][j]

    for i in range(graphOrder):
        if eccentricities[i] < eccentricities[centerNode]:
            centerNode = i

    return centerNode
