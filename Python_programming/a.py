import sys
from itertools import product

sys.setrecursionlimit(10000)

def max_value(N, K, V):
    max_total = 0
    found = False

    def is_valid(selection):
        used = set(selection)
        if len(used) < K:
            return False
        for i in range(N):
            if selection[i] == selection[(i + 1) % N]:
                return False
        return True

    for selection in product(range(K), repeat=N):
        if is_valid(selection):
            total = sum(V[i][selection[i]] for i in range(N))
            max_total = max(max_total, total)
            found = True

    return max_total if found else 0

def main():
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    V = []
    for _ in range(N):
        V.append(list(map(int, sys.stdin.readline().strip().split())))
    result = max_value(N, K, V)
    print(result)

if __name__ == "__main__":
    main()
