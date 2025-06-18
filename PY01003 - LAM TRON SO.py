if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if int(n) <= 10:
            print (n)
            continue
        temp = ''.join(reversed(n))
        a = list(temp)
        cnt = 0
        for i in range(len(a) - 1):
            x = int(a[i]) + cnt
            if x >= 5:
                cnt = 1
            else:
                cnt = 0
            a[i] = '0'
        if cnt == 1:
            a[len(a) - 1] = str(int(a[len(a) - 1]) + cnt)
        print (''.join(a[::-1]))