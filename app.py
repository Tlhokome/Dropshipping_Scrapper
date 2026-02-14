#from flask import Flask, jsonify, render_template, request
#import pandas as pd
#app = Flask(__name__)
#@app.route('/')
#def index():
#    df = pd.read_csv('shoes.csv')
#    shoes = df.to_dict('records')
#    return render_template('index.html', shoes=shoes)
#if __name__ == '__main__':
#    app.run(debug=True)


#Things to fix: 
#1. Redesign the website and understand how it works because I clearly got something wrong
#2. Fix some links and information that is not showing up on the website
#3. Make the website tailored to Ausi Kani's business.
#4. Add Adidas Scrapped data
#5. Fix image sizes and ensure everything is displayed properly on the website.
#6. Write a readme file to explain how to run the project, what it does, how to use it and the problems I encountered and how I solved them.
#7. Deploythe website on Heroku or any other hosting platform 
#8. Upload the project to GitHub and share the link with Ausi Kani.

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read the combined CSV
    df = pd.read_csv('shoes.csv')
    
    # Simple column rename for template
    df = df.rename(columns={
        'Shoe name': 'name',
        'Sale price': 'sale_price',
        'Original price': 'original_price',
        'Discount percentage': 'discount',
        'More info': 'link',
        'Shoe picture': 'image'
    })
    
    # Add source (Nike or Bash)
    def get_source(url):
        if 'nike.com' in str(url).lower():
            return 'Nike'
        elif 'bash.com' in str(url).lower():
            return 'Bash'
        return 'Other'
    
    df['source'] = df['link'].apply(get_source)
    
    # Convert to dict for template
    shoes = df.to_dict('records')
    
    return render_template('index.html', shoes=shoes)

if __name__ == '__main__':
    app.run(debug=True)