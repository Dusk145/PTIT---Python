class Subject:
    def __init__(self, Code, Name, Type) -> None:
        self.code = Code
        self.name = Name
        self.type = Type
    def res(self):
        print (self.code, self.name, self.type)

if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        Code = input()
        Name = input()
        Type = input()
        a.append(Subject(Code, Name, Type))
    a.sort(key = lambda x: x.code)
    for i in a:
        i.res()