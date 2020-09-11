def main():
    n = int(input("Digite um número: "))

    if n < 1:
        print("Erro. Digite um número positivo.")
    else:
        s = 0
        for i in range(0, n):
            s += (i+1)/(n-i)

    print("S = {}".format(s))


main()
