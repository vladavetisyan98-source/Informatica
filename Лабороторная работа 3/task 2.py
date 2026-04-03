# TODO Напишите функцию find_common_participants


def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки на списки
    list1 = group1.split(separator)
    list2 = group2.split(separator)

    # Находим общих участников с помощью множества
    common = set(list1) & set(list2)

    # Возвращаем отсортированный список
    return sorted(common)


# Основной код для проверки
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator='|'
)
