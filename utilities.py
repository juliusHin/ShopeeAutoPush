#isinya untuk misc
import os
import platform
import datetime

def clear_screen():
    os_type = platform.system()

    if os_type == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def timestamp():
    now= datetime.datetime.now()
    currentTime="{}/{}/{} {}:{}:{}".format(now.year,now.month,now.day,now.hour,now.minute,now.second)
    return currentTime