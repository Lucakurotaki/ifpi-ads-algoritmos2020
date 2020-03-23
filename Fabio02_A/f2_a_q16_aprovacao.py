def main():
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    print(aprovacao(nota1,nota2))

def aprovacao(n1,n2):
    if valida_nota(n1) == True and valida_nota(n2) == True:
        media = calc_media(n1,n2)
        if media >= 7:
            return "Aprovado."
        else:
            return final(media,int(input("Digite a nota do exame: ")))
    else:
        return "Notas inválidas."

def final(media,exame):
    if valida_nota(exame) == True:
        if calc_media(media,exame) >= 7:
            return "Aprovado."
        else:
            return "Reprovado."
    else:
        return "Nota do exame inválida."

def calc_media(n1,n2):
    media = (n1+n2)/2

    return media

def valida_nota(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False

main()
