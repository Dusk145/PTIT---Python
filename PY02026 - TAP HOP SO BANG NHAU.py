if __name__ == "__main__":
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    if sorted(a) == sorted(b):
        print ("YES")
    else:
        print ("NO")