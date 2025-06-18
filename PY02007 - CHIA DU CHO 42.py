if __name__ == "__main__":
    a = set()
    cnt = 0
    while True:
        s = input()
        for i in s.split():
            a.add(int(i) % 42)
            cnt += 1
        if cnt == 10:
            break
    print (len(a))