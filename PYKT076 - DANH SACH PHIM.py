from datetime import datetime

class Movie:
    cnt = 1
    def __init__(self, Genre, Day, Name, Episode):
        self.code = f"P{Movie.cnt:03d}"
        self.genre = Genre
        self.day = Day
        self.name = Name
        self.episode = Episode
        Movie.cnt += 1
    def res(self):
        print (f"{self.code} {self.genre} {self.day} {self.name} {self.episode}")

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input())
    b = []
    for i in range(m):
        temp = input()
        Genre = a[int(temp[3::]) - 1]
        Day = input()
        Name = input()
        Episode = int(input())
        b.append(Movie(Genre, Day, Name, Episode))
    b.sort(key = lambda x: (datetime.strptime(x.day, "%d/%m/%Y"), x.name, -x.episode))
    for i in b:
        i.res()