import requests

API_URL = "http://127.0.0.1:5000/inventory"

def main():
    while True:
        print("\nInventory CLI")
        print("1. View All Items")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Quit")
        choice = input("Choose an option: ")
       
        if choice == '1':
            r = requests.get(API_URL)
            print(r.json())

        elif choice == '2':
            name = input("Name: ")
            
            try:
                stock = int(input("Stock: "))
            except ValueError:
                print("Invalid stock. Must be an integer.")
                continue

            try:
                price = float(input("Price: "))
            except ValueError:
                print("Invalid price. Must be a number.")
                continue
            
            barcode = input("Barcode: ")
            r = requests.post(API_URL, json={"name": name, "stock": stock, "price": price, "barcode": barcode})
            print("Added:", r.json())

        elif choice == "3":
            id = input("Item ID: ")
            field = input("Field to update (stock/price): ")
            value = input("New Value:")
            value = int(value) if field == "stock" else float(value)
            r = requests.patch(f"{API_URL}/{id}", json={field: value})
            print(r.json())

        elif choice == "4":
            id = input("Item ID to delete: ")
            r = requests.delete(f"{API_URL}/{id}") 
            print("Deleted!" if r.status_code == 204 else r.json())

        elif choice == "5":
            break 

        else: 
            print("Invalid choice")

if __name__== "__main__":
    main()

