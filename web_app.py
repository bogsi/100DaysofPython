from flask import Flask, render_template, request, jsonify
from car_scraper import CarScraper

app = Flask(__name__)
scraper = CarScraper()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    brand = data.get('brand', '')
    model = data.get('model', '')
    max_price = data.get('max_price')
    
    if max_price:
        max_price = int(max_price)
    
    cars = scraper.search_all(brand, model, max_price)
    
    return jsonify({
        'cars': [
            {
                'title': car.title,
                'price': car.price,
                'url': car.url
            } for car in cars
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)