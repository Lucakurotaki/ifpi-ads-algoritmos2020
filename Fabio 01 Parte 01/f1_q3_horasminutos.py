# Entrada
print ('Bem-vindo a ferramenta de conversão de unidades de tempo!')
horas_e_minutos = int(input ('Digite o valor em minutos: '))

# Processamento
horas = horas_e_minutos // 60
minutos = horas_e_minutos % 60

# Saída
print ('O valor em horas e minutos é: {} horas e {} minutos'.format(horas, minutos))