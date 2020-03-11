#Entrada

tempo = int(input("Digite o tempo em segundos: "))

#Processamento

horas = tempo//3600
minutos = (tempo%3600)//60
segundos = tempo%60

#Saída

print("{} segundos equivale a {} horas, {} minutos e {} segundos.".format(tempo,horas,minutos,segundos))
