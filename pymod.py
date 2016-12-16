#!/usr/bin/python3.4
# -*-coding:utf-8 -*
import sys


class modules:

    def __init__(self):
        self.module_list = ["abc",
                            "aifc",
                            "argparse",
                            "array",
                            "ast",
                            "asynchat",
                            "asyncio",
                            "asyncore",
                            "atexit",
                            "audioop",
                            "base64",
                            "bdb",
                            "binascii",
                            "binhex",
                            "bisect",
                            "builtins",
                            "bz2",
                            "calendar",
                            "cgi",
                            "cgitb",
                            "chunk",
                            "cmath",
                            "cmd",
                            "code",
                            "codecs",
                            "codeop",
                            "collections",
                            "colorsys",
                            "compileall",
                            "concurrent",
                            "configparser",
                            "contextlib",
                            "copy",
                            "copyreg",
                            "cProfile",
                            "crypt",
                            "csv",
                            "ctypes",
                            "curses",
                            "datetime",
                            "dbm",
                            "decimal",
                            "difflib",
                            "dis",
                            "distutils",
                            "doctest",
                            "dummy_threading",
                            "email",
                            "encodings",
                            "ensurepip",
                            "enum",
                            "errno",
                            "faulthander",
                            "fcntl",
                            "filecmp",
                            "fileinput",
                            "fnmatch",
                            "formatter",
                            "fpectl",
                            "fractions",
                            "ftplib",
                            "functools",
                            "gc",
                            "getopt",
                            "getpass",
                            "gettext",
                            "glob",
                            "grp",
                            "gzip",
                            "hashlib",
                            "heapq",
                            "hmac",
                            "html",
                            "http",
                            "imaplib",
                            "imghdr",
                            "imp",
                            "importlib",
                            "inspect",
                            "io",
                            "ipaddress",
                            "itertools",
                            "json",
                            "keyword",
                            "lib2to3",
                            "linecache",
                            "locale",
                            "logging",
                            "lzma",
                            "macpath",
                            "mailbox",
                            "mailcap",
                            "marshal",
                            "math",
                            "mimetypes",
                            "mmap",
                            "modulefinder",
                            "msilib",
                            "msvcrt",
                            "multiprocessing",
                            "netrc",
                            "nis",
                            "nntplib",
                            "numbers",
                            "operator",
                            "optparse",
                            "os",
                            "ossaudiodev",
                            "parser",
                            "pathlib",
                            "pdb",
                            "pickle",
                            "pickletools",
                            "pipes",
                            "pkgutil",
                            "platform",
                            "plistlib",
                            "poplib",
                            "posix",
                            "pprint",
                            "profile",
                            "pstats",
                            "pty",
                            "pwd",
                            "py_compile",
                            "pyclbr",
                            "pydoc",
                            "queue",
                            "quopri",
                            "random",
                            "re",
                            "readline",
                            "reprlib",
                            "resource",
                            "rlcompleter",
                            "runpy",
                            "sched",
                            "select",
                            "selectors",
                            "shelve",
                            "shlex",
                            "shutil",
                            "signal",
                            "site",
                            "smtpd",
                            "smtplib",
                            "sndhdr",
                            "socket",
                            "socketserver",
                            "spwd",
                            "sqlite3",
                            "ssl",
                            "stat",
                            "statistics",
                            "string",
                            "stringprep",
                            "struct",
                            "subprocess",
                            "sunau",
                            "symbol",
                            "symtable",
                            "sys",
                            "sysconfig",
                            "syslog",
                            "tabnanny",
                            "tarfile",
                            "telnetlib",
                            "tempfile",
                            "termios",
                            "test",
                            "textwrap",
                            "threading",
                            "time",
                            "timeit",
                            "tkinter",
                            "token",
                            "tokenize",
                            "trace",
                            "traceback",
                            "tracemalloc",
                            "tty",
                            "turtle",
                            "turtledemo",
                            "types",
                            "typing",
                            "unicodedata",
                            "unitest",
                            "urllib",
                            "uu",
                            "uuid",
                            "venv",
                            "warnings",
                            "wave",
                            "weakref",
                            "webbrowser",
                            "winreg",
                            "winsound",
                            "wsgiref",
                            "xdrlib",
                            "xml",
                            "xmlrpc",
                            "zipapp",
                            "zipfile",
                            "zipimport",
                            "zlib"]
        self.modules_available = []
        self.modules_unvailable = []

    def pip(self):
        """import pip, if you have not import that print an Error"""
        try:
            __import__("pip")
        except ImportError:
            print("you have not install pip")

    def Tkpresent():
        try:
            try:
                import tkinter
            except ImportError:
                import Tkinter
        except ImportError:
            print("Wrapper Tk not avalaible")

    def module_verification(self):
        """list your module in your computer if available or not"""
        for liste in self.module_list:
            try:
                __import__(liste)
                self.modules_available.append(str(liste))
            except ImportError:
                self.modules_unvailable.append(str(liste))

    def printy(self):
        """print the available module"""
        try:
            for module in self.modules_available:
                print("{0}".format(module))
        except Exception as x:
            print("printy ERROR".center(40))
            print(x)

    def printn(self):
        """print the unvailable module"""
        try:
            for module in self.modules_unvailable:
                print("{0}".format(module))
        except Exception as x:
            print("printy ERROR".center(40))
            print(x)

    def listmodule():
        try:
            if sys.argv[1] == "-l":
                print("Modules list")
                for x in sys.modules.keys():
                    print("{0}".format(x))
        except IndexError:
            quit()


if __name__ == "__main__":
    x = modules()
    x.module_verification()
    x.printn()
    x.pip()
