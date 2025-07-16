import sys
import math
sys.setrecursionlimit(10000)

def lilly_berry(N, D, K, A, T):
    max_berries = 0

    for start in range(N):
        time_used = 0
        berries = 0
        partial_used = 0

        for i in range(start, N):
            if time_used + T[i] <= K:
                time_used += T[i]
                berries += A[i]
            elif partial_used < D:
                half_time = (T[i] + 1) // 2
                if time_used + half_time <= K:
                    time_used += half_time
                    berries += A[i]
                    partial_used += 1
                else:
                    break
            else:
                break

        max_berries = max(max_berries, berries)

    return max_berries

def main():
    N = int(sys.stdin.readline().strip())
    D = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())

    A = []
    for _ in range(N):
        A.append(int(sys.stdin.readline().strip()))

    T = []
    for _ in range(N):
        T.append(int(sys.stdin.readline().strip()))

    result = lilly_berry(N, D, K, A, T)
    print(result)

if __name__ == "__main__":
    main()
