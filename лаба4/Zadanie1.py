import json
a = "input.json"#введем переменую а

def task() -> float:
    with open ('input.json','r') as f:# открываем файл для чтения
        d = json.load(f)# создаем переменную, в которой заключены данные из файла input.json
        k = 0# сумма произведений
        for i in d:
            h =  i['score'] * i['weight']# находим произведение "score" и "weight"
            k += h# найденное произведение добавляем к сумме
        return round(k, 3)







print(task())
