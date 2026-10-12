FROM python:3.9

WORKDIR Coinmarketcap

COPY . .

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt




CMD [ "python", "coin_marketcap.py" ]