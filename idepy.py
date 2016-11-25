#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import sys
import Data


def newfile(x, n):
    for arg in sys.argv[n:]:
        filename = arg + "." + x
        file = open(filename, "w")
        file.writelines(Data.extension[x])
        file.close
        print("new file created {0}".format(arg))
    """create a new file with extension in Data"""


def newfileManager():
    try:
        if sys.argv[1] == "new":
            try:
                if Data.extension[sys.argv[2]]:
                    newfile(sys.argv[2], 3)
            except KeyError:
                newfile("py", 2)
    except IndexError:
        quit()
    """condition for create a new file, use arguments new"""
    """if a specify file use the dictionnary in the Data.extension"""


if __name__ == "__main__":
    newfileManager()
