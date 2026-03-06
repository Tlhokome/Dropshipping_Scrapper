from bs4 import BeautifulSoup
import requests
import pandas as pd

start_page = 1 #the first page to scrape
end_page = 3 #the last page to scrape (inclusive)

headers = {'User-Agent': 'Mozilla/5.0...'} 
base_url = 'https://bash.com/s?filter=category-2:shoes&sort=OrderByReleaseDateDESC&persistentFilter=productClusterIds%3A2526&page={page_num}'

shoes_data = [] #stores all scraped shoe data across pages 
for page_num in range(start_page, end_page + 1):
    url = base_url.format(page_num=page_num)
    print(f"\nScraping page {page_num}: {url}\n")

    try:
        html_text = requests.get(url, headers=headers).text

    except Exception as e:
        print(f"Failed to fetch page {page_num}: {e}")
        continue

    soup = BeautifulSoup(html_text, 'lxml') 
    shoes = soup.find_all('div', class_ = 'relative h-full w-full cursor-pointer rounded-md text-onyx-Black z-0 p-0')

    for i, shoe in enumerate(shoes): 
        try:    
            shoe_name = None
            shoe_link = None
            shoe_salePrice = None
            shoe_originalPrice = None
            percentOff = None
            shoe_image = None

            anchor = shoe.find('a', class_ = 'text-onyx-Black block w-full leading-4 no-underline')
            if anchor: #this condition checks if anchor is not None because it could happen that it is
                shoe_name = anchor.text.strip()
                link = anchor.get('href')
                if link:
                    shoe_link = 'https://www.bash.com' + link
        
            prices  = shoe.find('div', class_ = 'flex flex-wrap gap-1 overflow-hidden self-start w-full text-sm font-semibold')
            if prices:
                spans = prices.find_all('span')
                if len(spans) >= 3:
                    shoe_salePrice = spans[0].text.strip()  
                    shoe_originalPrice = spans[1].text.strip() 
                    percent = spans[2].text.strip()
                    percentOff = percent + ' off'

            image = shoe.find('img', class_ = 'aspect-portrait absolute z-[9] w-full rounded object-cover')
            if image:
                shoe_image = image['src']
        
            shoe_data = {
                'Shoe name': shoe_name,
                'Sale price': shoe_salePrice,
                'Original price': shoe_originalPrice,
                'Discount percentage': percentOff,
                'More info': shoe_link,
                'Shoe picture': shoe_image
            }
            shoes_data.append(shoe_data)   

            print(f"""
                Shoe name: {shoe_name}
                Discount price: {shoe_salePrice}
                Original price: {shoe_originalPrice}
                Discount percentage: {percentOff}
                More info: {shoe_link}      
                Shoe picture: {shoe_image}
            """)

        except Exception as e:
            print(f"Error scrapping shoe {i}: {e}")
            continue    

df = pd.DataFrame(shoes_data)
df.to_csv('scrapers/bash_shoes.csv', index=False)
print(f'\n Saved {len(shoes_data)} Bash shoes to bash_shoes.csv')
print('Next, run python combineScrappedInfo.py')


