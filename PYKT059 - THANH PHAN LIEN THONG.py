def dfs(i, ok):
    ok[i] = True
    for j in a[i]:
        if not ok[j]:
            dfs(j, ok)

if __name__ == "__main__":
    n, m, x = map(int, input().split())
    a = []
    for i in range(n + 1):
        a.append([])
    for _ in range(m):
        i, j = map(int, input().split())
        a[i].append(j)
        a[j].append(i)
    ok = [False] * (n + 1)
    dfs(x, ok)
    flag = False
    for i in range(1, n + 1):
        if not ok[i]:
            print (i)
            flag = True
    if not flag:
        print ("0")