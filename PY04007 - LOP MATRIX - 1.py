if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = []
        for i in range(n):
            a.append(input().split())
        for i in range(n):
            for j in range(m):
                temp = 0
                for k in range(n):
                    temp += int(a[i][k]) * int(a[j][k])
                print (temp, end = " ")
            print ()