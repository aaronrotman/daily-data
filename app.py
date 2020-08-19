# Dependencies
from flask import Flask, render_template
# import requests
# import json
# from config import etherscan_key

# Import function to return Ethereum gas data
from functions import get_gas_data, get_eth_price, get_stock_data

meta = {
    "title": "Daily Data",
    "headline": "Daily Data"
}

# Instantiate Flask
app = Flask(__name__)

# Index route
@app.route('/')
def index():

    # Get Ethereum gas data
    gas_data = get_gas_data()
    print(f"Last Block: {gas_data['last_block']} | Safe Gas Price: {gas_data['safe_gas']} | Propose Gas Price: {gas_data['propose_gas']}")
    
    # Get Ethereum price data
    eth_data = get_eth_price()
    print(f"Ethereum Price: {eth_data['eth_usd']} | Time: {eth_data['time']}")
    
    # Get stock market price data for Vanguard Total Stock Market ETF (VTI)
    stock_data = get_stock_data("vti")
    print(f"{stock_data['ticker']}: {stock_data['price']}")

    # Get bond market price data for Vanguard Total Bond Market ETF (BND)
    bond_data = get_stock_data("bnd")
    print(f"{bond_data['ticker']}: {bond_data['price']}")

    # Render the index page template
    return render_template("index.html", meta=meta, gas=gas_data, eth_data=eth_data, stock_data=stock_data, bond_data=bond_data)



# Allows the script to run from the command line
if __name__ == "__main__":
    app.run(debug=True)


       