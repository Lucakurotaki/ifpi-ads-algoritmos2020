#Entrada

tempo = int(input("Digite a quantidade de minutos: "))

#Processamento

dias = tempo//1440
horas = (tempo%1440//60)
minutos = tempo%60

#Saída

print("{} minutos equivale a {} dias, {} horas e {} minutos.".format(tempo,dias,horas,minutos))
