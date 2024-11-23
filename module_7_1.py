from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open('products.txt', 'r')
        sklad = file.read()
        file.close()
        return sklad

    def add(self,*args):
        file = open('products.txt', 'a')
        priv = list(args)
        for ar in priv:
            if ar.name in self.get_products():
                print(f'Продукт {ar.name} уже есть в магазине')
            else:
                file.write(f'{ar}\n')
        file.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
