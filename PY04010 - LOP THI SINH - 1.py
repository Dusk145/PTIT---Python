if __name__ == "__main__":
    Name = input()
    Birth = input()
    S = 0
    for i in range(3):
        S += float(input())
    print (f"{Name} {Birth} {S:.1f}")