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
