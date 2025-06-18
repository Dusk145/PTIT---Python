from datetime import date

class KhachHang:
    cnt = 1
    def __init__(self, Name, Room, Time, Cost) -> None:
        if KhachHang.cnt < 10:
            self.code = "KH0" + str(KhachHang.cnt)
        else:
            self.code = "KH" + str(KhachHang.cnt)
        self.name = Name
        self.room = Room
        self.time = Time
        self.cost = Cost
        KhachHang.cnt += 1
    def res(self):
        print (f"{self.code} {self.name} {self.room} {self.time} {self.cost}")
    
def count(n, Room):
    if Room[0] == "1":
        return 25 * n
    elif Room[0] == "2":
        return 34 * n
    elif Room[0] == "3":
        return 50 * n
    else:
        return 80 * n

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Name = input().strip()
        Room = input().strip()
        Start = list(map(int, input().split("/")))
        End = list(map(int, input().split("/")))
        temp = int(input())
        Time = (date(End[2], End[1], End[0]) - date(Start[2], Start[1], Start[0])).days + 1
        Cost = count(Time, Room) + temp
        a.append(KhachHang(Name, Room, Time, Cost))
    a.sort(key = lambda x: (-x.cost, x.code))
    for i in a:
        i.res()