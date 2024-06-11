import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import func as fc

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

gestaoVista = pd.read_csv('gestao_a_vista.CSV', sep=';', decimal=',')

print("Bem vindo ao programa de estatísticas básicas para análise de dados!"
      "\nPor favor, escolha uma das opções abaixo")


fc.menuacoes()








