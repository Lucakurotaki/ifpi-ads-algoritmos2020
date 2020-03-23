def main():
    angulo = float(input("Digite o valor do ângulo: "))

    print(quadrante(angulo))

def quadrante(ang):
    if ang < 0 or ang > 360:
        return "O valor do ângulo é inválido."
    elif ang >= 0 and ang < 90:
        return "O ângulo de {}º pertence ao primeiro quadrante.".format(ang)
    elif ang >= 90 and ang < 180:
        return "O ângulo de {}º pertence ao segundo quadrante.".format(ang)
    elif ang >= 180 and ang < 270:
        return "O ângulo de {}º pertence ao terceiro quadrante.".format(ang)
    else:
        return "O ângulo de {}º pertence ao quarto quadrante.".format(ang)

main()
