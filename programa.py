 ### QUESTAO 7 ###
from funcoes import define_posicoes, preenche_frota, posicao_valida



# def monta_frota():

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
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
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
                print("Esta posição não está válida!")

print (frota)


# def main():
#     frota = monta_frota()
#     print("\nFrota final:")
#     print(frota)


# if __name__ == "__main__":
#     main()