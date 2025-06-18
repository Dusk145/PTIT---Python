class HoaDon:
    cnt = 1
    def __init__(self, Name, Money):
        if HoaDon.cnt < 10:
            self.code = "KH0" + str(HoaDon.cnt)
        else:
            self.code = "KH" + str(HoaDon.cnt)
        self.name = Name
        self.money = Money
        HoaDon.cnt += 1
    def res(self):
        print (f"{self.code} {self.name} {self.money:.0f}")

def cost(n):
    if n <= 50:
        return n * 102
    elif n <= 100:
        return round(n * 150 * 1.03 - 2575)
    else:
        return round(n * 210 - 7875)

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        s = input()
        x = float(input())
        y = float(input())
        a.append(HoaDon(s, cost(y - x)))
    a.sort(key = lambda x: (-x.money, x.code))
    for i in a:
        i.res()