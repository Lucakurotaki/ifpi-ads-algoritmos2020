def main():
    numero = int(input("Escreva um número entre 0 e 100: "))

    print(verifica_primo(numero))

def verifica_primo(num):

    if num >= 0 and num <= 100:
        if num == 2 or num == 3 or num == 5 or num == 7:
            return "{} é um número primo.".format(num)
        elif num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0:
            return "{} é um número primo.".format(num)
        else:
            return "{} não é um número primo.".format(num)
    else:
        return "O número digitado não está no internvalo entre 0 e 100."

main()
