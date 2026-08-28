# Проект FitLife - MVP версия 1.0

# константы
STD_WATER_BALANCE = 30  # мл воды на 1 кг веса
ML_TO_L = 0.001  # коэффициент перевода миллилитров в литры


def hello():
    """приветсвие, узнаём имя и возраст"""
    print("Привет! Я твой персональный фитнес-ассистент")
    print("Я помогу тебе рассчитать индекс массы тела и норму воды в день.\n")

    user_name = input("\nКак я могу к тебе обращаться? ")

    # вдруг пользователь написал себя с маленькой буквы
    user_name = user_name.title()

    # самый старый человек прожил 122 года по официальным данным
    user_age = int(input("Сколько тебе лет? (число в диапазоне 8-122) "))

    # подсказку на возращение нескольких значений дал ИИ
    return user_name, user_age


def get_calc_info(user_name):
    """собирает информацию нужную для расчёта имт и нормы воды"""
    print(f"\n{user_name}, теперь мне нужно узнать твой вес и рост.")

    user_weight = float(input("Вес (в кг через точку, например, 52.8) "))
    user_height = float(input("Рост (в метрах через точку, например, 1.68) "))

    return user_weight, user_height


def calc(user_weight, user_height):
    """расчёт имт и нормы воды"""
    print("\nРасчёт...", "пик пик пик", sep='\n')

    bmi = round(user_weight / (user_height ** 2), 1)

    # в описании формула была через деление
    # но через такой подход может точность пострадать
    water_ml = user_weight * STD_WATER_BALANCE
    water_l = round(water_ml * ML_TO_L, 1)

    return bmi, water_l


def show(user_name, user_age, user_bmi, water_l):
    """вывод результата"""
    print("Расчёт окончен, сейчас сформирую отчёт.\n")

    # разбил на три принта, чтобы не было строк больше 79 символов)
    print(f"Имя: {user_name}", f"Возраст: {user_age}", sep='\n')
    print(f"Индекс массы тела: {user_bmi}")
    print(f"Норма воды в день: {water_l} л.")

    print(f"Отчёт сформирован. Будьте здоровы {user_name}!")


def main():
    """ну поскольку знаю с++ без main никак,
    главная функция, вызывает остальные функции
    """
    user_name, user_age = hello()
    user_weight, user_height = get_calc_info(user_name)
    bmi, water_l = calc(user_weight, user_height)
    show(user_name, user_age, bmi, water_l)


# в питоне маин просто пользовательская функция, поэтому явно вызываю
main()
