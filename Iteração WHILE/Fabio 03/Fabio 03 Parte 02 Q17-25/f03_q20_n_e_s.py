#Entrada

n = int(input("Digite um número: "))

#Processamento

if n < 1:
    print("Erro. Digite um número positivo.")
else:
    cont = 1
    s = 0
    while cont <= n:
        if cont%2 != 0:
            s+=1/cont
        else:
            s-=1/cont
        cont+=1

#Saída

print("S = {}".format(s))
