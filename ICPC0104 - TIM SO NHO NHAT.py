if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        idx = 0
        res = 1e18
        while idx < len(s):
            temp = ""
            while idx < len(s) and s[idx].isdigit():
                temp += s[idx]
                idx += 1
            if temp != "":
                res = min(res, int(temp))
            else:
                idx += 1
        print (res)