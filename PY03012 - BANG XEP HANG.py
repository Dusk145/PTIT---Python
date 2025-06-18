class Student:
    def __init__(self, Name, Score, Count) -> None:
        self.name = Name
        self.score = Score
        self.count = Count
    def res(self):
        print (self.name, self.score, self.count)

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Name = input()
        Score, Count = map(int, input().split())
        a.append(Student(Name, Score, Count))
    a.sort(key = lambda x: (-x.score, x.count, x.name))
    for i in a:
        i.res()