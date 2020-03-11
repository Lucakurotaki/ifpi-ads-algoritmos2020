#Entrada

tempo = int(input("Digite a quantidade de horas: "))

#Processamento

semanas = tempo//168
dias = (tempo%168)//24
horas = tempo%24

#Saída

print("{} horas euquivale a {} semanas, {} dias e {} horas.".format(tempo,semanas,dias,horas))
