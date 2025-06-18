from datetime import datetime

class Gamer:
    def __init__(self, Code, Name, Time) -> None:
        self.code = Code
        self.name = Name
        self.time = Time
    def res(self):
        hour = self.time // 3600
        minute = (self.time - 3600 * hour) // 60
        print (f"{self.code} {self.name} {hour:.0f} gio {minute:.0f} phut")

if __name__ == "__main__":
    format_time = "%H:%M"
    t = int(input())
    a = []
    for i in range(t):
        Code = input()
        Name = input()
        Start = datetime.strptime(input(), format_time)
        End = datetime.strptime(input(), format_time)
        Time = End - Start
        a.append(Gamer(Code, Name, Time.total_seconds()))
    a.sort(key = lambda x: (-x.time, x.code))
    for i in a:
        i.res()