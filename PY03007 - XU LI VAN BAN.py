import re

if __name__ == "__main__":
    s = ""
    while True:
        try:
            s += input()
        except: 
            break
    temp = re.split("[?.!]", s)
    for i in temp:
        if len(i) != 0:
            i = i.lower().split()
            i[0] = i[0][0].upper() + i[0][1:]
            print (" ".join(i))