import sqlite3
from sqlite3 import Error
import random

# Функция для подключения базы данных
def connect_db(file_name):
    conn = None
    try:
        conn = sqlite3.connect(file_name)
    # Провера наличия ошибкок при подключении базы данных
    except Error as e:
        print(e)
    return conn

# Функция для закрытия соединения с базой данных
def close_db(conn):
    conn.close()

# Функция, возвращающая название блюда
def getMealName(conn, meal_id):
    # Создание курсора
    cur = conn.cursor()
    # Исполнение запроса
    cur.execute(f"SELECT Название_блюда FROM 'Блюда' WHERE Код_блюда = {meal_id}")
    # функция возвращает 0-й элемент списка (список элементов рядка запроса)
    return cur.fetchone()[0]


"""def getMealEntry(conn, table_name, table_field, meal_id):
    cur = conn.cursor()
    cur.execute(f"SELECT {table_field} FROM '{table_name}' WHERE Код_блюда = {meal_id}")
    return cur.fetchone()[0]"""

# Функция, возвращающая запись количества нутриентов блюда
def getMealEntryUnknown(conn, table_field, meal_id):
    cur = conn.cursor()
    # Запрос поиска записи в заданном поле таблицы, заданного по идентификатору блюда рядка
    cur.execute(f"""SELECT {table_field} FROM 'Гарниры' where Код_блюда == {meal_id}
                    UNION
                    SELECT {table_field} FROM 'Завтрак'  where Код_блюда == {meal_id}
                    UNION
                    SELECT {table_field} FROM 'Мясо-рыба' where Код_блюда == {meal_id}
                    UNION
                    SELECT {table_field} FROM 'Основное' where Код_блюда == {meal_id}
                    UNION
                    SELECT {table_field} FROM 'Первое' where Код_блюда == {meal_id}
                    UNION
                    SELECT {table_field} FROM 'Перекусы' where Код_блюда == {meal_id}
                    UNION
                    SELECT {table_field} FROM 'Салат' where Код_блюда == {meal_id}
                """)
    return cur.fetchone()[0]

# Функция, возвращающая идентификатор случайного блюда
def randomMealID(conn, table_name):
    cur = conn.cursor()
    # запрос выбирает 1-й элемент случайно отсортированной таблицы
    cur.execute(f"SELECT Код_блюда FROM '{table_name}' ORDER BY RANDOM() LIMIT 1;")
    return cur.fetchone()[0]

# Класс, в котором хранятся название блюда и характеристики его нутриентов
class Dish:
    def __init__(self, conn, meal_id):
        self.name = getMealName(conn, meal_id)
        self.calories = getMealEntryUnknown(conn, "Калории__ккал_", meal_id)
        self.fat = getMealEntryUnknown(conn, "Жиры__г_", meal_id)
        self.proteins = getMealEntryUnknown(conn, "Белки__г_", meal_id)
        self.carbohydrates = getMealEntryUnknown(conn, "Углеводы__г_", meal_id)
        self.sugar = getMealEntryUnknown(conn, "Сахар_г_", meal_id)
        self.cholesterol = getMealEntryUnknown(conn, "Холестерин__мг_", meal_id)
        self.alcohol = getMealEntryUnknown(conn, "Алкоголь__г_", meal_id)
        self.caffeine = getMealEntryUnknown(conn, "Холестерин__мг_", meal_id)
        self.sodium = getMealEntryUnknown(conn, "Натрий__мг_", meal_id)
        self.cellulose = getMealEntryUnknown(conn, "Клетчатка", meal_id)
        self.A = getMealEntryUnknown(conn, "Витамин_А__IU_", meal_id)
        self.B1 = getMealEntryUnknown(conn, "Витамин_В1__мг_", meal_id)
        self.B6 = getMealEntryUnknown(conn, "Витамин_В6__мг_", meal_id)
        self.B12 = getMealEntryUnknown(conn, "Витамин_В12__IU_", meal_id)
        self.C = getMealEntryUnknown(conn, "Витамин_С__мг_", meal_id)
        self.D = getMealEntryUnknown(conn, "Витамин_Д__IU_", meal_id)
        self.E = getMealEntryUnknown(conn, "Витамин_Е__мг_", meal_id)
        self.K = getMealEntryUnknown(conn, "Витамин_К__мкг_", meal_id)
        self.calcium = getMealEntryUnknown(conn, "Кальций__мг_", meal_id)
        self.iron = getMealEntryUnknown(conn, "Железо__мг_", meal_id)
        self.magnesium = getMealEntryUnknown(conn, "Магний__мг_", meal_id)
        self.zinc = getMealEntryUnknown(conn, "Цинк_мг_", meal_id)

# Функция, возвращающая список классов Dish для завтрака
def Breakfast(conn):
    return [Dish(conn, randomMealID(conn, "Завтрак"))]

# Функция, возвращающая список классов Dish для обеда
def Lunch(conn):
    # Вариант компоновки блюд определяется случайно
    if random.choice([True, False]):
        return [Dish(conn, randomMealID(conn, "Первое")), Dish(conn, randomMealID(conn, "Основное"))]
    else:
        return [Dish(conn, randomMealID(conn, "Первое")), Dish(conn, randomMealID(conn, "Гарниры")),
                    Dish(conn, randomMealID(conn, "Мясо-рыба")), Dish(conn, randomMealID(conn, "Салат"))]

# Функция, возвращающая список классов Dish для ужина
def Dinner(conn):
    if random.choice([True, False]):
        return [Dish(conn, randomMealID(conn, "Основное"))]
    else:
        return [Dish(conn, randomMealID(conn, "Гарниры")),
                    Dish(conn, randomMealID(conn, "Мясо-рыба")), Dish(conn, randomMealID(conn, "Салат"))]

# Функция, возвращающая список классов Dish для перекуса
def Snack(conn):
    return [Dish(conn, randomMealID(conn, "Перекусы"))]


"""class DishList:
    def __init__(self): pass

    def Breakfast(self, conn):
        return [Dish(conn, randomMealID(conn, "Завтрак"))]

    def Lunch(self, conn):
        if random.choice([True, False]):
            return [Dish(conn, randomMealID(conn, "Первое")), Dish(conn, randomMealID(conn, "Основное"))]
        else:
            return [Dish(conn, randomMealID(conn, "Первое")), Dish(conn, randomMealID(conn, "Гарниры")),
                    Dish(conn, randomMealID(conn, "Мясо-рыба")), Dish(conn, randomMealID(conn, "Салат"))]

    def Dinner(self, conn):
        if random.choice([True, False]):
            return [Dish(conn, randomMealID(conn, "Основное"))]
        else:
            return [Dish(conn, randomMealID(conn, "Гарниры")),
                    Dish(conn, randomMealID(conn, "Мясо-рыба")), Dish(conn, randomMealID(conn, "Салат"))]

    def Snack(self, conn):
        return [Dish(conn, randomMealID(conn, "Перекусы"))]
"""

conn = connect_db("database12.db")

"""print(getMealName(conn, 98))
print(getMealEntryUnknown(conn, "Калории__ккал_", 10))

a1 = Dish(conn, 10)
print(a1.name, a1.calories)"""
print(Breakfast(conn)[0].name)

close_db(conn)