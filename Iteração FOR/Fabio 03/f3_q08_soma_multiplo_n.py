def main():
    n = int(input("Digite um número: "))

    ls = int(input("Digite o valor do limite superior: "))

    li = int(input("Digite o valor do limite inferior: "))

    if ls < li:
        print("Erro. O limite superior é menor do que o limite inferior.")

    else:
        print("Os múltiplos de {} entre {} e {} são:".format(n, li, ls))

    for i in range(li, ls):
        if (i <= ls) and (i % n == 0):
            print(i)


main()
