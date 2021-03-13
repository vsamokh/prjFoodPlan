import sqlite3
from sqlite3 import Error
import random
import glob_settings

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
    if glob_settings.lang == "uk": cur.execute(f"SELECT Название_блюда__uk_ FROM 'Блюда' WHERE Код_блюда = {meal_id}")
    elif glob_settings.lang == "ru": cur.execute(f"SELECT Название_блюда_ru_ FROM 'Блюда' WHERE Код_блюда = {meal_id}")
    else: cur.execute(f"SELECT Название_блюда__en_ FROM 'Блюда' WHERE Код_блюда = {meal_id}")
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


"""
def getMealRow(conn, meal_id):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM 'Гарниры' where Код_блюда == {meal_id}
                    UNION
                    SELECT * FROM 'Завтрак'  where Код_блюда == {meal_id}
                    UNION
                    SELECT * FROM 'Мясо-рыба' where Код_блюда == {meal_id}
                    UNION
                    SELECT * FROM 'Основное' where Код_блюда == {meal_id}
                    UNION
                    SELECT * FROM 'Первое' where Код_блюда == {meal_id}
                    UNION
                    SELECT * FROM 'Перекусы' where Код_блюда == {meal_id}
                    UNION
                    SELECT * FROM 'Салат' where Код_блюда == {meal_id}
                ")
    return cur.fetchone()
def getMealId(conn, name_en):
    cur = conn.cursor()
    cur.execute(f"SELECT Код_блюда FROM 'Блюда' WHERE Название_блюда__en_ = '{name_en}'")
    return cur.fetchone()[0]
"""

# Функция, возвращающая идентификатор случайного блюда
def randomMealID(conn, table_name, mealNum):
    cur = conn.cursor()
    # создание части команды запроса для удаления аллергенов
    s = "Алерген = NULL "
    for i in glob_settings.allergyid_list:
        s += f"OR Алерген = {i} "

    # запрос удаляет из выборки блюда с выбранными аллергенами
    # и выбирает 1-й элемент случайно отсортированной полученной таблицы
    cur.execute(f"""
    SELECT Код_блюда FROM (
        SELECT Код_блюда FROM '{table_name}'
        EXCEPT SELECT Блюдо FROM 'Алерген-блюдо' WHERE {s})
    ORDER BY RANDOM() LIMIT {mealNum}""")
    output = cur.fetchall()
    if mealNum == 1:
        return output[0][0]
    else:
        return output[0][0], output[1][0]

# функция для получения id и названия аллергена
def getAllergens(conn):
    cur = conn.cursor()
    cur.execute("SELECT Код_алергена, Алерген FROM 'Алергены'")
    return cur.fetchall()

# Класс, в котором хранятся название блюда и характеристики его нутриентов
class Dish:
    def __init__(self, conn, meal_id):
        self.meal_id = meal_id
        self.name = getMealName(conn, meal_id)
        self.calories = getMealEntryUnknown(conn, "Калории__ккал_", meal_id)
        self.fat = getMealEntryUnknown(conn, "Жиры__г_", meal_id)
        self.proteins = getMealEntryUnknown(conn, "Белки__г_", meal_id)
        self.carbohydrates = getMealEntryUnknown(conn, "Углеводы__г_", meal_id)
        self.cholesterol = getMealEntryUnknown(conn, "Холестерин__мг_", meal_id)
        self.sodium = getMealEntryUnknown(conn, "Натрий__мг_", meal_id)
        self.cellulose = getMealEntryUnknown(conn, "Клетчатка", meal_id)


# Функция, возвращающая список классов Dish для завтрака
def Breakfast(conn):
    a, b = randomMealID(conn, "Завтрак", 2)
    return [Dish(conn, a), Dish(conn, b)]

# Функция, возвращающая список классов Dish для обеда
def Lunch(conn):
    # Вариант компоновки блюд определяется случайно
    if random.choice([True, False]):
        return [Dish(conn, randomMealID(conn, "Первое", 1)), Dish(conn, randomMealID(conn, "Основное", 1))]
    else:
        return [Dish(conn, randomMealID(conn, "Первое", 1)), Dish(conn, randomMealID(conn, "Гарниры", 1)),
                    Dish(conn, randomMealID(conn, "Мясо-рыба", 1)), Dish(conn, randomMealID(conn, "Салат", 1))]

# Функция, возвращающая список классов Dish для ужина
def Dinner(conn):
    if random.choice([True, False]):
        return [Dish(conn, randomMealID(conn, "Основное", 1))]
    else:
        return [Dish(conn, randomMealID(conn, "Гарниры", 1)),
                    Dish(conn, randomMealID(conn, "Мясо-рыба", 1)), Dish(conn, randomMealID(conn, "Салат", 1))]

# Функция, возвращающая список классов Dish для перекуса
def Snack(conn):
    a, b = randomMealID(conn, "Перекусы", 2)
    return [Dish(conn, a), Dish(conn, b)]


"""conn = connect_db("databaseV2.3.db")
glob_settings.glob_init()
glob_settings.lang = "en"
glob_settings.allergyid_list.append(1)
print(randomMealID(conn, "Завтрак"))
print(glob_settings.lang)
print(glob_settings.allergyid_list)
close_db(conn)
"""
