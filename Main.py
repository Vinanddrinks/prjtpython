#!/usr/bin/python
# importation block
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
# tkinter commands button functions
# sheet adder


def nsv(title,sheet):
    global partidic, ws
    partidic[title] = sheet
    ws.destroy()


def new_sheet():
    global partidic, title, sheet, ws

    ws = tk.Tk()
    ws.title("Adding New sheet")
    title = tk.StringVar(ws)
    sheet = tk.StringVar(ws)
    cadre = tk.Frame(ws, bg="#7EAFE0")
    cadre.pack(expand=tk.YES)
    l1 = tk.Label(cadre, text="enter the title:",
                  font=("helvetica"), bg="#7EAFE0")
    l1.pack(expand=tk.YES)
    E1 = tk.Entry(cadre, textvariable=title)
    E1.pack(expand=tk.YES)
    l2 = tk.Label(cadre, text="enter the sheet:",
                  font=("helvetica"), bg="#7EAFE0")
    l2.pack(expand=tk.YES)
    E2 = tk.Entry(cadre, textvariable=sheet)
    E2.pack(expand=tk.YES)
    validate = tk.Button(cadre, text="validate", command=lambda: nsv(title.get(),sheet.get()))
    validate.pack(expand=tk.YES)
    cancel = tk.Button(cadre, text="Cancel", command=lambda: wi.destroy())
    cancel.pack(expand=tk.YES)

    w.mainloop()
# end sheet adder
# play sheet
def play():
    global partidic
    keys = []
    opt =["simple play","inversed play","transposed play"]
    for key in partidic:
        keys.append(key)
    w = tk.Tk()
    cursor = tk.StringVar(w)
    optc = tk.StringVar(w)
    tvc = tk.StringVar(w)
    w.title("play a music")
    f = tk.Frame(w,bg = "#7EAFE0")
    f.pack(expand=tk.YES)
    om = tk.OptionMenu(f, cursor, *keys)
    om.pack(expand=tk.YES)
    opm = tk.OptionMenu(f, optc, *opt)
    opm.pack(expand=tk.YES)
    E = tk.Entry(f,textvariable=tvc)
    E.pack(expand=tk.YES)
    P = tk.Button(f, text="Play", command=lambda: play_2(partidic[cursor.get()],optc.get(),int(tvc.get())))
    P.pack(expand=tk.YES)
    cancel=tk.Button(f, text="quit", command=lambda: w.destroy())
    cancel.pack(expand=tk.YES)
    w.mainloop()
def play_2(partition,PC,tv):
    if PC == "simple play":
        play_partition(partition)
    if PC == "inversed play":
        main_inversion_play(partition)
    if PC == "transposed play":
        main_transposition_play(partition,tv) 
# end play sheet
# markov solo
def Markov():
    global partidic, w
    keys = []

    for key in partidic:
        keys.append(key)
    w = tk.Tk()
    cursor = tk.StringVar(w)
    title = tk.StringVar(w)
    w.title("Markov derivation")
    f = tk.Frame(w, bg="#7EAFE0")
    f.pack(expand=tk.YES)
    l1 = tk.Label(f, text="choose a base sheet:",
                  font=("helvetica"), bg="#7EAFE0")
    l1.pack(expand=tk.YES)
    om = tk.OptionMenu(f, cursor, *keys)
    om.pack(expand=tk.YES)
    l2 = tk.Label(f, text="choose a title:",
                  font=("helvetica"), bg="#7EAFE0")
    l2.pack(expand=tk.YES)
    E = tk.Entry(f,textvariable= title)
    E.pack(expand=tk.YES)
    derive = tk.Button(f, text="Derive", command=lambda: Derive(cursor.get(), title.get()))
    derive.pack(expand=tk.YES)
    cancel=tk.Button(f, text="Cancel", command=lambda: w.destroy())
    cancel.pack(expand=tk.YES)
    w.mainloop()
def Derive(partition, title):
    global partidic,w
    partidic[title] = main_markov(partidic[partition])
    w.destroy()
# end markov solo
def Markovdb():
    Windox = tk.Tk()
    Windox.mainloop()
# save and quit function
def kill_save():
    global partidic, root
    writejson(partidic)
    root.destroy()
# end save and quit function
# end tkinter commands button functions


# tkinter display
# main window settings
root=tk.Tk()
root.title("Music and Statistic")
root.geometry("1080x720")
root.minsize(480, 360)
root.maxsize(1920, 1080)
root.iconbitmap("root.ico")
root.config(bg="#7EAFE0")
# end main widow settings
# frame configuration
cadre=tk.Frame(root, bg="#7EAFE0")
cadre.pack(expand=tk.YES)
# description title
desc=tk.Label(cadre, text="Welcome to Music and Statistic, a program to derive melody from other's", font=(
    "Helvetica", 20), bg="#7EAFE0")
desc.pack(expand=tk.YES)
# end description title

# new sheet button
kills=tk.Button(cadre, text=" Add new sheet ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: new_sheet())
kills.pack(expand=tk.YES)
# end new sheet button
killp=tk.Button(cadre, text=" Play sheet ", font=("Helvetica", 18),
                bg="#FFFFFF", fg="#000000", command=lambda: play())
killp.pack(expand=tk.YES)
# Markov button
killM=tk.Button(cadre, text=" Markov derivation based on one music ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: Markov())
killM.pack(expand=tk.YES)
# end Markov button
# Markov button
killMdb=tk.Button(cadre, text=" Markov derivation based on the whole database ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: Markovdb())
killMdb.pack(expand=tk.YES)
# end Markov button
# kill button
killSb=tk.Button(cadre, text=" Exit & save program ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: kill_save())
killSb.pack(expand=tk.YES)
# end kill button
# kill button
killb=tk.Button(cadre, text=" Exit program ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: root.destroy())
killb.pack(expand=tk.YES)
# end kill button

root.mainloop()  # main loop indicator for tkinter window
# end tkinter display
