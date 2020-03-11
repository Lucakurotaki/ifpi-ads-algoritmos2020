#Entrada

tempo = int(input("Digite a quantidade de meses: "))

#Processamento

anos = tempo//12
meses = tempo%12

#Saída

print("{} dias equivale a {} anos e {} meses.".format(tempo,anos,meses))
