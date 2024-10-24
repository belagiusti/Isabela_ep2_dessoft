### QUESTAO 1 ###

def define_posicoes(linha, coluna, orientacao, tamanho):

    posicao_navio = [[linha, coluna]] 

    if orientacao == 'vertical':
        for i in range(1,tamanho):
            posicao_navio.append([linha + i, coluna]) 
    else:
        
         for i in range(1,tamanho):
            posicao_navio.append([linha, coluna + i ])

    return posicao_navio




### QUESTAO 2 ###

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicao = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = [posicao]
    else:
        for n,l in frota.items():
            if n == nome_navio:
                l.append(posicao)
    
    return frota





### QUESTAO 3 ###

def faz_jogada (tabuleiro, linha, coluna):

    posicao = tabuleiro[linha][coluna]
    if posicao == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    
    return tabuleiro 






### QUESTAO 4 ###

def posiciona_frota(dic_frota):

    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


    for navio, lista in dic_frota.items():
        for l2 in lista:
            for l3 in l2:
                linha = l3[0]
                coluna = l3[1]
                tabuleiro[linha][coluna] = 1
        
    return tabuleiro 





### QUESTAO 5 ###


def afundados(frota, tabuleiro):

    navios_afundados = 0

    for navios in frota.values():
        for navio in navios:
            afundado = True
            for posicao in navio:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != 'X':  
                    break
            if afundado:
                navios_afundados += 1  

    return navios_afundados
