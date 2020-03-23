def main():
    altura = float(input("Digite a altura (m): "))
    peso = float(input("Digite o peso (kg): "))

    print(imc(altura,peso))

def imc(h,w):
    indice = w/h**2

    if indice < 25:
        return "Peso normal."
    elif indice >= 25 and indice <= 30:
        return "Obeso."
    else:
        return "Obesidade mórbida."

main()
