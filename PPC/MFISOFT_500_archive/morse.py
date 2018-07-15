from PIL import Image

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}


def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())


def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)


def get_text_from_img(filename):
    img = Image.open(filename)
    pixels = img.load()
    w, h = img.size

    bg = pixels[0, 0]
    data = []

    for y in range(1, h, 2):
        x = 1
        while x < w:
            if pixels[x, y] != bg:
                if pixels[x + 1, y] == bg:
                    data.append('.')
                    x += 2
                else:
                    data.append('-')
                    x += 4
            else:
                x += 1
        data.append(' ')

    return from_morse(''.join(data))