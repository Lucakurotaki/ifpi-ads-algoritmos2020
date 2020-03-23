def main():
    numero = int(input("Digite um número de 4 dígitos: "))

    print(numero_novo(numero))

def numero_novo(num):
    if verifica_numero(num) == False:
        return "O número não possui 4 dígitos."

    dig1 = num//100
    dig2 = num%100

    soma = dig1+dig2

    if soma**2 == num:
        return "O número {} obedece à característica em questão.".format(num)
    else:
        return "O número {} não obedece à característica em questão.".format(num)

def verifica_numero(num):
    if len(str(num)) != 4:
        return False
    else:
        return True
main()
