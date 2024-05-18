import string

BASE64_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

def encode_base64(data):
    binary_string = ''.join(f'{byte:08b}' for byte in data)
    padding_length = (6 - len(binary_string) % 6) % 6
    binary_string += '0' * padding_length

    base64_string = ''
    for i in range(0, len(binary_string), 6):
        segment = binary_string[i:i + 6]
        index = int(segment, 2)
        base64_string += BASE64_ALPHABET[index]

    padding = '=' * ((4 - len(base64_string) % 4) % 4)
    return base64_string + padding

def decode_base64(base64_string):
    padding_length = base64_string.count('=')
    base64_string = base64_string.rstrip('=')
    binary_string = ''

    for char in base64_string:
        index = BASE64_ALPHABET.index(char)
        binary_string += f'{index:06b}'

    binary_string = binary_string[:len(binary_string) - (padding_length * 2)]

    data = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        if len(byte) == 8:
            data.append(int(byte, 2))

    return bytes(data)