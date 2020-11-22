# %% import librarys
import requests
import json
import pandas as pd
import time
# %% read models
marcas_carros = pd.read_json("./carros/marcas_carros.json")
marcas_carros.head()
# %%
tipo = "carros"
acao = "veiculos"
# %%
for _id in marcas_carros['id']:
    get_veiculo = "http://fipeapi.appspot.com/api/1/{}/{}/{}.json".format(
        tipo, acao, _id)
    name_id = marcas_carros.loc[marcas_carros['id']
                                   == _id]['name'].values[0]
    path_json = './carros/marcas/{}.json'.format(name_id)
    print(path_json)
    response = requests.get(get_veiculo)
    if(response.status_code == 200):
        data = response.json()
        with open(path_json,'w') as f:
            json.dump(data,f)
    else :
        time.sleep(5)
# %%
