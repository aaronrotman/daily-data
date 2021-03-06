# Dependencies
from flask import Flask, render_template

# Import function to return Ethereum gas data
from functions import get_gas_data, get_eth_price, get_stock_data, get_chest_supply, get_address_balance

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

# Gods Unchained route
@app.route('/gods_unchained')
def gu_page():

    # Get Ethereum gas data
    gas_data = get_gas_data()
    print(f"Last Block: {gas_data['last_block']} | Safe Gas Price: {gas_data['safe_gas']} | Propose Gas Price: {gas_data['propose_gas']}")
    
    # Get Ethereum price data
    eth_data = get_eth_price()
    print(f"Ethereum Price: {eth_data['eth_usd']} | Time: {eth_data['time']}")

    # Rare genesis chest contract address
    rare_chest_addr = "0xee85966b4974d3c6f71a2779cc3b6f53afbc2b68"
    # Legendary genesis chest contract address
    legendary_chest_addr = "0x20d4cec36528e1c4563c1bfbe3de06aba70b22b4"
    # Season 1 sales address
    s1_sales_addr = "0xed824e513aff2545af0b6bb11ec2c503560e7672"
    
    # Get rare chest data
    rare_chests = get_chest_supply(rare_chest_addr)

    # Get legendary chest data
    legendary_chests = get_chest_supply(legendary_chest_addr)

    # Get Season 1 total sales data
    s1_sales_total = get_address_balance(s1_sales_addr)
    eth_price = eth_data['eth_usd']
    s1_sales = float(eth_price) * float(s1_sales_total)
    s1_sales_value = f"${s1_sales}"
    
    # Print chest counts
    print(f"Rare Chest Supply: {rare_chests} | Legendary Chest Supply: {legendary_chests} | Total Sales: {s1_sales_total} | Total Sale Value: {s1_sales_value}")

    # Dictionary to store chest counts
    data_dict= {
        "rare": rare_chests,
        "legendary": legendary_chests,
        "s1_sales": s1_sales_total,
        "s1_sales_value": s1_sales_value
    }
    
    # Render the index page template
    return render_template("gu_page.html", meta=meta, data=data_dict, gas=gas_data, eth_data=eth_data)

# NOTE: Set debug=False for production deployment
# Run the application
if __name__ == "__main__":
    app.run(debug=True)


       