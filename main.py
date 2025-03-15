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

if __name__ == "__main__":
    manager = ProductManager()

    product1 = Product("Jabuka", 15, 20)
    product2 = Product("Banana", 20, 30)
    product3 = Product("Kivi", 35, 40)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    manager.remove_product_by_name("Jabuka")

    manager.display_all_products()
    manager.total_value_of_all_products()