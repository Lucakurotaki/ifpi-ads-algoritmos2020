#Entrada

c_fabrica = float(input("O preço de fábrica do carro: "))

#Processamento

distribuidor = c_fabrica*0.28
imposto = c_fabrica*0.45

p_consumidor = c_fabrica+distribuidor+imposto

#Saída

print("O preço para o consumidor é de R${:.2f}.".format(p_consumidor))
