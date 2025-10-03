# 1. List comprehension (простое преобразование)
squares = [x**2 for x in range(1, 11)]
print("1. Квадраты чисел от 1 до 10:", squares)

# 2. List comprehension (фильтрация)
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print("2. Чётные числа от 1 до 20:", even_numbers)
