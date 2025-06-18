if __name__ == "__main__":
    word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while True:
        s = input()
        if s[0] == '0':
            break
        n, temp = s.split()
        res = ""
        for i in range(len(temp)):
            for j in range(len(word)):
                if temp[i] == word[j]:
                    res += word[(j + int(n)) % 28]
                    break
        print (''.join(reversed(res)))