# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

cata = "data/catalogue.json"

def load_cata(cata):
    with open(cata, encoding='utf-8') as a:
        # 读取文件
        result = json.load(a)
    print(result.values())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_cata(cata)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
