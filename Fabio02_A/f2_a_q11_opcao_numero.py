def main():
    opcao = int(input("Escolha uma opção (1, 2 ou 3): "))
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digte o terceiro número: "))

    print(opcao_escolhida(opcao,num1,num2,num3))

def opcao_escolhida(op,n1,n2,n3):

    if op == 1:
        return "O número da opção escolhida é: {}.".format(n1)
    elif op == 2:
        return "O número da opção escolhida é: {}.".format(n2)
    elif op == 3:
        return "O número da opção escolhida é: {}.".format(n3)
    else:
        return "Opção não identificada."

main()
