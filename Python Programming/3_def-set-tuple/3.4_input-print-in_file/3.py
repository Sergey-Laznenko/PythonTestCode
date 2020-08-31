"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
"""

def word(l):
    d = dict()

    for s in l:
        words = s.lower().split()
        for w in words:
            if w in d.keys():
                d[w] += 1
            else:
                d[w] = 1
        m_key = w

    m_val = d[m_key]

    for key, value in d.items():
        if value > m_val:
            m_key = key
            m_val = value
        if value == m_val:
            if key < m_key:
                m_key = key
                m_val = value

    result = m_key + ' ' + str(m_val)

    return(result)


lst = list()
with open('dataset.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lst.append(line)

s = word(lst)

with open('dataset.txt', 'w') as f:
    f.write(s)
