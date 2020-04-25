import os
import requests
import json     #конверстировать различные обьекты в строку может сериализация


# url = 'https://geekbrains.ru/'
#
# response = requests.get(url)
# file = open('test.html', 'w', encoding='UTF-8')
# try:
#     file.write(response.text)
# except IOError:
#     pass
# finally:
#     file.close()

#менеджер контекста
# with open('test2.txt', 'w', encoding='UTF-8') as file:
#     for itm in tmp:
#         file.write(itm + '\n')

# with open('test.html', 'r', encoding='UTF-8') as file:
#     # for line in file:
#     #     print(line, end='')
#     print(file.read(4))           # в скобочках можно указ сколько байт прочитать ибюо 1 символ = 1 байт

# print(os.listdir())
# print(os.environ['PWD'])

# os.environ['NEWKEY'] = 'Hello'
# print(os.environ)

# file_name = 'newname.txt'
# new_file_name = 'hello.txt'
#
# path = os.path.dirname(__file__)
#
# file_path = os.path.join(path, file_name)
# new_file_path = os.path.join(path, new_file_name)
# print(file_path)
# print(new_file_path)
# print(os.rename(file_path, new_file_path))

# print(path)

# print(__file__)

# print(os.rename('test2.txt', 'newname.txt'))

temp = {
    'name': 312321123,
    'data': [1, 2, 3, 4, 5],
    'sub': None,
    'rest': False,
    'tuple': (1, 2, 3, 4),
}

# j_data = json.dumps(temp)

# with open('data.json', 'w', encoding='UTF-8') as file:
#    file.write(json.dumps(temp))

with open('data.json', 'r', encoding='UTF-8') as file:
   data = json.loads(file.read())

print(type(data))
print(data)

#
# print(type(j_data))
# print(j_data)

