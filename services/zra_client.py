import requests
import json
from django.conf import settings


class SmartInvoiceClient:
    def __init__(self, base_url=None):
        self.base_url = "http://41.60.191.7:4000/sandboxvsdc1.0.8.0"
        self.headers = {
            "Content-Type": "application/json"
        }

    def _post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def save_item(self, item_data):
        """Save a single item to Smart Invoice"""
        return self._post("items/saveItem", item_data)

    def save_stock(self, stock_data):
        """Save stock details to Smart Invoice"""
        return self._post("/stock/saveStockItems", stock_data)
