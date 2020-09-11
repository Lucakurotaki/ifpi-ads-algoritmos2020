def main():

    n = int(input("Digite um número: "))

    if n < 2:
        print("Erro. Digite um número maior do que 1.")

    else:

        for i in range(1, n+1):
            print(i)


main()
