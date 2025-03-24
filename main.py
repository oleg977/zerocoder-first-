
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

    def eat(self, food):
        print(f"{self.name} ест {food}.")

# Подкласс для млекопитающих
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Гав!"  # Можно переопределить для разных млекопитающих

# Подкласс для птиц
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Чирик!"

# Подкласс для рептилий
class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "Шшш!"  # Звук, который может издавать рептилия

# Создание объектов животных
def create_animals():
    mammal = Mammal("Шарик", 5, "коричневый")
    bird = Bird("Кеша", 2, "50 см")
    reptile = Reptile("Геккон", 1, "зеленый")

    # Использование методов
    print(f"{mammal.name} говорит: {mammal.make_sound()}")
    mammal.eat("мясо")

    print(f"{bird.name} говорит: {bird.make_sound()}")
    bird.eat("семена")

    print(f"{reptile.name} говорит: {reptile.make_sound()}")
    reptile.eat("насекомые")


# Запуск создания животных
if __name__ == "__main__":
    create_animals()