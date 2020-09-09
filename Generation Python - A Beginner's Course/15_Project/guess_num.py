import random as rnd


def set_right():
    print("Установите правую границу диапазона n угадывания чисел [1, n]: ")
    while True:
        n = input()
        if n.isdigit() and int(n) > 0:
            return int(n)
        else:
            print("Правая граница должна быть валидным целым числом, превосходящим 0.")


def is_valid(s, rb):
    return s.isdigit() and 1 <= int(s) <= rb


def play_again():
    print("Хотите сыграть ещё раз? д/н")
    answer = input()
    while True:
        if answer == 'д':
            return True

        if answer == 'н':
            return False
        answer = input()


print("Добро пожаловать в числовую угадайку!")

while True:
    right_brd = set_right()
    unknown_n = rnd.randint(1, right_brd)

    attempts_count = 0

    while (True):
        print("Угадай число:")

        curr = input()
        if not is_valid(curr, right_brd):
            print("А может быть все-таки введем целое число от 1 до", right_brd, "?")
            continue

        if int(curr) == unknown_n:
            attempts_count += 1
            print("Вы угадали c", attempts_count, "попытки, поздравляем!")
            break

        if int(curr) < unknown_n:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            attempts_count += 1
            continue

        if int(curr) > unknown_n:
            print("Ваше число больше загаданного, попробуйте еще разок")
            attempts_count += 1
            continue

    if not play_again():
        break

print("Спасибо, что играли в числовую угадайку.")