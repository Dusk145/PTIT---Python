if __name__ == "__main__":
    n = input()
    temp = ''.join(reversed(n))
    res = ""
    cnt = 0
    for i in range(len(n)):
        cnt += 1
        res += temp[i]
        if cnt % 3 == 0 and i != len(n) - 1:
            res += ","
    print (''.join(reversed(res)))