def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    num4 = int(input("Digite o quarto número: "))
    num5 = int(input("Digite o quinto número: "))

    print(media_maiores(num1,num2,num3,num4,num5))

def calcular_media(n1,n2,n3,n4,n5):
    media = (n1+n2+n3+n4+n5)/5

    return media

def media_maiores(n1,n2,n3,n4,n5):

    media = calcular_media(n1,n2,n3,n4,n5)

    maiores = ""

    if n1 > media:
        maiores += "\n{}".format(n1)
    if n2 > media:
        maiores += "\n{}".format(n2)
    if n3 > media:
        maiores += "\n{}".format(n3)
    if n4 > media:
        maiores += "\n{}".format(n4)
    if n5 > media:
        maiores += "\n{}".format(n5)

    return "A média dos cinco números é {}, e os números maiores do que a média são:\n{}\n".format(media,maiores)

main()
