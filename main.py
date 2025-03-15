class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def metod_info(self):
        print(f"Proizvod: {self.name}")
        print(f"Cena: {self.price} RSD")
        print(f"Količina: {self.quantity} kom")

    def metod_update_kolicina(self, new_quantity):
        self.quantity = new_quantity
        print(f"Nova količina {self.name} je {self.quantity}.")

    def total_value(self):
        return self.price * self.quantity


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod '{product.name}' je dodat.")

    def display_all_products(self):
        if not self.products:
            print("Nema proizvoda u listi.")
            return
        print("Lista svih proizvoda:")
        for product in self.products:
            product.metod_info()
            print()

    def total_value_of_all_products(self):
        total_value = sum(product.total_value() for product in self.products)
        print(f"Ukupna vrednost: {total_value} RSD")
    
    def remove_product_by_name(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]
        print(f"Proizvodi '{product_name}' je uklonjen.")

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_item_to_cart(self, product, quantity):
        product_copy = Product(product.name, product.price, quantity)
        self.cart_items.append(product_copy)
        print(f"Proizvod '{product.name}' je dodat u korpu. Količina: {quantity}")

    def total_value_of_cart(self):
        total_value = sum(item.total_value() for item in self.cart_items)
        print(f"Ukupna vrednost korpe: {total_value} RSD")

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        print("U korpi:")
        for item in self.cart_items:
            item.metod_info()
            print()

    def remove_item_from_cart(self, product_name):
        initial_count = len(self.cart_items)
        self.cart_items = [item for item in self.cart_items if item.name != product_name]
        if len(self.cart_items) < initial_count:
            print(f"Proizvod '{product_name}' je uklonjen iz korpe.")
        else:
            print(f"Proizvod '{product_name}' nije pronađen u korpi.")

if __name__ == "__main__":
    manager = ProductManager()

    product1 = Product("Jabuka", 15, 20)
    product2 = Product("Banana", 20, 30)
    product3 = Product("Kivi", 35, 40)
    product4 = Product("Krska", 15, 15)



    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    manager.remove_product_by_name("Jabuka")

    manager.display_all_products()
    manager.total_value_of_all_products()

    cart = Cart()

    cart.add_item_to_cart(product1, 5)
    cart.add_item_to_cart(product4, 7)
    cart.add_item_to_cart(product3, 2)

    cart.display_cart()
    cart.total_value_of_cart()

    cart.remove_item_from_cart("Banana")
    cart.display_cart()
    cart.total_value_of_cart()
