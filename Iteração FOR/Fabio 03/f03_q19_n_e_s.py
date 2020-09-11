def main():
    n = int(input("Digite um número: "))

    if n < 1:
        print("Erro. Digite um número positivo.")
    else:
        s = 0
        for i in range(0, n):
            if i%2 == 0:
                s += (i+1)/(n-i)
            else:
                s -= (n-i)/(i+1)

    print("S = {}".format(s))


main()
