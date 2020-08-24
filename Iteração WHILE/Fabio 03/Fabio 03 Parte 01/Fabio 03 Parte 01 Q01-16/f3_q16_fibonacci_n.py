def main():
    #Entrada

    n = int(input("Digite um número positivo: "))

    #Processamento/Saída

    if n < 2:
        print("Erro. Digite um número maior do que 1.")

    else:
        n1 = 0
        n2 = 1
        soma = 0
        cont = 1
        print(soma)
        while cont < n:
            soma=n1+n2
            print(n2)
            n1=n2
            n2=soma
            cont+=1

main()
