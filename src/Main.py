import FloydWarshall as fw

N = 9999

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
    pass

main()