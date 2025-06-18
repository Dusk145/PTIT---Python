class KhachHang:
    cnt = 1
    def __init__(self, Name, Cost1, Cost2, Cost3, Total) -> None:
        self.code = f"KH{KhachHang.cnt:02d}"
        self.name = Name
        self.cost1 = Cost1
        self.cost2 = Cost2
        self.cost3 = Cost3
        self.total = Total
        KhachHang.cnt += 1
    def res(self):
        print (f"{self.code} {self.name} {self.cost1:.0f} {self.cost2:.0f} {self.cost3:.0f} {self.total:.0f}")

def change(Name):
    temp = ""
    for i in Name.split():
        temp += (i[0].upper() + i[1::] + " ")
    return temp.strip()

def count1(c, n):
    if c == "A":
        if n < 100:
            return n * 450
        else:
            return 45000
    elif c == "B":
        if n < 500:
            return n * 450
        else:
            return 500 * 450
    else:
        if n < 200:
            return n * 450
        else:
            return 200 * 450
        
def count2(c, n):
    if c == "A":
        if n > 100:
            return (n - 100) * 1000
    elif c == "B":
        if n > 500:
            return (n - 500) * 1000
    else:
        if n > 200:
            return (n - 200) * 1000
    return 0

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Name = change(input().strip().lower())
        c, x, y = input().split()
        temp = int(y) - int(x)
        Cost1 = count1(c, temp)
        Cost2 = count2(c, temp)
        Cost3 = Cost2 * 0.05
        Total = Cost1 + Cost2 + Cost3
        a.append(KhachHang(Name, Cost1, Cost2, Cost3, Total))
    a.sort(key = lambda x: -x.total)
    for i in a:
        i.res()