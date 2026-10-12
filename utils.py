import pandas as pd 
import requests
import time
import os


def transform(data,info):

    rows = []

    for coin in data:
        row = {
            'id': info['id'],
            'name': info['name'],
            'address': coin['wallet_address'],
            'asset': coin['platform']['symbol']
        }
        rows.append(row)

    return pd.DataFrame(rows)

def fetch_data(url,params):

    response = requests.get(url, params=params, headers={
        "Accept": "application/json",
        "X-CMC_PRO_API_KEY":os.getenv("KEY_API"),
    })

    response.raise_for_status()

    return response.json()

def fetch_exchanges(data):
    dfs=[]
    for val in data :
            try:
            
                rep_assets = fetch_data(os.getenv('URL_API'),params={'id':val['id']})

                data_assets=rep_assets['data']

                new_df= transform(data_assets,info= {'name':val['name'], 'id':val['id']})

                dfs.append(new_df)

                time.sleep(3)
            
            except Exception as e :
                print(f'erreur est :{e}')
                time.sleep(5)

    return dfs
            
