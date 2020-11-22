# %% Importando as bibliotecas
from os import getenv
import pandas as pd
import pymssql
import _mssql
import json
import sys
# %% Conectando ao banco de dados
def read_server_config(path: str):
    try:
        if path.split('.')[-1] == "json":
            # Abre o arquivo JSON
            file = open(path)
            # return JSON object as a dictionary
            configs = json.load(file)
            # fecha o arquivo
            file.close()
            return configs
        else:
            print("O arquivo '{}' não é um arquivo json")
            raise TypeError
            sys.exit()
    except Exception as e:
        print(e)
        file.close()
        return None


def connect_server(path):
    try:
        server = read_server_config(path)
        conn = pymssql.connect(host="{}:{}".format(server['host'],
                                                   server['port']),
                               user=server['user'],
                               password=server['password'],
                               database=server['database'])
        return conn
    except Exception as e:
        print(e)
        sys.exit()
        return None


def request_server(req, cursor):

    cursor.execute(req)

    resposta = []
    row = cursor.fetchone()
    while row:
        resposta.append(row)
        row = cursor.fetchone()
    return resposta


conn = connect_server('./src/config/server.json')
cursor = conn.cursor()
# %% Carregando os valores dos veiculos
# %% Criando o dataframe para o pandas
requisicao_veiculos = """SELECT * FROM Veiculo"""
veiculo = request_server(requisicao_veiculos, cursor)
veiculos = pd.DataFrame(veiculo)
veiculos.head()
# %% Renomeando as colunas
veiculos.columns = ['IDVeiculo',
                    'IDMolelo',
                    'Ano',
                    'Valor',
                    'Placa',
                    'Renavam',
                    'Observacoes',
                    'Chassi',
                    'IDVeiculoMarca',
                    'NumeroFrota',
                    'IDMarcaEquipamento',
                    'IDModeloEquipamento',
                    'NumeroImobilizado',
                    'NumeroSerie',
                    'Tipo',
                    'IDEmpresa']
veiculos.head()
# %% Descobrindo a marca dos veiculos
