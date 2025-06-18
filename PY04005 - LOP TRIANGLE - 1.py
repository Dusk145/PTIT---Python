import math

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

if __name__ == "__main__":
    t = int(input())
    n = []
    while len(n) < t * 6:
        for i in input().split():
            n.append(float(i))
    idx = 0
    for i in range(t):
        x = distance([n[idx], n[idx + 1]], [n[idx + 2], n[idx + 3]])
        y = distance([n[idx + 2], n[idx + 3]], [n[idx + 4], n[idx + 5]])
        z = distance([n[idx + 4], n[idx + 5]], [n[idx], n[idx + 1]])
        if max(x, y, z) * 2 >= x + y + z:
            print ("INVALID")
        else:
            print (f"{round(x + y + z, 3):.3f}")
        idx += 6