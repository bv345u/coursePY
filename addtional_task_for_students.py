# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    count = 0
    for i in l:
        if i == item:
            count+=1
    return count

a = [12, 423, 32, 3312]
print(my_count(a, 12))