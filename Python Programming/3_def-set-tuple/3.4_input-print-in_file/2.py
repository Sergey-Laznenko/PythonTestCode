"""
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
"""

def decompress(s):
    result = ''
    for i in range(len(s)):
        if not s[i].isdigit():
            j = i + 1
            cnt = ''
            while s[j].isdigit():
                cnt += s[j]
                if j + 1 < len(s):
                    j += 1
                else:
                    break
            cnt = int(cnt)
            result += s[i] * cnt
    return result


with open('dataset_3363_2.txt', 'r') as f:
    compressed_str = f.readline().strip()

s = decompress(compressed_str)
with open('dataset_3363_2', 'w') as f:
    f.write(s)