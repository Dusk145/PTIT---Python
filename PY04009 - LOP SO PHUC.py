def res(z):
    if z.imag < 0:
        temp = "-"
    else:
        temp = "+"
    return f"{z.real:.0f} {temp} {abs(z.imag):.0f}i"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        A, B = complex(a, b), complex(c, d)
        C, D = (A + B) * A, (A + B) ** 2
        print (f"{res(C)}, {res(D)}")