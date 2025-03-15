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