# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


my_list = (input("Введите числа через пробел: ")).split()
print(my_list)
a = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
my_list[:a:2], my_list[1:a:2] = my_list[1:a:2], my_list[:a:2]
print(my_list)












