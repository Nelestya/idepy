#!/usr/bin/python3.4
# -*-coding:utf-8 -*
import sys
import Data


def newfile():
    for arg in sys.argv[2:]:
        x = arg + ".py"
        file = open(x, "w")
        file.writelines(Data.pathpy + "\n")
        file.writelines(Data.encoding + "\n")
        file.close
        print("new file created {0}".format(arg))


if __name__ == "__main__":
    print(type(sys.argv))
    print(sys.argv[1])
    if sys.argv[1] == "new":
        newfile()
