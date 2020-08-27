#Entrada

n = int(input("Digite um número: "))

#Processamento

if n < 1:
    print("Erro. Digite um número positivo.")

else:
    count = 1
    s = 0
    while count <= n:
        s += 1/count
        count+=1

#Saída

print("S = {}".format(s))
