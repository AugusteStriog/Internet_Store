class Item:
    def __init__(self, id, title, manufacturer, buyer_id, shop_id):
        self.id = id
        self.title = title
        self.manufacturer = manufacturer
        self.buyer_id = buyer_id
        self.shop_id = shop_id

items = [
    Item(1, "Wireless Mouse", "Logitech"),
    Item(2, "Gaming Keyboard", "Corsair"),
    Item(3, "USB-C Charger", "Anker"),
]
