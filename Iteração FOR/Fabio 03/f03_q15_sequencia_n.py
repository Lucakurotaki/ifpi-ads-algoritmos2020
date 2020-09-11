def main():

    n = int(input("Digite um número positivo: "))

    if n < 1:
        print("Erro. Digite um número maior do que 0.")
    else:
        num = 1
        for i in range(2, n+2):
            print(num)
            num += i


main()
