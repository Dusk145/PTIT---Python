class GiaoVien:
    cnt = 1
    def __init__(self, Name, Subject, Score) -> None:
        self.code = f"GV{GiaoVien.cnt:02d}"
        self.name = Name
        self.subject = Subject
        self.score = Score
        GiaoVien.cnt += 1
    def res(self):
        print (f"{self.code} {self.name} {self.subject} {round(self.score, 1):.1f}", end = " ")
        if self.score >= 18:
            print ("TRUNG TUYEN")
        else:
            print ("LOAI")

def subj(c):
    if c == "A":
        return "TOAN"
    elif c == "B":
        return "LY"
    else:
        return "HOA"
    
def count(n):
    if n == "1":
        return 2
    elif n == "2":
        return 1.5
    elif n == "3":
        return 1
    else:
        return 0

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Name = input()
        temp = input()
        Subject = subj(temp[0])
        x = float(input())
        y = float(input())
        Score = x * 2 + y + count(temp[1])
        a.append(GiaoVien(Name, Subject, Score))
    a.sort(key = lambda x: (-x.score, x.code))
    for i in a:
        i.res()