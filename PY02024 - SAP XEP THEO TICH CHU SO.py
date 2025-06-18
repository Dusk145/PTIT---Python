def mul_digit(n):
    S = 1
    for i in n:
        S *= int(i)
    return S

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        a.sort(key = lambda x: (mul_digit(x), int(x)))
        print (*a)