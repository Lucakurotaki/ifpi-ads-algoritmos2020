#Entrada

n = int(input("Digite o número: "))

#Processamento/Saída

if n<2:
    print("Digite um número maior do que 1.")

else:
    cont = 0
    num = 1
    while cont < n:
        print(num)
        num+=1
        cont+=1
