#!/usr/bin/python3.4
# -*-coding:utf-8 -*
import sys


def listmodule():
    try:
        if sys.argv[1] == "-l":
            print("Modules list")
            for x in sys.modules.keys():
                print("{0}".format(x))
    except IndexError:
        quit()


if __name__ == "__main__":
    listmodule()
