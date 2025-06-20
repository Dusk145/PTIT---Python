from decimal import Decimal

class Point:
    def __init__ (self, a, b) -> None:
        self.x = a
        self.y = b
    def distance(self, a):
        res = ((self.x - a.x) ** 2 + (self.y - a.y) ** 2).sqrt()
        return f"{res:.4f}"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1