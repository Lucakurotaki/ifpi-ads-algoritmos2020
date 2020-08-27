#Entrada/Processamento

n = int(input("Digite o número de fichas: "))

if n == 0:
    print("Erro. Digite um valor positivo.")
    
else:
    if n < 0:
        n = n*-1
        
    cont = 0

    idts = 0
    
    id_maior = 0
    maior_peso = 0
    id_menor = 0
    menor_peso = 0

    while cont < n:
        idt = int(input("Digite o número de identidade: "))
        peso = float(input("Digite o peso: "))
        if peso > maior_peso or maior_peso == 0:
            maior_peso = peso
            id_maior = idt
        if peso < menor_peso or menor_peso == 0:
            menor_peso = peso
            id_menor = idt
        cont+=1
        

#saída

print("Boi mais gordo: ID: {}; Peso: {} kg.\n"
      "Boi mais magro: ID: {}; Peso: {} kg.".format(id_maior,maior_peso,id_menor,menor_peso))
