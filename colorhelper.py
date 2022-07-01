import os

codes = {
    "reset": "\u001b[0m",
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "light_yellow": "\u001b[93m",
    "yellow": "\u001b[33m",
    "yellow_background": "\u001b[43m",
    "blue": "\u001b[34m",
    "purple": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "bold": "\u001b[1m",
    "unbold": "\u001b[21m",
    "underline": "\u001b[4m",
    "stop_underline": "\u001b[24m",
    "blink": "\u001b[5m"
}


def formatter(msg, pre):
    post = codes["reset"]
    return u"{pre}{msg}{post}".format(**{
        'pre': pre,
        'msg': msg,
        'post': post
    })


def rojo(msg):
    return formatter(msg, codes["red"])


def verde(msg):
    return formatter(msg, codes["green"])


def azul(msg):
    return formatter(msg, codes["blue"])


if __name__ == "__main__":
    os.system("color")
    for code in codes:
        print(formatter(f"este es el color {code}", codes[code]))
        print("-----------------------------------------")
