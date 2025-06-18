from datetime import datetime

class LichThi:
    cnt = 1
    def __init__(self, Subject_Code, Subject, Date, Time, Group) -> None:
        self.code = f"T{LichThi.cnt:03d}"
        self.subject_code = Subject_Code
        self.subject = Subject
        self.date = Date
        self.time = Time
        self.group = Group
        LichThi.cnt += 1
    def res(self):
        print (f"{self.code} {self.subject_code} {self.subject} {self.date} {self.time} {self.group}")

if __name__ == "__main__":
    format_time = "%H:%M"
    format_date = "%d/%m/%Y"
    n, m = map(int, input().split())
    a = {}
    for i in range(n):
        x = input()
        y = input()
        a[x] = y
    b = []
    for i in range(m):
        Subject_Code, Date, Time, Group = input().split()
        b.append(LichThi(Subject_Code, a[Subject_Code], Date, Time, Group))
    b.sort(key = lambda x: (datetime.strptime(x.date, format_date), datetime.strptime(x.time, format_time)))
    for i in b:
        i.res()