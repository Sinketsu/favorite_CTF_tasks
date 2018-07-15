import os
from PIL import Image


def diff(pix1, pix2):
    return sum([int(pix1[i] - pix2[i]) ** 2 for i in range(3)])


def combine(img_list, img_out):
    img_list = ['flag/' + i for i in img_list]
    images = list(map(Image.open, img_list))
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save(img_out)


total = len(os.listdir('./flag'))
images = []

img_filename = os.listdir('./flag')[0]
images.append(img_filename)

while len(images) != total:
    img = Image.open('flag/' + img_filename)
    pixels = img.load()

    min_d = 999

    for file in os.listdir('./flag'):
        file_pixels = Image.open('flag/' + file).load()

        distance = diff(pixels[0, 15], file_pixels[0, 0])

        if distance < min_d and file not in images:
            min_d = distance
            min_d_file = file

    images.append(min_d_file)
    img_filename = min_d_file

    print('Progress: {}%'.format(round(len(images) / total * 100., 2)))

combine(images, 'result.png')

print('')
print('Done!')
print('Result file is result.png')