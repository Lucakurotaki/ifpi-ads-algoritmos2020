def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    print(numeros_iguais(num1,num2,num3))

def numeros_iguais(n1,n2,n3):
    if n1 == n2 and n2 == n3:
        return "Existem 3 números iguais."
    elif n1 == n2 or n1 == n3 or n2 == n3:
        return "Existem 2 números iguais."
    else:
        return "Todos os números são diferentes."

main()
