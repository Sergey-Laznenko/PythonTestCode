def is_palindrome(a):
    if str(a) == str(a)[::-1]:
        return True
    else:
        return False


def is_prime(b):
    if b in (0, 1):
        return False
    if b % 2 == 0:
        return False
    for i in range(3, round(b ** (1 / 2) + 1), 2):
        if b % i == 0:
            return False
    return True


def is_even(c):
    if c % 2 == 0:
        return True
    else:
        return False


pws = input().split(':')
a = pws[0]
b = pws[1]
c = pws[2]

if is_palindrome(a) == is_prime(b) == is_even(c):
    print('True')
else:
    print('False')
