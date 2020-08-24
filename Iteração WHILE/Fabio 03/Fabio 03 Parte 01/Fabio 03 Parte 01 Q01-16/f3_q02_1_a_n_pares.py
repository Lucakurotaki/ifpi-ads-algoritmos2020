#Entrada

n = int(input("Digite o número: "))

#Processamento/Saída

if n<3:
    print("Digite um número maior do que 2.")

else:
    cont = 0
    num = 1
    while cont < n:
        if num%2==0:
            print(num)
        cont+=1
        num+=1
