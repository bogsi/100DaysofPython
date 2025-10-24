import requests
from bs4 import BeautifulSoup
import time
from typing import List

class Car:
    def __init__(self, title, price, year, mileage, location, url):
        self.title = title
        self.price = price
        self.year = year
        self.mileage = mileage
        self.location = location
        self.url = url

class CarScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.base_url = "https://www.mobile.bg"

    def search_mobile_bg(
        self, brand: str = "", model: str = "", max_price: int = None
    ) -> List[Car]:
        """Търси коли в mobile.bg"""
        cars = []
        url = f"{self.base_url}/pcgi/mobile.cgi"

        params = {
            "act": "3",
            "slink": "rnhfqr",
        }

        if brand:
            params["f1"] = brand
        if model:
            params["f2"] = model
        if max_price:
            params["f5"] = str(max_price)

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            for row in soup.find_all("tr", {"onmouseover": True}):
                cols = row.find_all("td")
                if len(cols) < 6:
                    continue

                link_elem = cols[1].find("a")
                if not link_elem:
                    continue

                title = link_elem.text.strip()
                price = cols[2].text.strip() or "Не е посочена"
                year = cols[3].text.strip() or "-"
                mileage = cols[4].text.strip() or "-"
                location = cols[5].text.strip() or "-"

                car_url = link_elem.get("href")
                if car_url and not car_url.startswith("http"):
                    car_url = f"{self.base_url}{car_url}"

                if title and car_url:
                    cars.append(Car(title, price, year, mileage, location, car_url))

        except Exception as e:
            print(f"⚠️ Грешка при извличане от mobile.bg: {e}")

        return cars

    def search_all(self, brand: str = "", model: str = "", max_price: int = None) -> List[Car]:
        """Търси във всички сайтове"""
        all_cars = []

        print("Търсене в mobile.bg...")
        cars = self.search_mobile_bg(brand, model, max_price)
        print(f"Намерени {len(cars)} коли в mobile.bg")
        return cars

    def search_auto_bg(self, brand: str = "", model: str = "", max_price: int = None) -> List[Car]:
        """Placeholder за auto.bg търсене"""
        return []

def main():
    scraper = CarScraper()
    
    # Примерно търсене
    brand = input("Марка (или Enter за всички): ").strip()
    model = input("Модел (или Enter за всички): ").strip()
    max_price_input = input("Максимална цена (или Enter за без лимит): ").strip()
    
    max_price = int(max_price_input) if max_price_input else None
    
    cars = scraper.search_all(brand, model, max_price)
    
    print(f"\nНамерени {len(cars)} коли:")
    for i, car in enumerate(cars[:10], 1):  # Показва първите 10
        print(f"{i}. {car.title} - {car.price}")
        print(f"   URL: {car.url}\n")

if __name__ == "__main__":
    main()
