def main():
    ang1 = int(input("Digite o valor do primeiro ângulo: "))
    ang2 = int(input("Digite o valor do segundo ângulo: "))
    ang3 = int(input("Digite o valor do terceiro ângulo: "))

    print(triangulo(ang1,ang2,ang3))

def triangulo(a1,a2,a3):
    if a1 + a2 + a3 == 180:
        return "É um triângulo, do tipo "+verifica_tipo(a1,a2,a3)
    else:
        return "Não é um triângulo."

def verifica_tipo(a1,a2,a3):
    if a1 < 90 and a2 < 90 and a3 < 90:
        return "acutângulo."
    elif a1 > 90 or a2 > 90 or a3 > 90:
        return "obtusângulo."
    else:
        return "retângulo."

main()
