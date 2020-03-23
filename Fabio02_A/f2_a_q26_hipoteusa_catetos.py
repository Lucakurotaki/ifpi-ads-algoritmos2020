def main():
    lado1 = int(input("Digite o valor do primeiro lado: "))
    lado2 = int(input("Digite o valor do segundo lado: "))
    lado3 = int(input("Digite o valor do terceiro lado: "))

    print(triangulo(lado1,lado2,lado3))

def triangulo(l1,l2,l3):
    if l1 > l2+l3 or l2 > l1+l3 or l3 > l1+l2:
        return "Não é um triângulo."
    elif l1 > l2 and l1 > l3:
        return "A hipotenusa mede {} e, seus catetos, {} e {}.".format(l1,l2,l3)
    elif l2 > l1 and l2 >l3:
        return "A hipotenusa mede {} e, seus catetos, {} e {}.".format(l3,l1,l3)
    elif l3 > l2 and l3 > l1:
        return "A hipotenusa mede {} e, seus catetos, {} e {}.".format(l3,l1,l2)
    else:
        return "Não há hipotenusa e catetos, pois, é um triângulo equilátero."

main()
