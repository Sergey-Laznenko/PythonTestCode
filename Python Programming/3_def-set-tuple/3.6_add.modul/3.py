"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""

import requests

with open('dataset.txt', 'r') as f:
    url = f.readline().strip()

folder = 'https://stepic.org/media/attachments/course67/3.6.3/'
text = ''

while text[:2] != 'We':
    r = requests.get(url)
    text = r.text
    url = folder + text
    print(text)

print('--------------')
print('Thats all. Check "output/step03.text')

with open('dataset.txt', 'w') as f:
    f.write(text)
