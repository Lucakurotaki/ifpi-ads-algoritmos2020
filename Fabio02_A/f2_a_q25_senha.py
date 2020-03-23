def main():
    senha = int(input("Insira a senha: "))

    print(verifica_senha(senha))

def verifica_senha(senha):

    s_correta = 1234

    if senha == s_correta:
        return "Acesso permitido."
    else:
        return "Acesso negado."

main()
