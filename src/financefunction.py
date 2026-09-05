import pandas as pd
import matplotlib.pyplot as plt
import requests
from   cycler import cycler



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

def dataplot(data, labels, size=(8,3), ylabel=None):
  cores = cycler(color=['k','y','mediumseagreen','g','chocolate','m','b','r'])
  fig1 = plt.figure(figsize=size, dpi=100, facecolor='moccasin')

  axes1 = fig1.add_axes([0, 0, 1, 1])
  axes1.set_prop_cycle(cores)
  for d,l in zip(data, labels): 
    axes1.plot(data[0].index, d, label=l)
  axes1.set_ylabel(ylabel)
  axes1.legend(loc=0)
  plt.show()