from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0...'} 
html_text = requests.get('https://www.nike.com/za/w/mens-sale-shoes-3yaepznik1zy7ok', headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')

shoes_data = [] #List to store all scrapped shoe info
shoes = soup.find_all('div', class_ = 'product-card__body')

for i, shoe in enumerate(shoes): #note enumerate() add a counter(default is 0) to an iterable variable and returns a enumerate obj, that is a tuple (index, value_of_iterable)
    try:    
        shoe_name = shoe.find('div', class_ = 'product-card__title').text
        shoe_salePrice = shoe.find('div', class_ = 'product-price is--current-price css-1mj7kho').text.strip() if shoe.find('div', class_ = 'product-price is--current-price css-1mj7kho') else 'No sale price'
        shoe_originalPrice = shoe.find('div', class_ = 'product-price za__styling is--striked-out css-0').text.strip() if shoe.find('div', class_ = 'product-price za__styling is--striked-out css-0') else 'No original price'
        percent = shoe.find('div', class_ = 'product-price__perc css-hkd8g8').text.strip() if shoe.find('div', class_ = 'product-price__perc css-hkd8g8') else 'No discount'
        percentOff = '-' + percent 
        anchor = shoe.find('a', class_ = 'product-card__img-link-overlay')
        shoeLink = anchor['href'] if anchor else 'No link found'
        image = shoe.find('img', class_ = 'product-card__hero-image css-1fxh5tw')
        shoeImage = image['src'] if image else 'No image found'

        print(f''' 
            Shoe name: {shoe_name}
            Sale price: {shoe_salePrice}
            Original price: {shoe_originalPrice}
            Discount percentage: {percentOff}
            More info: {shoeLink}
            Shoe picture: {shoeImage}''')

        shoe_data = {
            'Shoe name': shoe_name,
            'Sale price': shoe_salePrice,
            'Original price': shoe_originalPrice,
            'Discount percentage': percentOff,
            'More info': shoeLink,
            'Shoe picture': shoeImage
        }
        shoes_data.append(shoe_data)
        
    except Exception as e:
        print(f"Error scrapping shoe {i}: {e}")
        continue
 
 
df = pd.DataFrame(shoes_data)
df.to_csv('scrapers/nike_shoes.csv', index=False)
print(f'\n Saved {len(shoes_data)} Nike shoes to nike_shoes.csv')
print('Next, run python combineScrappedInfo.py')