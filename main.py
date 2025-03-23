
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

    # Метод для строкового представления объекта
    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа администратора

        # Метод для добавления пользователя
        def add_user(self, user_list, user):
            user_list.append(user)
            print(f"User {user.get_name()} added successfully.")

        # Метод для удаления пользователя
        def remove_user(self, user_list, user_id):
            for user in user_list:
                if user.get_user_id() == user_id:
                    user_list.remove(user)
                    print(f"User with ID {user_id} removed successfully.")
                    return
            print(f"User with ID {user_id} not found.")

            # Метод для строкового представления объекта
            def __str__(self):
                return f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"

        # Создаем список для хранения пользователей
        users = []

        # Создаем обычного пользователя
        user1 = User(1, "John Doe")
        print(user1)

        # Создаем администратора
        admin1 = Admin(2, "Jane Doe")
        print(admin1)

        # Администратор добавляет пользователя
        admin1.add_user(users, user1)

        # Администратор пытается удалить пользователя
        admin1.remove_user(users, 1)

        # Выводим список пользователей
        for user in users:
            print(user)
