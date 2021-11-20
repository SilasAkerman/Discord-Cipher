


def encrypt_text(message, key):
    text = ""
    for symbol in message:
        if symbol.upper() in key.keys():
            text += key[symbol.upper()]
        else:
            text += symbol.lower()

    return text


def decrypt_text(message, key):
    keys = list(key.keys())
    values = list(key.values())

    key = {}
    for i in range(len(keys)):
        key.update({values[i].upper(): keys[i].lower()})

    text = ""
    for symbol in message:
        if symbol.upper() in key.keys():
            text += key[symbol.upper()]
        else:
            text += symbol.lower()

    return text