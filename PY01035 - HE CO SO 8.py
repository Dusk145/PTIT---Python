if __name__ == "__main__":
    s = input()
    while len(s) % 3 != 0:
        s = "0" + s
    for i in range(0, len(s), 3):
        temp = int(s[i]) * (2 ** 2) + int(s[i + 1]) * (2 ** 1) + int(s[i + 2]) * (2 ** 0)
        print (temp, end = "")