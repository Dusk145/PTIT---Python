if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    mini, idx = 1000000000, 0
    for i in range(n):
        S = 0
        for j in range(n):
            S += abs(a[j] - a[i])
        if S < mini:
            mini = S
            idx = i
    print (mini, a[idx])