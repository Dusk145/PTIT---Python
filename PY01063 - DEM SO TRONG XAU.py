if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        s = input()
        idx = cnt = 0
        while idx < len(n):
            idx = n.find(s, idx)
            if idx == - 1:
                break
            else:
                cnt += 1
                idx += len(s)
        print (cnt)