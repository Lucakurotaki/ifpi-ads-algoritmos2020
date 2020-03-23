def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))

    print(maior_menor(num1,num2,num3,num4,num5))

def maior_menor(n1,n2,n3,n4,n5):

    maior = n1
    menor = n2

    if n2 > maior:
        maior = n2
        menor = n1
        
    if n3 > maior:
        maior = n3
    elif n3 < menor:
        menor = n3

    if n4 > maior:
        maior = n4
    elif n4 < menor:
        menor = n4

    if n5 > maior:
        maior = n5
    elif n5 < menor:
        menor = n5

    return "O maior número é {} e, o menor, {}.".format(maior,menor)

main()
