
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Инициализируем пустой словарь для товаров

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} Добавляем с ценой {price:.2f} рублей")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f" Товар {item_name} удалён")#
        else:
            print(f"Товар {item_name} не найден ")

    def get_price(self, item_name):
        return self.items.get(item_name, None)  # Возвращаем цену или None, если товара нет

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            old_price = self.items[item_name]
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} обновлена с {old_price:.2f} руб до {new_price:.2f} руб")#
        else:
            print(f"Товар {item_name} не найден для обновления цены")
    def display_items(self):
        if self.items:
            print(f"Список товаров в магазине:")
            for item_name,price in self.items.items():
                print(f"- {item_name}: {price:.2f} руб")
        else:
            print("Список товаров пуст")


store = Store("Ромашка", "улица Пушкина 10")
store.add_item("Яблоко", 0.5)
store.add_item("Банан", 0.9)
store.add_item("Масло",0.98)
store.add_item("Перец", 4.1)
store.add_item("Груша", 7.4)
print(store.get_price("Яблоко"))
store.update_price("Яблоко", 0.8)
print(store.get_price("Яблоко"))
store.remove_item("Банан")
print(store.get_price("Банан"))
