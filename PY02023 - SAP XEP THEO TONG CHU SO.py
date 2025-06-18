def sum_digit(n):
    return sum(list(map(int, n)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        a.sort(key = lambda x: (sum_digit(x), int(x)))
        print (*a)