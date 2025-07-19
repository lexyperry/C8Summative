inventory = []

def get_all_items():
    return inventory

def get_item_by_id(id):
    return next((item for item in inventory if item["id"] == id), None)

def add_item(item):
    inventory.append(item)

def update_item(id, updates):
    item = get_item_by_id(id)
    if item:
        item.update(updates)
        return item
    return None

def delete_id(id):
    global inventory 
    inventory = [item for item in inventory if item["id"] != id]
    