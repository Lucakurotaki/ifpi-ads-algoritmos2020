def main():
    ls = int(input("Digite o valor do limite superior: "))

    li = int(input("Digite o valor do limite inferior: "))

    if ls <= li:
        print("Erro. O valor do limite superior é menor do que o valor do limite inferior.")

    else:
        print("Os números ímpares entre {} e {} são:".format(li, ls))

        for i in range(li, ls):
            if (i <= ls) and (i % 2 != 0):
                print(i)


main()
