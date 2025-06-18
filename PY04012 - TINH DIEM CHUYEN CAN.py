class SinhVien:
    def __init__(self, Code, Room, Name, Score) -> None:
        self.code = Code
        self.room = Room
        self.name = Name
        self.score = Score
    def res(self):
        print (f"{self.code} {self.name} {self.room} {self.score}", end = " ")
        if self.score == 0:
            print ("KDDK")
        else:
            print ()

if __name__ == "__main__":
    t = int(input())
    a = {}
    for _ in range(t):
        Code = input()
        Name = input()
        Room = input()
        a[Code] = SinhVien(Code, Room, Name, 10)
    for _ in range(t):
        s = input().split()
        for i in s[1]:
            if i == "m":
                a[s[0]].score -= 1
            elif i == "v":
                a[s[0]].score -= 2
            if a[s[0]].score < 0:
                a[s[0]].score = 0
    for i in a:
        a[i].res()