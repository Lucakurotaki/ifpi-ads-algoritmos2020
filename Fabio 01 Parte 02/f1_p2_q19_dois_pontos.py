#Entrada

x1 = int(input("Digite o valor do x1: "))
y1 = int(input("Digite o valor do y1: "))
x2 = int(input("Digite o valor do x2: "))
y2 = int(input("Digite o valor do y2: "))

#Processamento

p1 = (x2-x1)**2
p2 = (y2-y1)**2
d = (p1+p2)**(1/2)

#Saída

print("A distância entre os dois pontos é de {:.3f}.".format(d))
