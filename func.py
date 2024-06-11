import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

gestaoVista = pd.read_csv('gestao_a_vista.CSV', sep=';', decimal=',')

#Função que calcula soma
def soma():
    print(gestaoVista.head())
    while True:
        coluna = input("Especifique a coluna desejada: ").upper()
        if coluna not in gestaoVista:
            print(f'A coluna {coluna} não foi encontrada')
        else:
            print("A coluna encontrada foi encontrada!")
            break
    somaColuna = gestaoVista[coluna].sum()
    print(f"A soma da coluna {coluna} é {somaColuna}")
    return menuacoes()

#Função que calcula media
def media():
    print(gestaoVista.head())
    while True:
        coluna = input("Especifique a coluna desejada: ").upper()
        if coluna not in gestaoVista:
            print(f'A coluna {coluna} não foi encontrada')
        else:
            print("A coluna encontrada foi encontrada!")
            break
    mediaColuna = gestaoVista[coluna].mean()
    print(f"A media da coluna {coluna} é {mediaColuna}")
    return menuacoes()

#Função que calcula mediana
def mediana():
    print(gestaoVista.head())
    while True:
        coluna = input("Especifique a coluna desejada: ").upper()
        if coluna not in gestaoVista:
            print(f'A coluna {coluna} não foi encontrada')
        else:
            print("A coluna encontrada foi encontrada!")
            break
    medianaColuna = gestaoVista[coluna].median()
    print(f"A media da coluna {coluna} é {medianaColuna}")
    return menuacoes()

#Função que calcula desvio padrão
def desvioPadrao():
    print(gestaoVista.head())
    while True:
        coluna = input("Especifique a coluna desejada: ").upper()
        if coluna not in gestaoVista:
            print(f'A coluna {coluna} não foi encontrada')
        else:
            print("A coluna encontrada foi encontrada!")
            break
    desvioColuna = gestaoVista[coluna].std()
    print(f"O desvio padrão da coluna {coluna} é {desvioColuna}")
    return menuacoes()

#Função que exibe o menu de ações
def menuacoes():
    while True:
        print("\nQue operação deseja realizar?"
              "\n1 - Soma"
              "\n2 - Média"
              "\n3 - Mediana"
              "\n4 - Desvio padrão"
              "\n5 - Visão geral"
              "\n6 - Sair da aplicação")

        escolha = int(input("Escolha uma opção de 1 a 6: "))

        if escolha == 1:
            soma()
        elif escolha == 2:
            media()
        elif escolha == 3:
            mediana()
        elif escolha == 4:
            desvioPadrao()
        elif escolha == 5:
            print(gestaoVista.describe())
        elif escolha == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")