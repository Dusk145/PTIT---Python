if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        idx = 0
        res = 0
        while idx < len(s):
            temp = ""
            while idx < len(s) and s[idx].isdigit():
                temp += s[idx]
                idx += 1
            if temp == "":
                idx += 1
            else:
                res = max(res, int(temp))
        print (res)