#import pandas as pd

# Read individual scraper outputs
#nike = pd.read_csv('scrapers/nike_shoes.csv')
#bash = pd.read_csv('scrapers/bash_shoes.csv')
#adidas = pd.read_csv('scrapers/adidas_output.csv')
#combine 2 sites
#combined = pd.concat([nike, bash], ignore_index=True)
# Combine all 3
#combined = pd.concat([nike, adidas, shein], ignore_index=True)
# Save master file for Flask
#combined.to_csv('shoes.csv', index=False)
#print(f"Combined {len(combined)} shoes from 2 sites into shoes.csv")

import pandas as pd

# Read the scraper outputs
nike = pd.read_csv('scrapers/nike_shoes.csv')
bash = pd.read_csv('scrapers/bash_shoes.csv')

# Combine them
combined = pd.concat([nike, bash], ignore_index=True)

# Save to root folder
combined.to_csv('shoes.csv', index=False)

print(f" Combined {len(combined)} shoes")
print(f"   Nike: {len(nike)}")
print(f"   Bash: {len(bash)}")
print(" Saved to shoes.csv")