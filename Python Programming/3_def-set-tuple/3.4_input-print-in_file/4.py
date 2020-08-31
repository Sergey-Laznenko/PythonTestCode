"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку
по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике,
физике и русскому языку по всем абитуриентам.
"""

def get_stat(l):
    all_avg = [0 for i in range(3)]
    all_summ = [0 for i in range(3)]
    priv_avg = list()

    for s in l:
        score = s.split(';')
        summ = 0
        for i in range(1, len(score)):
            summ += int(score[i])
            all_summ[i - 1] += int(score[i])
        priv_avg.append(summ / i)

    for i in range(len(all_avg)):
        all_avg[i] = all_summ[i] / len(priv_avg)

    stat = list()
    stat.append(priv_avg)
    stat.append(all_avg)

    return stat


lst = list()
with open('dataset.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lst.append(line)

stat = get_stat(lst)

with open('dataset.txt', 'w') as f:
    for priv in stat[0]:
        f.write(str(priv) + '\n')
    for avg in stat[1]:
        f.write(str(avg) + ' ')
