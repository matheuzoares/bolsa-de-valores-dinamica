import requests
import pandas as pd
from bs4 import BeautifulSoup
from numpy import float32, int32

def cotacao(ticker: str):
    page = requests.get(f"https://www.google.com/search?q={ticker}")
    sourceCode = page.content

    soup = BeautifulSoup(sourceCode, 'html.parser')
    text = soup.find('div', class_="BNeawe iBp4i AP7Wnd").get_text()
    value = text.split()[0]
    changeDotToComma = value.replace(',', '.')
    price = float(changeDotToComma)

    return price

table = pd.DataFrame()

table['ATIVOS'] = ['MGLU3',
                   'EGIE3',
                   'TRPL4',
                   'SAPR11',
                   'ITSA4',
                   'BBDC4',
                   'KLBN11',
                   'BBSE3',
                   'FLRY3',
                   'MYPK3',
                   'WEGE3',
                   'SMTO3',
                   'TAEE11',
                   'LCAM3',
                   'TOTS3',
                   'IRBR3',
                   'OIBR3']

table['COTAS'] = [124,
                   10,
                   50,
                   65,
                  200,
                   75,
                   40,
                   70,
                   41,
                   50,
                   42,
                   25,
                   27,
                   20,
                   50,
                   10,
                  100]

table['PREÇO'] = table['ATIVOS'].map(cotacao)

table['VALOR INVESTIDO'] = [1098.25,
                             373.30,
                            1008.30,
                            1610.50,
                            1948.00,
                            1597.00,
                             953.45,
                            1883.70,
                            1042.80,
                             775.00,
                            1709.18,
                             608.75,
                             808.40,
                             536.40,
                            1098.50,
                             183.90,
                             123.00]

table['VALOR ATUAL'] = table['PREÇO'] * table['COTAS']

table['RENDIMENTO'] = table['VALOR ATUAL'] - table['VALOR INVESTIDO']

'''
table['COTAS'] = table['COTAS'].astype(int32)
table['PREÇO'] = round(table['PREÇO'].astype(float32), 2)
table['VALOR INVESTIDO'] = round(table['VALOR INVESTIDO'].astype(float32), 2)
table['VALOR ATUAL'] = round(table['VALOR ATUAL'].astype(float32), 2)
table['RENDIMENTO'] = round(table['RENDIMENTO'].astype(float32), 2)

table.loc['TOTAL'] = pd.Series(table['RENDIMENTO'].sum(), index = ['RENDIMENTO'])
table.loc['TOTAL'] = table.loc['TOTAL'].fillna('-')
'''

print(table)