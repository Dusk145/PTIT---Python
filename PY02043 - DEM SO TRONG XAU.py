if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        s = input()
        idx = cnt = 0
        while idx < len(n):
            temp = n.find(s, idx)
            if temp == -1:
                break
            else:
                cnt += 1
                idx = temp + len(s)
        print (cnt)