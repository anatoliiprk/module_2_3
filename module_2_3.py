print('"Нули ничто, отрицание недопутимо!"')
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i = i+1
        if i == len(my_list):
            print("Конец списка")
        continue
    elif my_list[i] > 0:
        print(my_list[i])
        i = i+1
        if i == len(my_list):
            print("Конец списка")
    else:
        print("Встретилось отрицательное число:", my_list[i])
        break
print("Задание выполнено")