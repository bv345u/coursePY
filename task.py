# TODO Напишите функцию find_common_participants

def find_common_participants(a, b, razd=","):
    out = []
    a = a.split(razd)
    b = b.split(razd)

    for i in a:
        for j in b:
            if i == j:
                out.append(i)

    out.sort()
    return(out)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))