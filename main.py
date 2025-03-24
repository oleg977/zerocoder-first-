class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Уникальный идентификатор пользователя
        self._name = name        # Имя пользователя
        self._access_level = 'user'  # Уровень доступа, по умолчанию 'user'

    # Геттеры для получения значений атрибутов
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

        # Сеттеры для изменения значений атрибутов
    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа администратора

            # Метод для добавления пользователя
    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь успешно добавлен.")
        print(user_list)

            # Метод для удаления пользователя
    def remove_user(self, user_list, user):
        user_list.remove(user)
          # Создаем список для хранения пользователей
users = []
admin = Admin(user_id='a1',name='Гоша')
user1 = User(user_id='U1',name='Спепа')
print(user1.get_name())
admin.add_user(users, user1)

