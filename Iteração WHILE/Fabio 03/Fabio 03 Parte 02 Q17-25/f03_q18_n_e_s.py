#Entrada

n = int(input("Digite um número: "))

#Processamento

if n < 1:
    print("Erro. Digite um número positivo.")
else:
    c1 = 1
    c2 = 0
    s = 0
    while c1 <= n:
        s += c1/(n-c2)
        c1+=1
        c2+=1

#saída

print("S = {}".format(s))
