class HoaDon:
    def __init__(self, Code, Name, Count, Cost, Reduce, Total) -> None:
        self.code = Code
        self.name = Name
        self.count = Count
        self.cost = Cost
        self.reduce = Reduce
        self.total = self.count * self.cost - self.reduce
    def res(self):
        print (f"{self.code} {self.name} {self.count} {self.cost} {self.reduce} {self.total}")

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Code = input()
        Name = input()
        Count = int(input())
        Cost = int(input())
        Reduce = int(input())
        a.append(HoaDon(Code, Name, Count, Cost, Reduce, 0))
    a.sort(key = lambda x: -x.total)
    for i in a:
        i.res()