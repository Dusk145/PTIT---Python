import math

class PhanSo:
    def __init__(self, a, b) -> None:
        self.x = a
        self.y = b
    def res(self):
        temp = math.gcd(self.x, self.y)
        self.x //= temp
        self.y //= temp
        return f"{self.x}/{self.y}"

if __name__ == "__main__":
    a, b = map(int, input().split())
    c = PhanSo(a, b)
    print (c.res())