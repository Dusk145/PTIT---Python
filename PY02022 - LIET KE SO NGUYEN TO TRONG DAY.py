import math

def nt():
    ok[0] = ok[1] = False
    for i in range(2, int(math.sqrt(1000000))):
        if ok[i]:
            for j in range(i * i, 1000000, i):
                ok[j] = False

if __name__ == "__main__":
    ok = [True] * 1000000
    nt()
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 1000000
    for i in a:
        cnt[i] += 1
    for i in a:
        if cnt[i] > 0 and ok[i]:
            print (i, cnt[i])
            cnt[i] = 0