if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        res = ""
        if (m == 3 and n >= 21) or (m == 4 and n <= 19):
            res = "Bach Duong"
        elif (m == 4 and n >= 20) or (m == 5 and n <= 20):
            res = "Kim Nguu"
        elif (m == 5 and n >= 21) or (m == 6 and n <= 20):
            res = "Song Tu"
        elif (m == 6 and n >= 21) or (m == 7 and n <= 22):
            res = "Cu Giai"
        elif (m == 7 and n >= 23) or (m == 8 and n <= 22):
            res = "Su Tu"
        elif (m == 8 and n >= 23) or (m == 9 and n <= 22):
            res = "Xu Nu"
        elif (m == 9 and n >= 23) or (m == 10 and n <= 22):
            res = "Thien Binh"
        elif (m == 10 and n >= 23) or (m == 11 and n <= 22):
            res = "Thien Yet"
        elif (m == 11 and n >= 23) or (m == 12 and n <= 21):
            res = "Nhan Ma"
        elif (m == 12 and n >= 22) or (m == 1 and n <= 19):
            res = "Ma Ket"
        elif (m == 1 and n >= 20) or (m == 2 and n <= 18):
            res = "Bao Binh"
        else:
            res = "Song Ngu"
        print (res)