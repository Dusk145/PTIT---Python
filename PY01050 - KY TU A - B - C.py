def res(i):
    for j in range(3):
        b.append(a[j])
        cnt[j] += 1
        if len(b) == i:
            if cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0 and cnt[0] <= cnt[1] and cnt[1] <= cnt[2]:
                for k in b:
                    print (k, end = "")
                print ()
        else:
            res(i)
        b.pop()
        cnt[j] -= 1

if __name__ == "__main__":
    n = int(input())
    a = ["A", "B", "C"]
    b = []
    cnt = [0] * 3
    for i in range(3, n + 1):
        res(i)