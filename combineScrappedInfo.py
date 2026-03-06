import pandas as pd
import re 

# Read the 2 scrapers' outputs
nike = pd.read_csv('scrapers/nike_shoes.csv')
bash = pd.read_csv('scrapers/bash_shoes.csv')

# Combines them
combined = pd.concat([nike, bash], ignore_index=True)

# Saves them in root folder
combined.to_csv('shoes.csv', index=False)

print(f" Combined {len(combined)} shoes")
print(f"   Nike: {len(nike)}")
print(f"   Bash: {len(bash)}")
print(" Saved to shoes.csv")

def parse_price(price_str):
    #the function removes 'R', spaces, and handles both comma and period as decimal/thousands separators
    cleaned = re.sub(r'[R\s]', '', str(price_str)) # Remove 'R' and whitespaces
    if ',' in cleaned and '.' not in cleaned:
        cleaned = cleaned.replace(',', '.')  # Nike-style: comma is decimal
    else:
        cleaned = cleaned.replace(',', '')   # Bash-style: comma is thousands
    try:
        return float(cleaned)
    except ValueError:
        return None

def calculate_runner_fee(sale_price_float):
    #calculates the runner fee based on the sale price using the provided tiered structure. 
    # If the sale price is None, it returns 0. 
    # For prices above 4000, it calculates 30% of the sale price as the runner fee.
    if sale_price_float is None:
        return 0
    if sale_price_float <= 100:
        return 60
    elif sale_price_float <= 200:
        return 100
    elif sale_price_float <= 300:
        return 130
    elif sale_price_float <= 500:
        return 150
    elif sale_price_float <= 700:
        return 200
    elif sale_price_float <= 900:
        return 250
    elif sale_price_float <= 1100:
        return 300
    elif sale_price_float <= 1400:
        return 350
    elif sale_price_float <= 1700:
        return 400
    elif sale_price_float <= 2000:
        return 450
    elif sale_price_float <= 2300:
        return 500
    elif sale_price_float <= 2700:
        return 550
    elif sale_price_float <= 3000:
        return 600
    elif sale_price_float <= 3400:
        return 650
    elif sale_price_float <= 3700:
        return 700
    elif sale_price_float <= 4000:
        return 750
    else:
        return round(sale_price_float * 0.30)  

combined = pd.read_csv('shoes.csv')

# Parse the raw 'Sale price' strings into clean floats for arithmetic
combined['sale_price_float'] = combined['Sale price'].apply(parse_price)

#Use the float price to determine the runner fee tier for each shoe
combined['runner_fee'] = combined['sale_price_float'].apply(calculate_runner_fee)

#Add the runner fee to the sale price to get the final ShoeBox price
# apply() is used here instead of a single column because we need two columns
# at once (sale_price_float + runner_fee). axis=1 tells pandas to go row by row.
# The result is formatted as a SA Rand string e.g. "R1 299.95"
combined['shoebox_price'] = combined.apply(
    lambda row: f"R{row['sale_price_float'] + row['runner_fee']:,.2f}".replace(',', ' ')
    if row['sale_price_float'] is not None else 'N/A',
    axis=1
)

#Delete the intermediate float column as it's no longer needed and we want to keep the final CSV clean with only the original columns plus runner_fee and shoebox_price.
combined.drop(columns=['sale_price_float'], inplace=True)

combined.to_csv('shoes.csv', index=False)
print(" ETL complete — runner_fee and shoebox_price columns added to shoes.csv")
print("Next, run python app.py")