class ThiSinh:
    cnt = 1
    def __init__(self, Name, Score) -> None:
        self.code = f"TS{ThiSinh.cnt:02d}"
        self.name = Name
        self.score = Score
        ThiSinh.cnt += 1
    def res(self):
        print (f"{self.code} {self.name} {self.score}", end = " ")
        if self.score >= 20.5:
            print ("Do")
        else:
            print ("Truot")

def change(Name):
    temp = ""
    for i in Name.split():
        temp += i[0].upper()
        temp += (i[1::] + " ")
    return temp.strip()

def nation(Nation):
    if Nation == "Kinh":
        return 0
    return 1.5

def count(Nation, Priority):
    temp = 0
    if Priority == 1:
        temp = 1.5
    elif Priority == 2:
        temp = 1
    return nation(Nation) + temp

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Name = change(input().strip().lower())
        Score = float(input())
        Nation = input()
        Priority = int(input())
        a.append(ThiSinh(Name, Score + count(Nation, Priority)))
    a.sort(key = lambda x: (-x.score, x.code))
    for i in a:
        i.res()