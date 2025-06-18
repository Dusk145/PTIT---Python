if __name__ == "__main__":
    a = open("CONTACT.in", "r")
    b = set()
    for i in a:
        b.add(i.strip().lower())
    print ("\n".join(sorted(b)))