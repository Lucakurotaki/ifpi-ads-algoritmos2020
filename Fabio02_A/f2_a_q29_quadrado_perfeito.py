def main():
    numero = int(input("Digite um número de 4 dígitos: "))

    print(quadrado_perfeito(numero))

def quadrado_perfeito(numero):
    if verifica_numero(numero) == False:
        return "O número não possui 4 dígitos."

    raiz = numero**(1/2)

    dig1 = numero//100
    dig2 = numero%100

    if raiz == dig1+dig2:
        return "{} é um quadrado perfeito.".format(numero)
    else:
        return "{} não é um quadrado perfeito.".format(numero)

def verifica_numero(num):
    if len(str(num)) != 4:
        return False
    else:
        return True

main()
