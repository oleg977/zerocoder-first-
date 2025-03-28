
from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"

class Axe(Weapon):
    def attack(self):
        return "рубит топором"


class MagicWand(Weapon):
    def attack(self):
        return "кастует заклинание"


# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}.")
        else:
            print(f"{self.name} не имеет оружия!")

            # Класс монстра
class Monster:
    def __init__(self, name):
        self.name = name
        self.is_defeated = False

    def defeat(self):
        self.is_defeated = True
        print(f"{self.name} побежден!")

            # Шаг 4: Механизм боя
def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()
    print()

            # Демонстрация
if __name__ == "__main__":
     hero = Fighter("Боец")
     monster = Monster("Монстр")
     # Бой с мечом
     hero.change_weapon(Sword())
     battle(hero, monster)

     # Бой с луком
     hero.change_weapon(Bow())
     battle(hero, monster)

     # Бой с топором (новое оружие добавлено без изменения существующего кода)
     hero.change_weapon(Axe())
     battle(hero, monster)

     # Бой с волшебной палочкой (новое оружие)
     hero.change_weapon(MagicWand())
     battle(hero, monster)


