def main():
    h_inicio = int(input("Digite a hora do início do jogo: "))
    m_inicio = int(input("Digite o minuto do início do jogo: "))
    h_fim = int(input("Digite a hora do fim do jogo: "))
    m_fim = int(input("Digite o minuto do fim do jogo: "))

    print(duracao(h_inicio,m_inicio,h_fim,m_fim))

def duracao(hi,mi,hf,mf):

    if hf >= hi and mf >= mi:
        dur_h = hf - hi
        dur_min = mf - mi

    elif hf <= hi and mf < mi:
        dur_h = 23+hf - hi
        dur_min = 60+mf - mi
        
    elif hf < hi and mf >= mi:
        dur_h = 24+hf - hi
        dur_min = mf - mi
        
    elif hf > hi and mf < mi:
        dur_h = hf - hi
        dur_min = 60+mf - mi

    return "A duração do jogo é de {} horas e {} minutos.".format(dur_h,dur_min)

main()
