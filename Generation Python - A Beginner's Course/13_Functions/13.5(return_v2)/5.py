"""
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

 - его длина не менее 8 символов;
 - он содержит как минимум одну заглавную букву (верхний регистр);
 - он содержит как минимум одну строчную букву (нижний регистр);
 - он содержит хотя бы одну цифру.
"""


def is_password_good(password):
    nums = "0123456789"
    flag1 = flag2 = flag3 = False
    if len(password) < 8:
        result = False
        return result
    elif password.isdigit():
        result = False
        return result
    for i in password:
        if i.isupper():
            flag1 = True
        elif i.islower():
            flag2 = True
        elif i in nums:
            flag3 = True
    if flag1 * flag2 * flag3:
        result = True
    elif flag1 ** flag2 and not flag3:
        result = False
    else:
        result = False
    return result


txt = input()

print(is_password_good(txt))
