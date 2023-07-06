# 1) RLE-сжатие – один из самых простых методов сжатия строки, основанный на сокращении подстрок, 
# состоящих из одинаковых символов. Сжатие осуществляется следующим образом:
# Строка разбивается на минимальное количество подстрок, состоящих из одинаковых символов. 
# Например, abbcaaa превращается в строки a, bb, c, aaa.
# Каждая из полученных строк превращается в строку, состоящую из числа и буквы. 
# Числом является количество повторений символа в этой строке, буква берётся из первого символа обрабатываемой строки. 
# Число не добавляется, если количество символов в строке равно единице. Из предыдущего массива строк мы получаем 
# a, 2b, c, 3a.
# Затем полученные строки конкатенируются в исходном порядке. В рассмотренном примере в итоге получим a2bc3a.
# Вводится строка, нужно сжать ее по алгоритму, описанному выше.


# def rle_encode(string):
#     encoded_string = ""
#     count = 1
#     for i in range(1, len(string)):
#         if string[i] == string[i-1]:
#             count += 1
#         else:
#             if count > 1:
#                 encoded_string += str(count)
#             encoded_string += string[i-1]
#             count = 1
#     if count > 1:
#         encoded_string += str(count)
#     encoded_string += string[-1]
#     return encoded_string

# original_string = "abbcaaa"
# encoded_string = rle_encode(original_string)
# print("Encoded string:", encoded_string)



# 2.Создайте список из случайных чисел. 
# Найдите номер его последнего локального максимума (локальный максимум — это элемент, 
# который больше любого из своих соседей).


# import random
# random_list = [random.randint(1, 100) for _ in range(10)]

# # Поиск последнего локального максимума
# last_local_max_index = None
# for i in range(1, len(random_list) - 1):
#     if random_list[i] > random_list[i - 1] and random_list[i] > random_list[i + 1]:
#         last_local_max_index = i + 1

# print("Список случайных чисел:", random_list)
# if last_local_max_index is not None:
#     print("Номер последнего локального максимума:", last_local_max_index)
# else:
#     print("В списке нет локальных максимумов.")



# 3.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

# import random
# random_numbers = [random.randint(1, 10) for _ in range(20)]

# # Нахождение максимального количества одинаковых элементов
# max_count = 0
# max_number = None

# for number in random_numbers:
#     count = random_numbers.count(number)
#     if count > max_count:
#         max_count = count
#         max_number = number

# print("Список случайных чисел:", random_numbers)
# print("Максимальное количество одинаковых элементов:", max_count)
# print("Элемент с максимальным количеством:", max_number)




# 4.Создайте список из случайных чисел. Найдите второй максимум.

import random
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Список случайных чисел:")
print(random_numbers)

# Нахождение второго максимума
max1 = max(random_numbers)
random_numbers.remove(max1)  # Удаляем первый максимум
max2 = max(random_numbers)

# Вывод второго максимума
print("Второй максимум:", max2)