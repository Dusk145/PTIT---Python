import re

if __name__ == "__main__":
    t = int(input())
    a = {}
    for _ in range(t):
        s = input().lower()
        for i in re.split("[^a-z0-9]", s):
            if i != "":
                a[i] = a.get(i, 0) + 1
    temp = sorted(a, key = lambda x: (-a[x], x))
    for i in temp:
        print (i, a[i])