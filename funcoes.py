def define_posicoes(linha, coluna, orientacao, tamanho):

    posicao_navio = [[linha, coluna]] 

    if orientacao == 'vertical':
        for i in range(1,tamanho):
            posicao_navio.append([linha + i, coluna]) 
    else:
        
         for i in range(1,tamanho):
            posicao_navio.append([linha, coluna + i ])

    return posicao_navio



def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicao = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = [posicao]
    else:
        for n,l in frota.items():
            if n == nome_navio:
                l.append(posicao)
    
    return frota
