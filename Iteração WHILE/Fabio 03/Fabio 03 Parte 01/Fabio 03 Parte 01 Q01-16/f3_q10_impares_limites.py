#Entrada

ls = int(input("Digite o valor do limite superior: "))

li = int(input("Digite o valor do limite inferior: "))

#Processament/Saída

if ls <= li:
    print("Erro. O valor do limite superior é menor do que o valor do limite inferior.")

else:
    cont = 0
    while cont < ls:
        if cont > li and cont%2 != 0:
            print(cont)
        cont+=1
