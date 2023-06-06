peças = input()
N, M = peças.split()
N, M = int(N), int(M)
def dominos (N,M):
    print ((N*M)//2)
dominos(N,M)    