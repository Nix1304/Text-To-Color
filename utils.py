import datetime
import pickle
import random
from io import BytesIO

import boto3


def load_obj(name):
    with open(f'{name}.pkl', 'rb') as f:
        return pickle.load(f)


def save_obj(obj, name):
    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(obj, f)


def save_to_s3(name):
    s3 = boto3.resource('s3')
    data = open(f'{name}', 'rb')
    s3.Bucket('kurumibotpython').put_object(Key=name, Body=data)


def save_to_s3_pickle(obj, name):
    save_obj(obj, name)
    save_to_s3(f'{name}.pkl')


def open_from_s3_pickle(name):
    s3 = boto3.resource('s3')
    with BytesIO() as data:
        s3.Bucket('kurumibotpython').download_fileobj(f'{name}.pkl', data)
        data.seek(0)
        return pickle.load(data)


def generate_random_code(length):
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    _out = ''
    for i in range(0, length):
        _out += symbols[random.randint(0, len(symbols) - 1)]
    return _out


def activate_code(code):
    codes = open_from_s3_pickle('codes')
    if code in codes.keys():
        if codes[code]['activated']:
            print('Code already activated!')
            return
    else:
        print('Code not found!')
        return
    if 'money' in codes[code].keys():
        print(f'Added {codes[code]["money"]}')
    if 'exp' in codes[code].keys():
        print(f'Added {codes[code]["exp"]}')
    if 'group' in codes[code].keys():
        print(f'Group set {codes[code]["group"]}')
    codes[code]['activated'] = True
    save_to_s3_pickle(codes, 'codes')


def add_code(add):
    codes = open_from_s3_pickle('codes')
    code = generate_random_code(8)
    print(code)
    while code in codes.keys():
        code = generate_random_code(8)
    if 'activated' in add.keys():
        code = {code: add}
    else:
        add['activated'] = False
        code = {code: add}
    codes.update(code)
    save_to_s3_pickle(codes, 'codes')


def wipe_codes():
    save_obj({}, 'codes')


def get_codes():
    print(open_from_s3_pickle('codes'))


def get_times_of_day(variants: (list, set, frozenset)):
    """Функция возвращает ответ в зависимости от времени суток
        Аргументы:
        :param variants: ответ в разное время суток (ночь, утро, день, вечер)
        Пример:
        get_times_of_day(("Ночь", "Утро", "День", "Вечер"))
        :return: ответ в зависимости от времени суток
        """
    hours = datetime.datetime.now().hour
    if hours in range(0, 6):
        return variants[0]
    elif hours in range(6, 12):
        return variants[1]
    elif hours in range(12, 18):
        return variants[2]
    elif hours in range(18, 0):
        return variants[3]
