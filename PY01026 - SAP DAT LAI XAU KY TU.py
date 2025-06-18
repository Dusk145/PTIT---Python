if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        print ("Test " + str(_ + 1) + ": ", end = "")
        if "".join(sorted(a)) == "".join(sorted(b)):
            print ("YES")
        else:
            print ("NO")