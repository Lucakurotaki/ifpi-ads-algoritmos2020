#Entrada

n = int(input("Insira o número de habitantes: "))

#Entrada/Processamento

if n == 0:
    print("Erro. Digite um número maior do que 0.")
else:
    if n < 0:
        n = n*-1

    cont = 0
    total_s = 0
    total_f = 0

    hab_min = 0
    
    while cont < n:
        print()
        salario = float(input("Digite o valor do salário: "))
        filhos = int(input("Digite a quantidade de filhos: "))

        total_s += salario
        total_f += filhos
        if salario <= 1000:
            hab_min+=1

        cont+=1

    media_s = total_s/n
    media_f = total_f/n
    perc_min = (hab_min*100)/n

#Saída

print("\nMedia de salário da população: R$ {:.2f}\n"
      "Média de número de filhos: {:.2f}\n"
      "Percentual de pessoas com salário de até R$ 1.000,00: {:.1f}%"
      .format(media_s,media_f,perc_min))
