import math

class SinhVien:
    cnt = 1
    def __init__(self, Name, Score) -> None:
        self.code = f"SV{SinhVien.cnt:02d}"
        self.name = Name
        self.score = Score
        SinhVien.cnt += 1
    def res(self):
        print (f"{self.code} {self.name} {(math.ceil(self.score * 100) / 100):.2f}", end = " ")

def change(Name):
    temp = ""
    for i in Name.split():
        temp += i[0].upper()
        temp += (i[1::] + " ")
    return temp.strip()

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Name = change(input().strip().lower())
        x = float(input())
        y = float(input())
        z = float(input())
        Score = (x * 3 + y * 3 + z * 2) / 8
        a.append(SinhVien(Name, Score))
    a.sort(key = lambda x: (-x.score, x.code))
    temp = 1
    for i in range(len(a)):
        a[i].res()
        if i > 0 and a[i - 1].score > a[i].score:
            temp = i + 1
        print (temp)