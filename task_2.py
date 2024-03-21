# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — з
# начение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое
# представление.

def my_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(my_dict(bananas=23, apples=(234, 456), potato=[345, 456, 667]))


