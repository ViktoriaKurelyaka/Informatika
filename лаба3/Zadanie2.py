def find_common_participants(participants_first_group, participants_second_group, o = ','):
    a = set(participants_first_group.split(o))# делим стоку на отдельные элементы и приводим к множеству
    b = list(participants_second_group.split(o))
    c = list(a.intersection(b)) # находим пересечение двух множеств
    return c




participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, o = '|'))