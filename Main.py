#!/usr/bin/python
# importation block
from read.functionshapetotime import *
from read.notetohertz import *
from read.partitiontolist import *
from read.playpartition import *
from files.readfile import *
from analytics.new_melody import *
import tkinter as tk
from pathlib import Path
# end of importation block
# database initialization
if Path('pdata.json').is_file():
    partidic = readfilejson()
else:
    partidic = readfiletxt()
# end database initialization
# tkinter commands functions
# end tkinter commands functions
# tkinter display
# main window settings
root = tk.Tk()
root.title("Music and Statistic")
root.geometry("1080x720")
root.minsize(480, 360)
root.maxsize(1920, 1080)
root.iconbitmap("root.ico")
root.config(bg="#7EAFE0")
# end main widow settings
# description title
desc = tk.Label(root, text="Welcome to Music and Statistic, a program to derive melody from other's", font=(
    "Helvetica", 20), bg="#7EAFE0")
desc.pack(expand=tk.YES)
# end description title

# kill button

root.mainloop()  # indicateur de boucle sur la fenêtre principale
#end tkinter display