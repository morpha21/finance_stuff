import pandas as pd
import requests


hoje = pd.to_datetime("today").strftime("%d/%m/%Y")

def get_bc(codigo, data_inicial=None, data_final=hoje):
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo)
    p   = {
        'dataInicial': data_inicial,
        'dataFinal'  : data_final
    }
    response = requests.get(url, params=p)
    if response.status_code == 200:
        dados = pd.DataFrame(response.json())
    else:
        print('Erro na requisição:', response.status_code)
    dados['data'] = pd.to_datetime(dados['data'], format="%d/%m/%Y")
    dados.set_index('data', inplace=True)
    dados['valor'] = pd.to_numeric(dados['valor'])
    dados
    return dados
