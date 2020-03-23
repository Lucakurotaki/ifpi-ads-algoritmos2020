def main():
    lado1 = int(input("Digite o valor do primeiro lado: "))
    lado2 = int(input("Digite o valor do segundo lado: "))
    lado3 = int(input("Digite o valor do terceiro lado: "))

    print(triangulo(lado1,lado2,lado3))

def triangulo(l1,l2,l3):
    if l1+l2 > l3 and l2+l3 > l1 and l1+l3 > l2:
        return "É um triângulo, do tipo "+verifica_tipo(l1,l2,l3)
    else:
        return "Não é um triângulo."

def verifica_tipo(l1,l2,l3):
    if l1 == l2 and l2 == l3:
        return "equilátero."
    elif l1 == l2 or l2 == l3 or l1 == l3:
        return "isóceles."
    else:
        return "escaleno."
    
main()
