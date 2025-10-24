from flask import Flask, render_template, request
from car_scraper import CarScraper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    brand = request.form.get('brand', '').strip()
    model = request.form.get('model', '').strip()
    max_price = request.form.get('max_price', '').strip()
    
    max_price = int(max_price) if max_price else None
    
    scraper = CarScraper()
    cars = scraper.search_mobile_bg(brand, model, max_price)
    
    return render_template('results.html', cars=cars, count=len(cars))

if __name__ == '__main__':
    app.run(debug=True)