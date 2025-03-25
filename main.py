
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Гав!"

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Чирик!"

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return "Шшш!"

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee.name}")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name}, возраст: {animal.age} лет")

    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee.name}, должность: {employee.position}")

# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавление животных
    zoo.add_animal(Mammal("Шарик", 5, "коричневый"))
    zoo.add_animal(Bird("Кеша", 2, "50 см"))
    zoo.add_animal(Reptile("Геккон", 1, "зеленый"))

    # Добавление сотрудников
    zoo.add_employee(Employee("Иван", "Дрессировщик"))
    zoo.add_employee(Employee("Мария", "Зоолог"))

    # Показать животных и сотрудников
    zoo.show_animals()
    zoo.show_employees()
