if __name__ == "__main__":
    a = list(input())
    cnt4 = cnt7 = 0
    for i in range(len(a)):
        if a[i] == '4':
            cnt4 += 1
        elif a[i] == '7':
            cnt7 += 1
    if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7:
        print ("YES")
    else:
        print ("NO")