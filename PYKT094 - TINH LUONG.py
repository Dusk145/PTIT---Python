class NhanVien:
    def __init__(self, Code, Name, Room, Money) -> None:
        self.code = Code
        self.name = Name
        self.room = Room
        self.money = Money
    def res(self):
        print (f"{self.code} {self.name} {self.room} {self.money}")

def count(a, b):
    if a == "A":
        if b >= 16:
            return 20
        elif b >= 9:
            return 14
        elif b >= 4:
            return 12
        return 10
    elif a == "B":
        if b >= 16:
            return 16
        elif b >= 9:
            return 13
        elif b >= 4:
            return 11
        return 10
    elif a == "C":
        if b >= 16:
            return 14
        elif b >= 9:
            return 12
        elif b >= 4:
            return 10
        return 9
    else:
        if b >= 16:
            return 13
        elif b >= 9:
            return 11
        elif b >= 4:
            return 9
        return 8

if __name__ == "__main__":
    n = int(input())
    a = {}
    for i in range(n):
        s = input()
        a[s[0:2]] = s[3::]
    m = int(input())
    b = []
    for i in range(m):
        Code = input()
        Name = input()
        Pay = int(input())
        Day = int(input())
        Room = a[Code[3::]]
        Money = Pay * Day * count(Code[0], int(Code[1:3])) * 1000
        b.append(NhanVien(Code, Name, Room, Money))
    for i in b:
        i.res()