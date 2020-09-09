import random as rnd

# Константы.
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

# Наш алфавит, из него состоит пароль.
chars = ''


def input_boolean():
    answ = input()
    while True:
        if answ == 'д':
            return True
        if answ == 'н':
            return False

        print("Некорректный ввод! Введите 'д' или 'н'.")
        answ = input()


def exclude_pw_dataset(dataset, ex_chrs):
    if input_boolean():
        for sym in ex_chrs:
            dataset.replace(sym, "")


# Что включаем в пароль?
print("Сколько паролей сгенерировать?")
passwords_count = int(input())

print("Какова длина паролей?")
password_len = int(input())

print("Включать ли цифры: 0123456789? д/н")
if input_boolean():
    chars += digits

print("Включать ли строчные буквы: abcdefghijklmnopqrstuvwxyz? д/н")
if input_boolean():
    chars += lowercase_letters

print("Включать ли прописные буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ? д/н")
if input_boolean():
    chars += uppercase_letters

print("Включать ли символы: !#$%&*+-=?@^_? д/н")
if input_boolean():
    chars += punctuation

print("Исключить ли неоднозначные символы: il1Lo0O? д/н")
if input_boolean():
    for sym in "il1Lo0O":
        chars = chars.replace(sym, "")


# Функция для генерации паролей.
def generate_password(length, chrs):
    password = ""
    for _ in range(length):
        password += rnd.choice(chrs)

    return password


print("======================")

for i in range(passwords_count):
    print(i + 1, ". ", generate_password(password_len, chars), sep="")

print("======================")

print("Вуаля! Ваши пароли успешно сгенерированы.")
