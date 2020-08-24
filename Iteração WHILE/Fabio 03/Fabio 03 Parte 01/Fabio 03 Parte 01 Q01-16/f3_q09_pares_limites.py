#Entrada

ls = int(input("Digite o valor do limite superior: "))

li = int(input("Digite o valor do limite inferior: "))

#Processamento/Saída

if ls < li:
    print("Erro. O valor do limite superior é menor do que o valor do limite inferior.")
else:
    print("Os números pares entre {} e {} são:".format(li,ls))

cont = 0

while cont <= ls:
    if cont >= li and cont%2 == 0:
        print(cont)
    cont+=1
