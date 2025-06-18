if __name__ == "__main__":
    n = int(input())
    a = sorted(map(int, input().split()))
    x = a[-1] * a[-2]
    y = a[0] * a[1]
    z = x * a[-3]
    t = y * a[-1]
    print (max(x, y, z, t))