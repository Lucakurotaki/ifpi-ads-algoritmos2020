def main():
    s = 0
    j = 1
    for i in range(0, 50):
        s += j/(i+1)
        j += 2

    print("S = {}".format(s))


main()
