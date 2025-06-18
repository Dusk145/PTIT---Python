if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted(map(int, input().split()))
        cnt = 0
        for i in range(len(a) - 1):
            temp = a[i]
            while temp + 1 < a[i + 1]:
                cnt += 1
                temp += 1
        print (cnt)