if __name__ == "__main__":
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().split())))
    even, odd = [], []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort(key = lambda x: x)
    odd.sort(key = lambda x : -x)
    idx1, idx2 = 0, 0
    for i in a:
        if i % 2 == 0:
            print (even[idx1], end = " ")
            idx1 += 1
        else:
            print (odd[idx2], end = " ")
            idx2 += 1