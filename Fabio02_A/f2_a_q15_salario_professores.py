def main():
    ha1 = int(input("Digite a qunatidade de horas aula do primeiro professor: "))
    vh1 = float(input("Digite o valor por hora: "))
    
    ha2 = int(input("Digite a  quantidade de horas aula do segundo professor: "))
    vh2 = float(input("Digite o valor por hora: "))
    
    print(maior_salario(ha1,vh1,ha2,vh2))

def salario_total(ha,va):

    total = ha*va

    return total

def maior_salario(ha1,v1,ha2,v2):

    total_pf1 = salario_total(ha1,v1)
    total_pf2 = salario_total(ha2,v2)

    if total_pf1 > total_pf2:
        return "O primeiro professor tem salário maior."
    elif total_pf2 > total_pf1:
        return "O segundo professor tem salário maior."
    else:
        return "Ambos os professores têm o mesmo salário."

main()
