def main():
    num = int(input("Digite um número de dois dígitos: "))
    print(dezena_unidade(num))

def dezena_unidade(num):
    if len(str(num)) == 2:
        dezena = num//10
        centena = num%10
        return verifica_igualdade(num,dezena,centena)
    else:
        return "O número digitado não tem dois dígitos."

def verifica_igualdade(num, dzn, ctn):
    if dzn == ctn:
        return "O algarismo da dezena e da centena de {} são iguais.".format(num)
    else:
        return "O algarismo da dezena e da centena de {} são diferentes.".format(num)

main()
