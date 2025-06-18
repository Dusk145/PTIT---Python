def bin_search(left, right, x):
    while left <= right:
        mid = (right + left) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == "__main__":
    check = {}
    a = []
    for i in range(60):
        for j in range(38):
            for k in range(26):
                temp = (2 ** i) * (3 ** j) * (5 ** k)
                if temp not in check:
                    check[temp] = 1
                    a.append(temp)
    a.sort()
    t = int(input())
    for _ in range(t):
        n = int(input())
        idx = bin_search(0, len(a) - 1, n)
        if idx == -1:
            print ("Not in sequence")
        else:
            print (idx + 1)