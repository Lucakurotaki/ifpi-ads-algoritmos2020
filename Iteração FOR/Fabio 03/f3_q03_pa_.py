def main():
    a = int(input("Digite o valor inicial(A0): "))

    lim = int(input("Digite o valor Limite: "))

    r = int(input("Digite a razão: "))

    if a < 0:
        print("Digite um valor positivo.")
    elif lim <= a:
        print("Digite um valor limite maior do que o valor inicial.")
    elif r <= 0:
        print("Digite um valor maior do que 0.")

    else:
        for i in range(a, lim, r):
            print(i)


main()
