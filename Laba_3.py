# 1. List comprehension (простое преобразование)
squares = [x**2 for x in range(1, 11)]
print("1. Квадраты чисел от 1 до 10:", squares)

# 2. List comprehension (фильтрация)
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print("2. Чётные числа от 1 до 20:", even_numbers)

# 3. List comprehension (работа со строками)
words = ["python", "Java", "c++", "Rust", "go"]
filtered_words = [word.upper() for word in words if len(word) > 3]
print("3. Слова в верхнем регистре длиннее 3 символов:", filtered_words)

# 4. Собственный итератор
class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n == 0:
            raise StopIteration
        current = self.n
        self.n -= 1
        return current

print("4. Итератор Countdown:")
for x in Countdown(5):
    print(x, end=" ")
print()

# 5. Собственный генератор
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("5. Первые 5 чисел Фибоначчи:")
for num in fibonacci(5):
    print(num, end=" ")
print()

# 6. Decimal (точные вычисления)
from decimal import Decimal, getcontext

def deposit_calculator():
    # Устанавливаем точность вычислений
    getcontext().prec = 10
    
    # Ввод данных
    P = Decimal(input("Введите начальную сумму вклада: "))
    r = Decimal(input("Введите годовую процентную ставку: "))
    t = Decimal(input("Введите срок вклада в годах: "))
    
    # Расчет по формуле
    S = P * (1 + r / (12 * 100)) ** (12 * t)
    
    # Округление до копеек
    S_rounded = S.quantize(Decimal('0.01'))
    profit = S_rounded - P
    
    print(f"Итоговая сумма вклада: {S_rounded} руб.")
    print(f"Общая прибыль: {profit} руб.")

print("6. Финансовый калькулятор:")
deposit_calculator()

# 7. Fraction (рациональные дроби)
from fractions import Fraction

frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

addition = frac1 + frac2
subtraction = frac1 - frac2
multiplication = frac1 * frac2
division = frac1 / frac2

print("7. Операции с дробями:")
print(f"3/4 + 5/6 = {addition}")
print(f"3/4 - 5/6 = {subtraction}")
print(f"3/4 × 5/6 = {multiplication}")
print(f"3/4 ÷ 5/6 = {division}")

# 8. DateTime (текущая дата и время)
from datetime import datetime

now = datetime.now()
print("8. Текущая дата и время:")
print(f"Текущая дата и время: {now}")
print(f"Только текущая дата: {now.date()}")
print(f"Только текущее время: {now.time()}")

# 9. DateTime (разница дат)
from datetime import date

def birthday_calculator():
    birth_year = int(input("Введите год рождения: "))
    birth_month = int(input("Введите месяц рождения: "))
    birth_day = int(input("Введите день рождения: "))
    
    birthday = date(birth_year, birth_month, birth_day)
    today = date.today()
    
    # Прошло дней с рождения
    days_passed = (today - birthday).days
    
    # Следующий день рождения
    next_birthday = date(today.year, birth_month, birth_day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_month, birth_day)
    
    days_to_next = (next_birthday - today).days
    
    print(f"С момента рождения прошло: {days_passed} дней")
    print(f"До следующего дня рождения: {days_to_next} дней")

print("9. Расчет дней:")
birthday_calculator()

# 10. DateTime (форматирование строк)
def format_datetime(dt):
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    
    return f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt.strftime('%H:%M')}"

print("10. Форматирование даты:")
print(format_datetime(datetime.now()))