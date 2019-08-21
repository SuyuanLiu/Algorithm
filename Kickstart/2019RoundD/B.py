def helper(G, n, m):
    colsu = [[[] for i in range(m+1)] for j in range(n)] 
    for i in range(len(G)):
        hi, s = G[i]
        colsu[hi-1][0].append(i)

    for i in range(m):
        for j in range(len(G)):
            hi, s = G[j]
            if s == 'C':
                colsu[(hi+i)%n][i+1].append(j)
            else:
                
                idx = n - (abs(hi-i-2))%(n-1) if (hi-i-1) < 0 else hi-i-2
                colsu[idx][i+1].append(j)
    
    res = [0 for i in range(len(G))]
    for i in range(n):
        tmp = colsu[i]
        for j in range(m, -1, -1):
            if not tmp[j]:
                continue
            else:
                for n in tmp[j]:
                    res[n] += 1
                break
    return res


def main():
    t = int(input())
    for i in range(1, t + 1):
        res = []
        n, g, m = [int(s) for s in input().split(' ')]
        G = []
        for j in range(g):
            [hi, s] = [n for n in input().split(' ')]
            hi = int(hi)
            G.append([hi, s])
        res = helper(G, n, m)

        print("Case #{}: {}".format(i, ' '.join(str(c) for c in res)))

if __name__ == '__main__':
    main()
