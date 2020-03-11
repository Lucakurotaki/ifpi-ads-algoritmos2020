#Entrada
print("\nax + by = c\ndx + ey = f")
a = int(input("\nDigite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))
e = int(input("Digite o valor de e: "))
f = int(input("Digite o valor de f: "))

#Processamento

x = (c*e-b*f)/(a*e-b*d)
y = (a*f-c*d)/(a*e-b*d)

#Saída

print("\nPara\n{}x + {}y = {}\n{}x + {}y = {}:\n\nx = {} e y = {}.".format(a,b,c,d,e,f,x,y))
