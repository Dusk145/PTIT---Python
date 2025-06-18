from datetime import datetime

class Exam:
    def __init__(self, Code, Date, Time, ID, Subject, Group, Number) -> None:
        self.code = Code
        self.date = Date
        self.time = Time
        self.id = ID
        self.subject = Subject
        self.group = Group
        self.number = Number
    def res(self):
        print (self.date, self.time, self.id, self.subject, self.group, self.number)

if __name__ == "__main__":
    a = {}
    with open("MONTHI.in", "r") as f:
        t = int(f.readline())
        for _ in range(t):
            Code = f.readline().strip()
            Name = f.readline().strip()
            Type = f.readline().strip()
            a[Code] = Name
    b = {}
    with open("CATHI.in", "r") as f:
        t = int(f.readline())
        for _ in range(t):
            Date = f.readline().strip()
            Time = f.readline().strip()
            ID = f.readline().strip()
            b[f"C{(_ + 1):03d}"] = f"{Date} {Time} {ID}"
    c = []
    with open("LICHTHI.in", "r") as f:
        t = int(f.readline())
        for _ in range(t):
            Code1, Code2, Group, Number = f.readline().strip().split()
            Date, Time, ID = b[Code1].split()
            Subject = a[Code2]
            c.append(Exam(Code1, Date, Time, ID, Subject, Group, Number))
    format_time = "%H:%M"
    format_date = "%d/%m/%Y"
    c.sort(key = lambda x: (datetime.strptime(x.date, format_date), datetime.strptime(x.time, format_time), x.code))
    for i in c:
        i.res()