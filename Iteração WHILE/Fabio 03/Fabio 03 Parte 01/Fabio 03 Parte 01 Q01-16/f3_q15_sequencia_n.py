def main():
    #Entrada

    n = int(input("Digite um número positivo: "))

    #Processamento/Saída

    if n < 1:
        print("Erro. Digite um número maior do que 0.")
    else:
        cont = 0
        add = 2
        soma = 1
        while cont < n:
            print(soma)
            soma+=add
            add+=1
            cont+=1
            
main()
