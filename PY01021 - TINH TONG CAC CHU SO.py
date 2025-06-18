if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        temp = "".join(sorted(s))
        S = 0
        idx = 0
        for i in range(len(temp)):
            if temp[i] >= "0" and temp[i] <= "9":
                S += int(temp[i])
            else:
                idx = i
                break
        print (temp[idx::] + str(S))