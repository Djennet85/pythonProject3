#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
if month in sum(seasons_dict.values(), []):
    for i in seasons_dict.items():
        if month in i [1]:
            print(i[0])
else:
    print("Вы ввели не существующий месяц!")
