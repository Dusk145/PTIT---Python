import math

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def res(a, b, c):
    temp = math.sqrt((a + b + c) * (-c + a + b) * (b + c - a) * (c + a - b))
    return temp * 0.25

if __name__ == "__main__":
    t = int(input())
    n = []
    while len(n) < 6 * t:
        for i in input().split():
            n.append(float(i))
    idx = 0
    for i in range(t):
        a, b, c, d, e, f = n[idx: idx + 6]
        x = distance([a, b], [c, d])
        y = distance([c, d], [e, f])
        z = distance([e, f], [a, b])
        if max(x, y, z) * 2 >= x + y + z:
            print ("INVALID")
        else:
            print (f"{round(res(x, y, z), 2):.2f}")
        idx += 6