from flask import Flask, render_template, request
import pandas as pd
import math

app = Flask(__name__)

# Number of items to display per page
PER_PAGE = 30

@app.route('/')
def index():
    # Get current page from query string (e.g., ?page=2). Default to 1.
    # get() - it looks for the 'page' parameter in the URL query string. 
    # If it doesn't find it, it defaults to 1. 
    # The type=int part ensures that the value is converted to an integer.
    
    # it will later be used to determine which subset of the shoe data to display on the webpage, allowing for pagination of the shoe listings.
    # For example, if the URL is http://localhost:5000/?page=2, then page will be set to 2. If the URL does not include a page parameter, it will default to 1.
    page = request.args.get('page', 1, type=int)

    # Read the combined CSV
    df = pd.read_csv('shoes.csv')

    # Simple column rename for template
    df = df.rename(columns={
        'Shoe name': 'name',
        'Sale price': 'sale_price',
        'Original price': 'original_price',
        'Discount percentage': 'discount',
        'More info': 'link',
        'Shoe picture': 'image',
        'runner_fee': 'runner_fee',       
        'shoebox_price': 'shoebox_price'  
    })

    # Add source (Nike or Bash) for easy redirecting
    def get_source(url):
        if 'nike.com' in str(url).lower():
            return 'Nike'
        elif 'bash.com' in str(url).lower():
            return 'Bash'
        return 'Other'

    df['source'] = df['link'].apply(get_source)

    #Pagination logic:
    total_items = len(df)
    total_pages = math.ceil(total_items / PER_PAGE) if total_items > 0 else 1

    # Ensures page is within valid range
    if page < 1:
        page = 1
    elif page > total_pages and total_pages > 0: #this prevents the website from having pages that exceed the number of items, that is we dont want blank pages with items
        page = total_pages

    #Calculate start and end indices for the current page
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE

    # Slice the DataFrame to get only the rows for this page
    df_page = df.iloc[start:end]

    #Convert the page's DataFrame rows to a list of dictionaries for the template
    shoes = df_page.to_dict('records')
    

    return render_template(
        'index.html',
        shoes=shoes,
        page=page,
        total_pages=total_pages,
        per_page=PER_PAGE
    )

if __name__ == '__main__':
    app.run(debug=True)

