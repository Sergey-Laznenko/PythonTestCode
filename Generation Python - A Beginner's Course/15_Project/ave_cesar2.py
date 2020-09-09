def calc_shift(s, index):
    shift = 0
    punctuation = '''.,/?!:;[]{}"" -'''
    for i in range(index, len(s)):
        if s[i] in punctuation:
            break
        shift += 1

    return shift


def encrypt(message):
    encrypted_m = message

    alphabet_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_low = "abcdefghijklmnopqrstuvwxyz"

    ind = 0
    while ind < len(message):
        if message[ind] in '''.,/?!:;[]{}"" -''':
            ind += 1
            continue

        shift = calc_shift(message, ind)
        for j in range(ind, ind + shift):
            if message[j] in alphabet_high:
                index = (alphabet_high.find(message[j]) + shift) % 26
                encrypted_m = encrypted_m[:j] + alphabet_high[index] + encrypted_m[j + 1:]

            if message[j] in alphabet_low:
                index = (alphabet_low.find(message[j]) + shift) % 26
                encrypted_m = encrypted_m[:j] + alphabet_low[index] + encrypted_m[j + 1:]

        ind += shift + 1

    return encrypted_m


# main
message_ = input()
print(encrypt(message_))
