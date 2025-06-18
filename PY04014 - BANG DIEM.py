from decimal import Decimal

class Score:
    cnt = 1
    def __init__(self, Name, Avg):
        if Score.cnt < 10:
            self.code = "HS0" + str(Score.cnt)
        else:
            self.code = "HS" + str(Score.cnt)
        self.name = Name
        self.avg = Avg
        Score.cnt += 1
    def res(self):
        temp = ""
        if self.avg >= 9:
            temp = "XUAT SAC"
        elif self.avg >= 8:
            temp = "GIOI"
        elif self.avg >= 7:
            temp = "KHA"
        elif self.avg >= 5:
            temp = "TB"
        else:
            temp = "YEU"
        print (f"{self.code} {self.name} {self.avg:.1f} {temp}")

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        s = input()
        S = 0
        cnt = 0
        for i in input().split():
            if cnt < 2:
                S += Decimal(i) * 2
                cnt += 1
            else:
                S += Decimal(i)
        a.append(Score(s, round(Decimal(S / 10 / Decimal(1.2)), 1)))
    a.sort(key = lambda x: (-x.avg, x.code))
    for i in a:
        i.res()