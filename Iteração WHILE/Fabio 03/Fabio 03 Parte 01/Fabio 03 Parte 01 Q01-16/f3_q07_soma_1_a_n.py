#Entrada

n = float(input("Digite um número: "))

#Proessamento

cont = 0
soma = 0

while cont < n:
    cont+=1
    soma+=cont

#Saida

print("A soma de 1 a {} é: {}".format(int(n),soma))
