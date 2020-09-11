def main():
    ls = int(input("Digite o valor do limite superior: "))
    li = int(input("Digite o valor do limite inferior: "))

    if ls < li:
        print("Erro. O valor do limite superior é menor do que o valor do limite inferior.")

    else:
        print("Os números primos entre {} e {} são:".format(li, ls))

        for i in range(li, ls):
            if i <= ls:
                if i == 1 or i == 2 or i == 3 or i == 5 or i == 7:
                    print(i)
                elif (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 5) and (i % 7 != 0):
                    print(i)


main()
