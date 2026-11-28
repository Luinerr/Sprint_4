import random


def generate_list_book(number):
        result = []

        while len(result) < number:
            s = generate_name_book(10)
            if s not in result:
                result.append(s)

        return result

def generate_name_book(lenght):
    string_for_generate_name = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    return ''.join(random.choices(string_for_generate_name, k=lenght))
