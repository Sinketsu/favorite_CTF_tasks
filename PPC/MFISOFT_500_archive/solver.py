import zipfile
import morse
import shutil
import os


while True:
    pwd = morse.get_text_from_img('pwd.png')
    pwd = pwd.lower()
    print('Decoded password: {}'.format(pwd))

    for file in os.listdir('./'):
        if '.zip' in file:
            zip_file = file

    z = zipfile.ZipFile(zip_file, 'r')
    z.extractall(pwd=bytes(pwd.encode()))
    z.close()

    os.remove(zip_file)

    for file in os.listdir('./flag'):
        if '.zip' in file:
            zip_file = file

    shutil.move('flag/pwd.png', './pwd.png')
    shutil.move('flag/' + zip_file, './' + zip_file)