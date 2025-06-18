class NhanVien:
    cnt = 1
    def __init__(self, Name, Score):
        self.code = "TS0" + str(NhanVien.cnt)
        self.name = Name
        self.score = Score
        NhanVien.cnt += 1
    def res(self):
        temp = ""
        if self.score > 9.5:
            temp = "XUAT SAC"
        elif self.score >= 8:
            temp = "DAT"
        elif self.score >= 5:
            temp = "CAN NHAC"
        else:
            temp = "TRUOT"
        print (f"{self.code} {self.name} {self.score:.2f} {temp}")

def change(n):
    n = float(n)
    if n <= 10:
        return n
    return n / 10

if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        s = input()
        x = change(input())
        y = change(input())
        a.append(NhanVien(s, round((x + y) / 2, 2)))
    a.sort(key = lambda x: (-x.score, x.code))
    for i in a:
        i.res()