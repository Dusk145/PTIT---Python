def sum_str(s):
    S = 0
    for i in s:
        S += (ord(i) - ord("A"))
    return S

def change(x, n):
    temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n += (ord(x) - ord("A"))
    return temp[n % 26]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        a = s[: (len(s) // 2)]
        b = s[(len(s) // 2):]
        S_a = sum_str(a)
        S_b = sum_str(b)
        A = B = ""
        for i in range(len(a)):
            A += change(a[i], S_a)
            B += change(b[i], S_b)
        for i in range(len(a)):
            print (change(A[i], ord(B[i]) - ord("A")), end = "")
        print ()