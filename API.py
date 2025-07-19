import requests 

def fetch_product_details(query):
    url = f"https://world.openfoodfacts.org/api/v0/product/{query}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == 1:
            product = data["product"]
            return{
                "product_name": product.get("product_name", ""),
                "brands": product.get("brands", ""),
                "ingredients": product.get("ingredients_text", "")
            }
        return None