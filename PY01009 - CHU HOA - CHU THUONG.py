if __name__ == "__main__":
    s = input()
    cnt1 = cnt2 = 0
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            cnt1 += 1
        elif s[i] >= 'A' and s[i] <= 'Z':
            cnt2 += 1
    if cnt1 >= cnt2:
        print (s.lower())
    else:
        print (s.upper())