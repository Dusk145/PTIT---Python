import math

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x, m = map(float, input().split()) 
        # n(1 + x/100) ^ a = m
        print (math.ceil(math.log(m / n) / math.log(1 + x / 100)))