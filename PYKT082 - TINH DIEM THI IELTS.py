def score(n):
    if n >= 39: return 9.0
    if n >= 37: return 8.5
    if n >= 35: return 8.0
    if n >= 33: return 7.5
    if n >= 30: return 7.0
    if n >= 27: return 6.5
    if n >= 23: return 6.0
    if n >= 20: return 5.5
    if n >= 16: return 5.0
    if n >= 13: return 4.5
    if n >= 10: return 4.0
    if n >= 7: return 3.5
    if n >= 5: return 3.0
    if n >= 3: return 2.5 



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c, d = input().split()
        a = score(int(a))
        b = score(int(b))
        S = (a + b + float(c) + float(d)) / 4
        res = S - int(S)
        if res < 0.25:
            res = int(S)
        elif res < 0.75:
            res = int(S) + 0.5
        else:
            res = int(S) + 1.0
        print (float(res))