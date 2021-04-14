from tkinter import Button, Label
from tkinter import Tk
from tkinter import filedialog

import py7zr

root = Tk()
root.title("MoDIK - загрузчик модов")



def MD_Install(filepath: str, path: str):
    with py7zr.SevenZipFile(filepath, 'r') as archive:
        archive.extractall(path=path)


b1 = Button(text="Выбрать путь steam", width=5, height=3,)


def steam_path():
    return filedialog.askdirectory()


root.mainloop()
