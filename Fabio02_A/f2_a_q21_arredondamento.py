def main():
    numero = float(input("Digite um número: "))

    print(arredondamento(numero))

def arredondamento(num):

    s_decimal = num//1
    decimal = num - s_decimal

    if decimal >= 0.5:
        return "{} arredondado é: {}".format(num,int(s_decimal+1))
    else:
        return "{} arredondado é: {}".format(num,int(s_decimal))

main()
