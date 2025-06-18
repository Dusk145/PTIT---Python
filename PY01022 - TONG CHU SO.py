def sum_digit(n):
    S = 0
    for i in n:
        S += (ord(i) - 48)
    return S

if __name__ == "__main__":
    n = input()
    cnt = 0 
    if len(n) <= 1:
        cnt += 1
    else:
        while len(n) > 1:
            n = str(sum_digit(n))
            cnt += 1
    print (cnt)