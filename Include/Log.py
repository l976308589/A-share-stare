import arrow as ar
from path import Path as Pth


def filename_exists(filename):
    if not filename.exists():
        filename.makedirs_p()


def log(string):
    now = ar.now()
    filename = Pth(f".\\Bin\\Log\\{now.format('YYYY-MM-DD')}.txt")
    filename_exists(filename.parent)
    string = f'{now.format("YYYY-MM-DD HH:mm:ss.SSSSSS")}\t{string}'
    string = string.replace('\n', '+')
    filename.write_text(string + '\n', append=True, encoding='gbk')
    print(string)
