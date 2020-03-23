def main():
    valor1 = int(input("Digite o primeiro número: "))
    valor2 = int(input("Digite o segundo número: "))
    opcao = int(input("Indique a operação a ser feita:\n\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\n: "))

    print(operacao(valor1,valor2,opcao))

def operacao(n1,n2,op):
    if op == 1:
        soma = n1+n2
        return "O resultado da adição entre {} e {} é: {}.".format(n1,n2,soma)
    elif op == 2:
        diferenca = n1-n2
        return "O resultado da subtração entre {} e {} é: {}.".format(n1,n2,diferenca)
    elif op == 3:
        produto = n1*n2
        return "O resultado da multiplicação entre {} e {} é: {}.".format(n1,n2,produto)
    elif op == 4:
        razao = n1/n2
        return "O resultado da divisão entre {} e {} é: {}.".format(n1,n2,razao)
    else:
        return "Opção não identificada."

main()
