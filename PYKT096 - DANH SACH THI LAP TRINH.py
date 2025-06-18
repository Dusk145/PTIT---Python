class ThiSinh:
    cnt = 1
    def __init__(self, Name, Team, School):
        self.code = f"C{ThiSinh.cnt:03d}"
        self.name = Name
        self.team = Team
        self.school = School
        ThiSinh.cnt += 1
    def res(self):
        print (f"{self.code} {self.name} {self.team} {self.school}")

if __name__ == "__main__":
    n = int(input())
    a = {}
    for i in range(n):
        Code = input()
        School = input()
        a[Code] = School
    m = int(input())
    b = list(a.keys())
    c = []
    for i in range(m):
        Name = input()
        temp = input()
        Team = b[int(temp[4::]) - 1]
        School = a[Team]
        c.append(ThiSinh(Name, Team, School))
    c.sort(key = lambda x: x.name)
    for i in c:
        i.res()