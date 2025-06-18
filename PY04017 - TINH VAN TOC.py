from datetime import datetime

class Human:
    def __init__(self, Code, Name, Place, Speed) -> None:
        self.code = Code
        self.name = Name
        self.place = Place
        self.speed = Speed
    def res(self):
        print (f"{self.code} {self.name} {self.place} {round(self.speed, 0):.0f} Km/h")

def change(Name, Place):
    temp = ""
    for i in Place.split():
        temp += i[0]
    for i in Name.split():
        temp += i[0]
    return temp

if __name__ == "__main__":
    format_time = "%H:%M"
    Start = datetime.strptime("6:00", format_time)
    t = int(input())
    a = []
    for _ in range(t):
        Name = input().strip()
        Place = input().strip()
        End = datetime.strptime(input(), format_time)
        Time = (End - Start).total_seconds() / 3600
        Code = change(Name, Place)
        Speed = 120 / Time
        a.append(Human(Code, Name, Place, Speed))
    a.sort(key = lambda x: -x.speed)
    for i in a:
        i.res()