def main():
    n = int(input("Digite um número: "))

    if n < 1:
        print("Erro. Digite um número positivo.")

    else:
        s = 0
        for i in range(1, n+1):
            s += 1/i

    print("S = {}".format(s))


main()
