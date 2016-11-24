#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import sys
import Data


def newfile(x, n):
    for arg in sys.argv[n:]:
        y = arg + "." + x
        file = open(y, "w")
        file.writelines(Data.extension[x])
        file.close
        print("new file created {0}".format(arg))


if __name__ == "__main__":

    if sys.argv[1] == "new":
        if Data.extension[sys.argv[2]]:
            newfile(sys.argv[2], 3)
        else:
            newfile("py", 2)

