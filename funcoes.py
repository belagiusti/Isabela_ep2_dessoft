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
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1  

    return navios_afundados




### QUESTAO 6 ###

def posicao_valida(frota, linha, coluna, orientacao, tamanho):

    tamanho_tabuleiro = 10
    
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes_navio:
        linha_pos, coluna_pos = posicao
        if linha_pos < 0 or linha_pos >= tamanho_tabuleiro or coluna_pos < 0 or coluna_pos >= tamanho_tabuleiro:
            return False  # Fora dos limites do tabuleiro


    for navios in frota.values():
        for navio in navios:
            for posicao_ocupada in navio:
                if posicao_ocupada in posicoes_navio:
                    return False  # Posição já ocupada por outro navio

    return True  











### QUESTAO 7 ###

def monta_frota():
    frota = {
        "porta-aviões": [],
        "navio-tanque": [],
        "contratorpedeiro": [],
        "submarino": []
    }

    embarcacoes = {
        "porta-aviões": (4, 1),
        "navio-tanque": (3, 2),
        "contratorpedeiro": (2, 3),
        "submarino": (1, 4)
    }

    for nome_navio, (tamanho, quantidade) in embarcacoes.items():
        for i in range(quantidade):
            while True:
                print(f"\nInsira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))

                if nome_navio != "submarino":
                    orientacao = int(input("[1] Vertical [2] Horizontal >"))
                    orientacao = 'vertical' if orientacao == 1 else 'horizontal'
                else:
                    orientacao = 'vertical'

                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
                    break
                else:
                    print("Esta posição não está válida! Tente novamente.")
    
    return frota


# def main():
#     frota = monta_frota()
#     print("\nFrota final:")
#     print(frota)


# if __name__ == "__main__":
#     main()