import sys
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7

def get_ans(M, Parent):
    N = M + 1
    tree = [[] for _ in range(N + 1)]  # 1-based indexing

    # Build the tree
    for i in range(M):
        tree[Parent[i]].append(i + 2)

    # Step 1: Compute beauty for each node
    beauty = [0] * (N + 1)

    def dfs_beauty(u):
        depths = []
        for v in tree[u]:
            d = dfs_beauty(v)
            depths.append(d)
        if not depths:
            beauty[u] = 1
            return 1
        depths.sort(reverse=True)
        d1 = depths[0]
        d2 = depths[1] if len(depths) > 1 else 0
        beauty[u] = d1 + d2 + 1
        return d1 + 1

    dfs_beauty(1)

    # Step 2: Track in-time and out-time for ancestor check
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    time = [1]

    def dfs_time(u):
        in_time[u] = time[0]
        time[0] += 1
        for v in tree[u]:
            dfs_time(v)
        out_time[u] = time[0]
        time[0] += 1

    dfs_time(1)

    def is_ancestor(u, v):
        return in_time[u] < in_time[v] and out_time[v] < out_time[u]

    # Step 3: Count all valid good sets using DFS
    ans = 0

    def dfs_count(u):
        nonlocal ans
        # Single node set is always valid
        ans += 1

        # Explore child nodes and check ancestor-descendant condition
        for v in tree[u]:
            dfs_count(v)
            if is_ancestor(u, v) and beauty[u] > beauty[v]:
                ans += 1
            elif is_ancestor(v, u) and beauty[v] > beauty[u]:
                ans += 1

    dfs_count(1)
    return ans % MOD

# Do not modify this part
def main():
    M = int(sys.stdin.readline().strip())
    Parent = []
    for _ in range(M):
        Parent.append(int(sys.stdin.readline().strip()))

    result = get_ans(M, Parent)
    print(result)

if __name__ == "__main__":
    main()
