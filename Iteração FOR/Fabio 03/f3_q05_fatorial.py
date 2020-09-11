def main():
    num = int(input("Digite o número: "))

    if num < 1:
        print("Digite um número maior do que 0.")

    else:
        fat = 1
        for i in range(1, num+1):
            fat *= i

        print("{}! = {}".format(num, fat))


main()
