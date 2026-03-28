def index(a, b):
    if b in a: # если элемент b есть в списке a
        for i in range(len(a)):# запускаем цикл for для определения индекса элемента b
            if a[i] == b:# если элемент с индексом i совпадает с элементом, то выводим i
                return i
            continue# обрываем
    return None# если нет совпадений выводим None



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
