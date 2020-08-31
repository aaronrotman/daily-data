# Dependencies
import requests
import json
from datetime import datetime
import os

# LOCAL DEPLOYMENT
# Import config variables from local config file
# from config import etherscan_key, alphavantage_key

# HEROKU DEPLOYMENT
# Get config variables from Heroku config variables
etherscan_key = os.environ.get('etherscan_key')
alphavantage_key = os.environ.get('alphavantage_key')

# Function to return current Ethereum gas data
def get_gas_data():
    try:
        query_url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={etherscan_key}"
        gas_response = requests.get(query_url)
        gas_price = json.loads(gas_response.text)
        results = gas_price['result']
        gas_dict = {
            "last_block": results['LastBlock'],
            "safe_gas": f"{results['SafeGasPrice']} gwei",
            "propose_gas": f"{results['ProposeGasPrice']} gwei"
        }
        return gas_dict

    # Handle api call failures
    except Exception as e:
        print(e)
        gas_dict = {
            "last_block": "Data Unavailable",
            "safe_gas": "Data Unavailable",
            "propose_gas": "Data Unavailable"
        }
        return gas_dict

# Function to return the current Ethereum price data
def get_eth_price():
    try:
        eth_price_url = f"https://api.etherscan.io/api?module=stats&action=ethprice&apikey={etherscan_key}"
        eth_response = requests.get(eth_price_url)
        eth_price = json.loads(eth_response.text)
        eth_result = eth_price['result']

        # Convert timestamp into a string
        epoch_time = int(eth_result['ethusd_timestamp'])
        string_time = datetime.fromtimestamp(epoch_time).strftime('%X')

        eth_dict = {
            "eth_usd": f"${eth_result['ethusd']}",
            "time": string_time
        }
        return eth_dict

    # Handle api call failures
    except Exception as e:
        print(e)
        eth_dict = {
            "eth_usd": "Data Unavailable",
            "time": "Data Unavailable"
        }
        return eth_dict

# Function to return current price data for Vanguard Total Stock Market ETF (VTI)
def get_stock_data(ticker):
    try:
        stock_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={alphavantage_key}"
        stock_response = requests.get(stock_url)
        stock_price = json.loads(stock_response.text)
        stock_result = stock_price["Global Quote"]
        stock_dict = {
            "ticker": stock_result['01. symbol'],
            "price": f"${stock_result['05. price']}",
            "open": f"${stock_result['02. open']}",
            "daily_high": f"${stock_result['03. high']}", 
            "daily_low": f"${stock_result['04. low']}", 
            "last_close": f"${stock_result['08. previous close']}",
            "change": f"${stock_result['09. change']}",
            "change_percent": stock_result['10. change percent'],
            "volume": stock_result['06. volume']     
        }
        return stock_dict

    # Handle api call failures
    except Exception as e:
        print(e)
        stock_dict = {
            "ticker": "Data Unavailable",
            "price": "Data Unavailable",
            "open": "Data Unavailable",
            "daily_high": "Data Unavailable", 
            "daily_low": "Data Unavailable",
            "last_close": "Data Unavailable",
            "change": "Data Unavailable",
            "change_percent": "Data Unavailable",
            "volume": "Data Unavailable"    
        }
        return stock_dict


# Function to return the remaining supply of Gods Unchained genesis chests
def get_chest_supply(contract_address):
    try:
        chest_supply_url = f"https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress={contract_address}&apikey={etherscan_key}"
        chest_response = requests.get(chest_supply_url)
        chest_data = json.loads(chest_response.text)
        chest_supply = chest_data["result"]
        return chest_supply

    # Handle api call failures
    except Exception as e:
        print(e)
        chest_supply = "Data unavailable"
        return chest_supply