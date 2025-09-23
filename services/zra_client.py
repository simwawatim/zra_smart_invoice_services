import requests
import json


class SmartInvoiceClient:
    def __init__(self, base_url=None, internal_url=None):
        self.base_url = base_url or "http://41.60.191.7:4000/sandboxvsdc1.0.8.0"
        self.internal_url = internal_url or "http://41.60.191.7:4002"
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
        

    def _get(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        try:
            response =  requests.get(url=url, headers= self.headers, json=data)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def _get_codes(self, endpoint, value):
        url = f"{self.internal_url}/{endpoint}/{value}/"
        try:
            response = requests.get(url=url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_country_code(self, country_name: str):
        return self._get_codes("country", country_name.upper())

    def get_unit_of_measure(self, code: str):
        return self._get_codes("unitofmeasure", code)

    def get_packaging_unit_code(self, code: str):
        return self._get_codes("packaging-unit-code", code)

    def save_item(self, item_data):
        return self._post("items/saveItem", item_data)

    def save_stock(self, stock_data):
        return self._post("stock/saveStockItems", stock_data)
    
    def save_stock_master(self, stock_master_data):
        return self._post("stockMaster/saveStockMaster", stock_master_data)
    
    def save_sale(self, sale_data):
        return self._post("trnsSales/saveSales", sale_data)
    

    def get_customer(self, customer_data):
        return self._post("customers/selectCustomer", customer_data)
    
    def save_branch_customer(self, customer_data):
        return self._post("branches/saveBrancheCustomers", customer_data)
    
    def get_purchases(self, purchase_data):
        return self._post("/trnsPurchase/selectTrnsPurchaseSales", purchase_data)
    
    def save_purchase(self, purchase_data):
        return self._post("trnsPurchase/savePurchase", purchase_data)