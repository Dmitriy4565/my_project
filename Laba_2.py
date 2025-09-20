# print("Таблица умножения:")
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i*j:3}", end=" ") #3 значит ширина в 3 символа
#     print()



# 2. Сумма всех нечётных чисел от 1 до 100
# odd_sum = sum(i for i in range(1, 101) if i % 2 != 0)
# print(f"Сумма нечётных чисел от 1 до 100: {odd_sum}")


# # 3. Делители числа n
# n = int(input("Введите число n: "))
# print(f"Делители числа {n}: ", end="")
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=" ")

# # 4. Факториал числа
# number = int(input("Введите число для факториала: "))
# fact = 1
# for i in range(1, number+1):
#     fact *= i
# print(f"Факториал числа {number} = {fact}")


# # 5. Последовательность Фибоначчи
# k = int(input("Введите длину последовательности Фибоначчи: "))
# fib = [0, 1]
# for i in range(2, k):
#     fib.append(fib[-1] + fib[-2])
# print("Последовательность Фибоначчи:", fib)

import random

# 0. Генерация списка из 10 случайных чисел от -50 до 50
numbers = [random.randint(-50, 50) for _ in range(10)]
print("Исходный список:", numbers)


# even_numbers = [x for x in numbers if x % 2 == 0] # Вывести только чётные элементы 
# print("Чётные элементы списка:", even_numbers)


# print("Максимальное число:", max(numbers)) # максимальное и минимальное число
# print("Минимальное число:", min(numbers))


# user_list = [] # Сортировать список из 5 чисел
# for i in range(5):
#     num = int(input(f"Введите число {i+1}: "))
#     user_list.append(num)

# user_list.sort()
# print("Отсортированный список пользователя:", user_list)   


no_duplicates = [] #Удалить из списка все дубликаты
for x in numbers:
    if x not in no_duplicates:
        no_duplicates.append(x)
print("Список без дубликатов (из original):", no_duplicates)\
    

# # 5. Поменять местами первый и последний элемент списка (операция над оригинальным списком)
# swapped = numbers[:]  # делаем копию чтобы не потерять исходный порядок выше
# if len(swapped) > 1:
#     swapped[0], swapped[-1] = swapped[-1], swapped[0]
# print(f"Список после обмена первого и последнего элемента: {swapped}")

# 1. Словарь студентов и их оценок, средний балл
# students = {
#     "Иван": 4,
#     "Мария": 5,
#     "Петр": 3,
#     "Анна": 4
# }
# average = sum(students.values()) / len(students)
# print(f"Средний балл студентов: {average}")


# 2. Подсчёт количества каждой буквы в строке
# text = input("Введите строку: ").lower()
# letters_count = {}
# for ch in text:
#     if ch not in letters_count:
#         letters_count[ch] = 1
#     else:
#         letters_count[ch] += 1
# print("Словарь букв:", letters_count)


# # 3. Словарь: числа от 1 до 10 и их квадраты
# squares = {x: x**2 for x in range(1, 11)}
# print("Словарь квадратов:", squares)


# # 4. Словарь из двух списков
# keys = ["яблоко", "банан", "груша", "слива"]
# values = [100, 40, 70, 60]
# fruits = dict(zip(keys, values))
# print("Словарь из двух списков:", fruits)

# set1 = {1, 2, 3, 4, 5} # пересечение и объединение множеств
# set2 = {4, 5, 6, 7, 8}
# print(f"Множество 1: {set1}")
# print(f"Множество 2: {set2}")
# print(f"Пересечение: {set1 & set2}")
# print(f"Объединение: {set1 | set2}")


# 2. Найти все уникальные слова в тексте
# sentence = input("Введите текст: ")
# unique_words = set(sentence.split())
# print(f"Уникальные слова: {unique_words}")


# # 3. Общие элементы двух списков через множества
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8]
# common = set(list1) & set(list2)
# print(f"Общие элементы: {common}")


# 4. Проверка подмножества
# A = {1, 2}
# B = {1, 2, 3, 4}
# print(f"A является подмножеством B? {A.issubset(B)}")


# 5. Удалить элементы меньше заданного числа
# nums = {3, 10, 7, 1, 9, 4}
# limit = int(input("Введите число: "))
# filtered = {x for x in nums if x >= limit}
# print("Множество после удаления:", filtered)

import random
from collections import Counter

# numbers = [random.randint(1, 10) for _ in range(20)] # Список из уникальных значений
# print(f"Сгенерированный список: {numbers}")
# print(f"Уникальные значения: {list(set(numbers))}")

numbers = [5, 5, 5, 7, 2, 4, 8, 9, 2, 7, 10, 4, 1, 4, 9, 9, 7, 10, 3, 6]
# counts = {} # количество повторений
# counts = Counter(numbers) # Counter сколько раз каждый элемент встречается в последовательности
# print(f"Словарь количества повторений: {counts}")


# words = 'Дан список слов. Создать множество из слов, длина которых больше 5 символов.' #Множество слов длиной больше 5 символов
# new_words = words.split(" ")
# long_words = {w for w in new_words if len(w) > 5}
# print(f"Слова длиной больше 5 символов: {long_words}")


# sentence = input("Введите предложение: ").lower() # Ввести предложение и подсчитать количество вхождений слов
# word_count = Counter(sentence.split())
# print("Словарь слов и их количества: {dict(word_count)}")


# lst = [1, 2, 2, 3, 4, 4, 5] # 5.
# unique_list = list(set(lst))
# print("Список без дубликатов:", unique_list)


# products = {"яблоко": 50, "груша": 70, "виноград": 120, "банан": 40} # Самый дорогой товар
# max_product = max(products, key=products.get)
# print(f"Самый дорогой товар: {max_product} = {products[max_product]}")


# 7. Список имён: какие встречаются чаще одного раза, и самое частое имя
# names = ["Анна", "Иван", "Мария", "Иван", "Анна", "Анна", "Петр"]
# name_count = Counter(names) #повторения каждого имени
# print(f"Имена и количество повторений: {dict(name_count)}")
# repeated = []  # Имена, которые встречаются больше одного раза
# for name, count in name_count.items():
#     if count > 1:
#         repeated.append(name)
# print(f"Имена, которые встречаются больше одного раза: {repeated}")
# max_name = max(name_count, key=name_count.get) # Самое частое имя
# max_name_count = name_count[max_name]
# print(f"Самое частое имя: {max_name_count}")


text = input("Введите строку: ").lower() # Словарь: символ - индекс первого вхождения
char_index = {}
for i, ch in enumerate(text):
    if ch not in char_index:
        char_index[ch] = i
print(f"Словарь символов и их первого индекса: {char_index}")
 