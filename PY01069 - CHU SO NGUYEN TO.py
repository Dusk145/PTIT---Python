def check():
    if len(set(b)) != 4 or b[len(b) - 1] == 2:
        return False
    return True

def res(k):
    for j in range(4):
        b.append(a[j])
        if len(b) == k:
            if check():
                print ("".join(map(str, b)))
        else:
            res(k)
        b.pop()

if __name__ == "__main__":
    n = int(input())
    a = [2, 3, 5, 7]
    b = []
    for i in range(4, n + 1):
        res(i)