import json
import time
from random import randint

from ctx import cntxMng
from dec import print_result

with open(r"C:\Users\MI\Downloads\data_light.json", encoding="utf - 8") as f:
    data = json.load(f)


@print_result
def f1(*args):
    result = sorted(list(set([data[prof_el]["job-name"].lower() for prof_el in range(len(data))])))
    return result


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    money = randint(10 ** 5, 2 * 10 ** 5)
    return list(map(lambda x: x + ',зарплата ' + str(money) + ' руб', arg))


with cntxMng():
    time.sleep(0.5)
    # print(type(f2(f1(data))))
    f4(f3(f2(f1(data))))
