def main():
    n = int(input("Digite um número: "))

    soma = 0
    for i in range(1, n+1):
        soma += i

    print("A soma de 1 a {} é: {}".format(int(n), soma))


main()
