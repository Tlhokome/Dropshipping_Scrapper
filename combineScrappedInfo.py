import pandas as pd

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