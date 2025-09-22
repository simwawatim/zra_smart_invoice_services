import requests
import json
from django.conf import settings

def send_item_to_smart_invoice(item_data):
    url = 'http://41.60.191.7:4000/sandboxvsdc1.0.8.0/items/saveItem'  
    headers = {
        'Content-Type': 'application/json',
    }
    payload = json.dumps(item_data)

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for non-2xx responses
        return response.json()  # Return parsed JSON response from Smart Invoice
    except requests.exceptions.RequestException as e:
        # Handle any exceptions from the request (network error, API issues)
        return {"error": str(e)}
