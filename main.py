from tkinter import Button, Label
from tkinter import Tk
from tkinter import filedialog

import py7zr

root = Tk()
root.title("MoDIK - загрузчик модов")


def steam_path():
    return filedialog.askdirectory()


def MD_Install(filepath: str, path: str):
    with py7zr.SevenZipFile(filepath, 'r') as archive:
        archive.extractall(path=path)


def clicked():
    steam = steam_path()
    f = open('steam_path.py', 'w')
    f.write(f"steam = '{steam}'")


b1 = Button(text="Выбрать путь steam",  command=clicked)
b1.pack()

root.mainloop()
