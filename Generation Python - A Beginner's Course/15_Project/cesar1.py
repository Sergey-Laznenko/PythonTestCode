def encrypt(message, lang, shift):
    encrypted_m = message

    if lang == "en":
        alphabet_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_low = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(message)):
            if message[i] in alphabet_high:
                index = (alphabet_high.find(message[i]) + shift) % 26
                encrypted_m = encrypted_m[:i] + alphabet_high[index] + encrypted_m[i + 1:]

            if message[i] in alphabet_low:
                index = (alphabet_low.find(message[i]) + shift) % 26
                encrypted_m = encrypted_m[:i] + alphabet_low[index] + encrypted_m[i + 1:]

        return encrypted_m

    elif lang == "ru":
        alphabet_high = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        alphabet_low = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

        for i in range(len(message)):
            if message[i] in alphabet_high:
                index = (alphabet_high.find(message[i]) + shift) % 32
                encrypted_m = encrypted_m[:i] + alphabet_high[index] + encrypted_m[i + 1:]

            if message[i] in alphabet_low:
                index = (alphabet_low.find(message[i]) + shift) % 32
                encrypted_m = encrypted_m[:i] + alphabet_low[index] + encrypted_m[i + 1:]

        return encrypted_m


def decrypt(message, lang, shift):
    decrypted_m = message

    if lang == "en":
        alphabet_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_low = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(message)):
            if message[i] in alphabet_high:
                index = (alphabet_high.find(message[i]) - shift) % 26
                decrypted_m = decrypted_m[:i] + alphabet_high[index] + decrypted_m[i + 1:]

            if message[i] in alphabet_low:
                index = (alphabet_low.find(message[i]) - shift) % 26
                decrypted_m = decrypted_m[:i] + alphabet_low[index] + decrypted_m[i + 1:]

        return decrypted_m

    elif lang == "ru":
        alphabet_high = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        alphabet_low = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

        for i in range(len(message)):
            if message[i] in alphabet_high:
                index = (alphabet_high.find(message[i]) - shift) % 32
                decrypted_m = decrypted_m[:i] + alphabet_high[index] + decrypted_m[i + 1:]

            if message[i] in alphabet_low:
                index = (alphabet_low.find(message[i]) - shift) % 32
                decrypted_m = decrypted_m[:i] + alphabet_low[index] + decrypted_m[i + 1:]

        return decrypted_m


print("Приветствую. Вы хотите зашифровать или расшифровать сообщение? encrypt/decrypt")

# direction: encryption or decryption
direction_ = False
while True:
    input_ = input()

    if input_ == "encrypt":
        direction_ = True
        break

    if input_ == "decrypt":
        break

    print("Пожалуйста введите encrypt, чтобы зашифровать сообщение и decrypt, чтобы расшифровать сообщение.")

# language: Russian or English
lang_ = "en"
print("Вы можете выбрать русский язык (без буквы 'ё') или английский язык. ru/en")
while True:
    input_ = input()

    if input_ == "ru":
        lang_ = "ru"
        break

    if input_ == "en":
        break

    print("Пожалуйста введите ru, чтобы выбрать русский язык и en, чтобы выбрать английский.")

# shift step (right steps in alphabet)
shift_ = 0
print("Вы можете выбрать шаг сдвига в алфавите - натуральное число.")
while True:
    input_ = input()

    if input_.isdigit() and int(input_) > 0:
        shift_ = int(input_)
        break

    print("Пожалуйста, введите натуральное число для указания шага сдвига.")

# main
if direction_:
    print("Введите сообщение для шифрования(!внимание! используйте тот язык, который выбрали):")
    message_ = input()
    print("Зашифрованное сообщение:", encrypt(message_, lang_, shift_))
else:
    print("Введите сообщение для расшифровки(!внимание! используйте тот язык, который выбрали):")
    message_ = input()
    print("Расшифрованное сообщение:", decrypt(message_, lang_, shift_))