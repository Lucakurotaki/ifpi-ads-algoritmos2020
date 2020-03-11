#Entrada

a = int(input("Digite o valor do A (inteiro e positivo): "))
b = int(input("Digite o valor do B (inteiro e positivo): "))
c = int(input("Digite o valor do C (inteiro e positivo): "))

#Processamento

r = (a+b)**2
s = (b+c)**2

d = (r+s)/2

#Saída
print("\nR=(A+B)², logo, R={}.".format(r))
print("S=(B+C)², logo, S={}.".format(s))
print("\nD=(R+S)/2, logo, D={}.".format(d))
