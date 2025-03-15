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