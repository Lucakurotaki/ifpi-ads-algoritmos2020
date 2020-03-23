def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    print(ordem_crescente(num1,num2,num3))

def ordem_crescente(n1,n2,n3):
    if n1 > n2 and n2 >= n3:
        return "A ordem crescente é: {}, {}, {}.".format(n1,n2,n3)
    elif n1 > n3 and n3 >= n2:
        return "A ordem crescente é: {}, {}, {}.".format(n1,n3,n2)
    elif n2 > n1 and n1 >= n3:
        return "A ordem crescente é: {}, {}, {}.".format(n2,n1,n3)
    elif n2 > n3 and n3 >= n1:
        return "A ordem crescente é: {}, {}, {}.".format(n2,n3,n1)
    elif n3 > n1 and n1 >= n2:
        return "A ordem crescente é: {}, {}, {}.".format(n3,n1,n2)
    elif n3 > n2 and n2 >= n1:
        return "A ordem crescente é: {}, {}, {}.".format(n3,n2,n1)
    else:
        return "Todos os números são iguais."

main()
