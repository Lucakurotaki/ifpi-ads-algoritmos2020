def main():
    num = int(input("Digite um número: "))

    print(par_impar(num))

def par_impar(num):

    if num%2 == 0:
        return "O número {} é par.".format(num)
    else:
        return "O número {} é ímpar.".format(num)

main()
