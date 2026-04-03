import csv
import json



INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    result = [] #создадим пустой список
    with open(INPUT_FILENAME, 'r') as f:
        a =  csv.DictReader(f, delimiter=",", quotechar="\n")# введем переменную для чтения значений из csv, и сделаем разделитель между значениями и разделитель строк
        for i in a:
            result.append(i)# преобразуем каждую строку в словарь и добавим в ответ

    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)#запишем результата в json файл с отступами равными 4



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
