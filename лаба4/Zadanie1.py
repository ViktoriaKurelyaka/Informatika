import json
a = "input.json"

def task() -> float:
    with open ('input.json','r') as f:
        d = json.load(f)# создаем переменную, в которой заключены данные из файла input.json
        k = 0# сумма произведений
        for i in d:
            h =  i['score'] * i['weight']
            k += h
        return round(k, 3)







print(task())
