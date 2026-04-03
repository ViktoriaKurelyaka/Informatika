import csv
import json



INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    result = []
    with open(INPUT_FILENAME, 'r') as f:
        a =  csv.DictReader(f, delimiter=",", quotechar="\n")
        for i in a:
            result.append(i)

    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
