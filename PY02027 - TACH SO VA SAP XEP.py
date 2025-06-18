if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        s = input()
        idx, temp = 0, ""
        while idx < len(s):
            if s[idx].isdigit():
                temp += s[idx]
            else:
                if temp != "":
                    a.append(int(temp))
                    temp = ""
            idx += 1
        if temp != "":
            a.append(int(temp))
    print ("\n".join(map(str, sorted(a))))