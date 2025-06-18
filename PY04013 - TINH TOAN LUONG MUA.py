from datetime import datetime

class Precipitation:
    cnt = 1
    def __init__(self, Name, Value, Time):
        if Precipitation.cnt < 10:
            self.code = "T0" + str(Precipitation.cnt)
        else:
            self.code = "T" + str(Precipitation.cnt)
        self.name = Name
        self.value = Value
        self.time = Time
        Precipitation.cnt += 1
    def res(self):
        tb = (self.value * 60) / self.time
        print (f"{self.code} {self.name} {tb:.2f}")

if __name__ == "__main__":
    format_time = "%H:%M"
    t = int(input())
    a = {}
    for _ in range(t):
        x = input()
        start_time = input()
        end_time = input()
        y = float(input())
        start = datetime.strptime(start_time, format_time)
        end = datetime.strptime(end_time, format_time)
        delta = end - start
        if x in a:
            a[x].value += y
            a[x].time += (delta.total_seconds() / 60)
        else:
            a[x] = Precipitation(x, y, delta.total_seconds() / 60)
    for i in a:
        a[i].res()