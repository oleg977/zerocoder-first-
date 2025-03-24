
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

    def eat(self, food):
        print(f"{self.name} ест {food}.")
class Cat(Animal):
    def make_sound(self):
        return "Мяу!"
class Dog(Animal):
    def make_sound(self):
        return "Гав!"

cat = Cat("Барсик", 3)
dog = Dog("Шарик", 5)

# Использование методов
print(f"{cat.name} говорит: {cat.make_sound()}")
cat.eat("рыбу")

print(f"{dog.name} говорит: {dog.make_sound()}")
dog.eat("мясо")