def main():
    n = int(input("Digite um número positivo: "))

    if n < 2:
        print("Erro. Digite um número maior do que 1.")

    else:
        n1 = 0
        n2 = 1
        soma = 0
        print(n1)
        for i in range(0, n-1):
            soma = (n1 + n2)
            print(n2)
            n1 = n2
            n2 = soma


main()
