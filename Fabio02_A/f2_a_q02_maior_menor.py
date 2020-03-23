def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print(numero_maior(num1,num2))

def numero_maior(n1,n2):
    if n1 > n2:
        return "{} é o maior e {} é o menor.".format(n1,n2)
    elif n2 > n1:
        return "{} é o maior é {} é o menor.".format(n2,n1)
    else:
        return "Os números são iguais."

main()
