import pandas as pd 
from utils import fetch_data, fetch_exchanges

import os

def save_json(data):
        data.to_json('coinmarketcap_exchange.json',orient='records',indent=4)
    

def main ():

    api_key = os.getenv("URL_API_EXCHANGE")
    params={
        "start": "1",
        'limit':10
    }
    
    response = fetch_data(api_key,params=params)
    data = response['data']
    dfs= fetch_exchanges(data)
    df_final = pd.concat(dfs, ignore_index=True)
    
    save_json(df_final)


if __name__ == '__main__':
    main()