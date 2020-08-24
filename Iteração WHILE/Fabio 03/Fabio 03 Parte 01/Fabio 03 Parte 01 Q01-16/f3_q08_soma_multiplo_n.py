#Entrada

n = int(input("Digite um número: "))

ls = int(input("Digite o valor do limite superior: "))

li = int(input("Digite o valor do limite inferior: "))

#Processamento/Saída

if ls < li:
    print("Erro. O limite superior é menor do que o limite inferior.")

else:
    print("Os múltiplos de {} entre {} e {} são:".format(n,li,ls))

cont = 0

while cont <= ls:
    if cont >= li and cont%n == 0:
        print(cont)
    cont+=1
