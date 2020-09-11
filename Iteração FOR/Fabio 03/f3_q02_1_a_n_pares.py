def main():

    n = int(input("Digite um número: "))

    if n < 3:
        print("Erro. Digite um número maior do que 2.")

    else:
        for i in range(1, n+1):
            if i % 2 == 0:
                print(i)


main()
