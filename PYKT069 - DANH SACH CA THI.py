from datetime import datetime

class Exam:
    cnt = 1
    def __init__(self, Date, Time, Room) -> None:
        self.code = f"C{Exam.cnt:03d}"
        self.date = Date
        self.time = Time
        self.room = Room
        Exam.cnt += 1
    def res(self):
        print (self.code, self.date, self.time, self.room)
    
if __name__ == "__main__":
    format_time = "%H:%M"
    format_date = "%d/%m/%Y"
    a = []
    with open("CATHI.in","r") as f:
        t = int(f.readline())
        for _ in range(t):
            Date = f.readline().strip()
            Time = f.readline().strip()
            Room = f.readline().strip()
            a.append(Exam(Date, Time, Room))
    a.sort(key = lambda x: (datetime.strptime(x.date, format_date), datetime.strptime(x.time, format_time), x.code))
    for i in a:
        i.res()