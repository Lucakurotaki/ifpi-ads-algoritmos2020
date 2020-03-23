def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    print(maior_numero(num1,num2,num3))

def maior_numero(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return "{} é o maior número entre {}, {} e {}.".format(n1,n1,n2,n3)
    elif n2 > n1 and n2 > n3:
        return "{} é o maior número entre {}, {} e {}.".format(n2,n1,n2,n3)
    elif n3 > n1 and n3 > n2:
        return "{} é o maior número entre {}, {} e {}.".format(n3,n1,n2,n3)
    else:
        return "Os números são iguais."

main()
