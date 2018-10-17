import random

from PIL import Image

colors = {'#000000': 'A', '#ccccff': 'B', '#ccffff': 'C', '#ccffcc': 'D', '#ccff99': 'E',
          '#ffff66': 'F', '#6666ff': 'G', '#33cccc': 'H', '#009933': 'I', '#ff33cc': 'J',
          '#000099': 'K', '#003366': 'L', '#ffff00': 'M', '#660033': 'N', '#800000': 'O',
          '#666699': 'P', '#003300': 'Q', '#669900': 'R', '#000066': 'S', '#003399': 'T',
          '#9900ff': 'U', '#ff0000': 'V', '#0066ff': 'W', '#ccff33': 'X', '#009999': 'Y',
          '#cc33ff': 'Z',
          '#06b11a': 'a', '#5a0864': 'b', '#1c8a9d': 'c', '#3ea707': 'd', '#1ae86d': 'e',
          '#8cc02c': 'f', '#fa6f2e': 'g', '#8d8216': 'h', '#199aee': 'i', '#037f97': 'j',
          '#bc04e8': 'k', '#2ded2a': 'l', '#d3d6d8': 'm', '#fa16c8': 'n', '#e55f5d': 'o',
          '#3ef905': 'p', '#b4e0a2': 'q', '#d72bb4': 'r', '#841799': 's', '#f161c6': 't',
          '#f7543d': 'u', '#f5b740': 'v', '#f61021': 'w', '#9cb471': 'x', '#f05825': 'y',
          '#510d35': 'z',
          '#ffffff': ' ', '#d12bba': ',', '#511952': '.', '#19c4f4': '[', '#f4cb23': ']',
          '#9998b8': '!', '#e29829': '?', '#182ca9': '-', '#87d46d': '\'',
          '#f435c3': '1', '#3207f7': '2', '#45cb27': '3', '#63ea13': '4', '#132836': '5',
          '#f1b8b5': '6', '#092be0': '7', '#e215ab': '8', '#38527d': '9', '#827337': '0'}

liters = {'A': '#000000', 'B': '#ccccff', 'C': '#ccffff', 'D': '#ccffcc', 'E': '#ccff99',
          'F': '#ffff66', 'G': '#6666ff', 'H': '#33cccc', 'I': '#009933', 'J': '#ff33cc',
          'K': '#000099', 'L': '#003366', 'M': '#ffff00', 'N': '#660033', 'O': '#800000',
          'P': '#666699', 'Q': '#003300', 'R': '#669900', 'S': '#000066', 'T': '#003399',
          'U': '#9900ff', 'V': '#ff0000', 'W': '#0066ff', 'X': '#ccff33', 'Y': '#009999',
          'Z': '#cc33ff',
          'a': '#06b11a', 'b': '#5a0864', 'c': '#1c8a9d', 'd': '#3ea707', 'e': '#1ae86d',
          'f': '#8cc02c', 'g': '#fa6f2e', 'h': '#8d8216', 'i': '#199aee', 'j': '#037f97',
          'k': '#bc04e8', 'l': '#2ded2a', 'm': '#d3d6d8', 'n': '#fa16c8', 'o': '#e55f5d',
          'p': '#3ef905', 'q': '#b4e0a2', 'r': '#d72bb4', 's': '#841799', 't': '#f161c6',
          'u': '#f7543d', 'v': '#f5b740', 'w': '#f61021', 'x': '#9cb471', 'y': '#f05825',
          'z': '#510d35',
          ' ': '#ffffff', ',': '#d12bba', '.': '#511952', '[': '#19c4f4', ']': '#f4cb23',
          '!': '#9998b8', '?': '#e29829', '-': '#182ca9', '\'': '#87d46d',
          '1': '#f435c3', '2': '#3207f7', '3': '#45cb27', '4': '#63ea13', '5': '#132836',
          '6': '#f1b8b5', '7': '#092be0', '8': '#e215ab', '9': '#38527d', '0': '#827337'}


def to_image(text):
    dis = (len(text) if len(text) < 16 else 16,
           len(text) // 17 + 1)
    image = Image.new('RGBA', dis)
    pix = image.load()
    index = 0
    for y in range(0, dis[1]):
        for x in range(0, dis[0]):
            if index >= len(text):
                pix[x, y] = (123, 0, 123, 0)
            else:
                h = liters[text[x + y*16]].lstrip('#')
                pix[x, y] = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
            index += 1
    image.save('output.png')


def from_image(image):
    image = image.convert('RGB')
    pix = image.load()
    max_dis = image.size
    _out = ''
    for y in range(0, max_dis[1]):
        for x in range(0, max_dis[0]):
            color = '#%02x%02x%02x' % pix[x,y]
            if color in colors:
                _out += colors[color]
    return _out


def generate_rand_color():
    return '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# print(generate_rand_color())
to_image('Text to coding')
print(from_image(Image.open('output.png')))
