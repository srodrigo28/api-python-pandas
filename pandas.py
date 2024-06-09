import pandas as pd
from flask import Flask

tabela = pd.read_csv('base1.csv')
total = tabela['valor'].sum()
produto = tabela['produto']
print('Total: R$ ', total)