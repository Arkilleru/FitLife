# Проект FitLife - MVP версия 1.1

# константы
STD_WATER_BALANCE = 30  # мл воды на 1 кг веса
ML_TO_L = 1000  # коэффициент перевода миллилитров в литры


def hello():
    """Приветствие, узнаём имя и возраст."""
    print(
        "Привет! Я твой персональный фитнес-ассистент",
        "Я помогу тебе рассчитать индекс массы тела и норму воды в день.",
        sep='\n', end='\n'
    )

    user_name = input("\nКак я могу к тебе обращаться? ")

    # вдруг пользователь написал себя с маленькой буквы
    user_name = user_name.title()

    user_age = int(input("Сколько тебе лет? (целое число) "))

    # подсказку на возращение нескольких значений дал ИИ
    return user_name, user_age


def get_calc_info(user_name):
    """Собирает информацию нужную для расчёта имт и нормы воды."""
    print(f"\n{user_name}, теперь мне нужно узнать твой вес и рост.")

    # если человек ввёл через , заменяем на .
    user_weight = float(
        input("Вес (в кг, например, 52.8): ").replace(',', '.')
    )

    user_height = float(
        input("Рост (в метрах, например, 1.68) ").replace(',', '.')
    )

    return user_weight, user_height


def calc(user_weight, user_height):
    """Расчёт имт и нормы воды."""
    print("\nРасчёт...", "пик пик пик", sep='\n', end='\n\n')

    bmi = round(user_weight / (user_height ** 2), 1)

    water_ml = user_weight * STD_WATER_BALANCE
    water_l = round(water_ml / ML_TO_L, 1)

    return bmi, water_l


def main():
    """Главная функция, вызывает остальные функции."""
    user_name, user_age = hello()
    user_weight, user_height = get_calc_info(user_name)
    bmi, water_l = calc(user_weight, user_height)

    return user_name, user_age, bmi, water_l


# Точка входа
if __name__ == '__main__':
    user_name, user_age, user_bmi, water_l = main()

    print(
        "Расчёт окончен, сейчас сформирую отчёт.\n",
        f"Имя: {user_name}",
        f"Возраст: {user_age}",
        f"Индекс массы тела: {user_bmi}",
        f"Норма воды в день: {water_l} л.\n",
        f"Отчёт сформирован. Будьте здоровы {user_name}!",
        sep='\n'
    )
