import requests
import pandas as pd
from bs4 import BeautifulSoup

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
                   'TOTS3']

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
                   50]

table['PREÇO'] = table['ATIVOS'].map(cotacao)

table['VALOR INVESTIDO'] = [1000.00,
                             500.00,
                            1000.00,
                            1500.00,
                            2000.00,
                            1500.00,
                             750.00,
                            1800.00,
                            1000.00,
                             750.00,
                            1500.00,
                             500.00,
                             800.00,
                             500.00,
                            1000.00]

table['VALOR ATUAL'] = table['PREÇO'] * table['COTAS']

table['RENDIMENTO'] = table['VALOR ATUAL'] - table['VALOR INVESTIDO']

total = sum(table['RENDIMENTO'])

print(table, f'RENDIMENTO TOTAL: {total:.2f}', sep='\n', end='')