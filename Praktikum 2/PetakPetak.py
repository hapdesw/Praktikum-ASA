N, M = map(int, input().split())

def brute_force_maximize_neighbors(N, M):
    petak = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 != 0:
                petak[i][j] = 1
            else:
                petak[i][j] = 0
    petak2 = '\n'.join([' '.join(map(str, N)) for N in petak])
    return petak2

print(brute_force_maximize_neighbors(N, M))