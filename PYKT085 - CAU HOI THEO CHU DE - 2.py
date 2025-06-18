if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        temp = input().strip()
        a.append(temp)
    cnt = 0
    temp = ""
    for i in range(n):
        if cnt == 0:
            temp = a[i]
        if a[i] == "":
            print (temp + ": " + str(cnt - 1))
            cnt = 0
            continue
        cnt += 1
    if cnt != 0:
        print (temp + ": " + str(cnt - 1))