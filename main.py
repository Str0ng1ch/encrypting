def encrypt_caesar(text):
    new_text = ''
    for i in range(len(text)):
        new_text += chr((ord(text[i]) + 3) % 65536)
    return new_text


def decode_caesar(text):
    index = ord(max(t := {item: text.count(item) for item in text}, key=t.get)) - ord(' ')
    new_text = ''
    for i in range(len(text)):
        new_text += chr((ord(text[i]) - index) % 65536)
    return new_text


def encrypt_viginera(text, key):
    new_text = ''
    for i in range(len(text)):
        new_text += chr((ord(text[i]) + key[i % len(key)]) % 65536)
    return new_text


def main():
    text = 'i love ice cream so much'
    print(encrypt_caesar(text))
    print(decode_caesar(encrypt_caesar(text)))
    print(encrypt_viginera('i love ice cream so much', [1, 2, 3, 4]))
    print(encrypt_viginera(encrypt_viginera('i love ice cream so much', [1, 2, 3, 4]), [-1, -2, -3, -4]))


if __name__ == "__main__":
    main()
