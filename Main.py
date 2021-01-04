#!/usr/bin/python
# authors : Vincent Labouret
# tkinter using an event based structure the use of functions is very different
# with less return more use of global variable so all tkinter ode is in this file
# in order to isolate it from the logical part of the project wich is called as function here
# the use of tkinter is more detailled in the main window creation at the end of the file
# importation block
from read.playpartition import *
from files.readfile import *
from analytics.new_melody import *
import tkinter as tk
from dbmarkov import *
from pathlib import Path
# end of importation block
# database initialization using path to check json database existence
if Path('pdata.json').is_file():
    partidic = readfilejson()
else:
    partidic = readfiletxt()
# end database initialization
# tkinter commands button functions ( all the function that are called or depend of the widget button in the main menu)
# sheet adder

# validation of the fonction below using global to monitor Tk object type and the database
# it allocate the new partition in the database (partidic (dictionary))
# and close the ws wich is the event window
def nsv(title, sheet):
    global partidic, ws
    partidic[title] = sheet
    ws.destroy()

# create a window with a form to add a new entry in the partition dictionary
# it take as input two string on for the title one for the sheet 


def new_sheet():
    global partidic, title, sheet, ws

    ws = tk.Tk()
    ws.geometry("300x300")
    ws.config(bg="#7EAFE0")
    ws.title("Adding New sheet")
    #stringvar  is a type of string used in tkinter to monitor the value inputed in widget it depnd on a parent window
    title = tk.StringVar(ws)
    sheet = tk.StringVar(ws)
    #Frame() allow to create a frame to organize elements position in a window
    cadre = tk.Frame(ws, bg="#7EAFE0")
    cadre.pack(expand=tk.YES)
    #label() is a widget used to display text
    l1 = tk.Label(cadre, text="enter the title:",
                  font=("helvetica"), bg="#7EAFE0")
    l1.pack(expand=tk.YES)
    #Entry() is a widget used to have a string input
    E1 = tk.Entry(cadre, textvariable=title)
    E1.pack(expand=tk.YES, fill=tk.X)
    l2 = tk.Label(cadre, text="enter the sheet:",
                  font=("helvetica"), bg="#7EAFE0")
    l2.pack(expand=tk.YES)
    E2 = tk.Entry(cadre, textvariable=sheet)
    E2.pack(expand=tk.YES, fill=tk.X)
    validate = tk.Button(cadre, text="Validate",
                         command=lambda: nsv(title.get(), sheet.get()))
    validate.pack(expand=tk.YES, fill=tk.X, pady=10)
    cancel = tk.Button(cadre, text="Cancel", command=lambda: ws.destroy())
    cancel.pack(expand=tk.YES, fill=tk.X, pady=10)

    ws.mainloop()
# end sheet adder
# play sheet
# create a window with a form to play a sheet of the partition dictionary
# getting from partidic the list of key 
# allowing the user to choose between the songs and the method to play it with an integer input for transposition
def play():
    global partidic
    keys = []
    opt = ["simple play", "inversed play", "transposed play"]
    for key in partidic:
        keys.append(key)
    w = tk.Tk()
    w.geometry("300x300")
    w.config(bg="#7EAFE0")
    cursor = tk.StringVar(w)
    optc = tk.StringVar(w)
    tvc = tk.StringVar(w)
    tvc.set(0)
    w.title("play a music")
    f = tk.Frame(w, bg="#7EAFE0")
    f.pack(expand=tk.YES)
    l1 = tk.Label(f, text="choose a song:",
                  font=("helvetica"), bg="#7EAFE0")
    l1.pack(expand=tk.YES)
    #OptionMenu allow to make a visual list of choices for a user using a list to define the options of the menu
    # and a stringvar() to monitor the output
    om = tk.OptionMenu(f, cursor, *keys)
    om.pack(expand=tk.YES, fill=tk.X)
    l2 = tk.Label(f, text="choose a playing method:",
                  font=("helvetica"), bg="#7EAFE0")
    l2.pack(expand=tk.YES)
    opm = tk.OptionMenu(f, optc, *opt)
    opm.pack(expand=tk.YES, fill=tk.X)
    l3 = tk.Label(f, text="choose a transposition value:",
                  font=("helvetica"), bg="#7EAFE0")
    l3.pack(expand=tk.YES)
    E = tk.Entry(f, textvariable=tvc)
    E.pack(expand=tk.YES, fill=tk.X)
    E.insert(tk.END, '0')
    P = tk.Button(f, text="Play", command=lambda: play_2(
        partidic[cursor.get()], optc.get(), int(tvc.get())))
    P.pack(expand=tk.YES, fill=tk.X, pady=10)
    cancel = tk.Button(f, text="Quit", command=lambda: w.destroy())
    cancel.pack(expand=tk.YES, fill=tk.X, pady=10)
    w.mainloop()
# validate the form of the above function and call plays functions no need to return as it is an audio output


def play_2(partition, PC, tv):
    if PC == "simple play":
        play_partition(partition)
    if PC == "inversed play":
        main_inversion_play(partition)
    if PC == "transposed play":
        main_transposition_play(partition, tv)
# end play sheet
# markov solo
# create a window with a form to create a new partition based on a sheet of the database
# input : list of choice from partidic , string inpu for title 

def Markov():
    global partidic, w
    keys = []

    for key in partidic:
        keys.append(key)
    w = tk.Tk()
    w.geometry("300x300")
    w.config(bg="#7EAFE0")
    cursor = tk.StringVar(w)
    title = tk.StringVar(w)
    w.title("Markov derivation")
    f = tk.Frame(w, bg="#7EAFE0")
    f.pack(expand=tk.YES)
    l1 = tk.Label(f, text="choose a base sheet:",
                  font=("helvetica"), bg="#7EAFE0")
    l1.pack(expand=tk.YES)
    om = tk.OptionMenu(f, cursor, *keys)
    om.pack(expand=tk.YES, fill=tk.X)
    l2 = tk.Label(f, text="choose a title:",
                  font=("helvetica"), bg="#7EAFE0")
    l2.pack(expand=tk.YES)
    E = tk.Entry(f, textvariable=title)
    E.pack(expand=tk.YES)
    derive = tk.Button(f, text="Derive", command=lambda: Derive(
        cursor.get(), title.get()))
    derive.pack(expand=tk.YES, fill=tk.X, pady=10)
    cancel = tk.Button(f, text="Cancel", command=lambda: w.destroy())
    cancel.pack(expand=tk.YES, fill=tk.X, pady=10)
    w.mainloop()
# validation of the function above using global to access the database and the window variable
# input string fot title and partition as the dictionary key
# output new key and value in partidic it also destroy the event window w
def Derive(partition, title):
    global partidic, w
    partidic[title] = main_markov(partidic[partition])
    w.destroy()
# end markov solo
# markov db
# create a window with a form to create a new partition based on the database
# input integer: length of the partition, string: title of the new partition  

def Markovdb():
    global Windox
    Windox = tk.Tk()
    Windox.geometry("300x300")
    Windox.config(bg="#7EAFE0")
    f = tk.Frame(Windox, bg="#7EAFE0")
    f.pack(expand=tk.YES)
    l1 = tk.Label(f, text="choose a title:",
                  font=("helvetica"), bg="#7EAFE0")
    l1.pack(expand=tk.YES)
    cursor_t = tk.StringVar(Windox)
    cursor_l = tk.StringVar(Windox)
    cursor_l.set("30")
    E = tk.Entry(f, textvariable=cursor_t)
    E.pack(expand=tk.YES, fill=tk.X)
    l1 = tk.Label(f, text="choose a length in note number:",
                  font=("helvetica"), bg="#7EAFE0")
    l1.pack(expand=tk.YES)
    E1 = tk.Entry(f, textvariable=cursor_l)
    E1.pack(expand=tk.YES, fill=tk.X)
    validate = tk.Button(f, text="Derive", command=lambda: mdb(
        cursor_t.get(), int(cursor_l.get())))
    validate.pack(expand=tk.YES, fill=tk.X, pady=10)
    cancel = tk.Button(f, text="Cancel", command=lambda: Windox.destroy())
    cancel.pack(expand=tk.YES, fill=tk.X, pady=10)
    Windox.mainloop()
# validation of the above function using global to access database and widow variable
# output new dictionary entry with the partitions

def mdb(title, length):
    global partidic, Windox
    partidic[title] = db_markov(partidic, length)
    Windox.destroy()

# end markov db
# save and quit function
# create and write the dictionary partidic  in json file and breaking the mainloop of the program in order to stop it


def kill_save():
    global partidic, root
    writejson(partidic)
    root.destroy()
# end save and quit function
# end tkinter commands button functions


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
# frame configuration
cadre = tk.Frame(root, bg="#7EAFE0")
cadre.pack(expand=tk.YES)
# description title
desc = tk.Label(cadre, text="Welcome to Music and Statistic, a program to derive melody from others", font=(
    "Helvetica", 20), bg="#7EAFE0")
desc.pack(expand=tk.YES)
# end description title

# new sheet button
kills = tk.Button(cadre, text=" Add new sheet ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: new_sheet())
kills.pack(expand=tk.YES, fill=tk.X, pady=25)
# end new sheet button
killp = tk.Button(cadre, text=" Play sheet ", font=("Helvetica", 18),
                  bg="#FFFFFF", fg="#000000", command=lambda: play())
killp.pack(expand=tk.YES, fill=tk.X)
# Markov button
killM = tk.Button(cadre, text=" Markov derivation based on one music ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: Markov())
killM.pack(expand=tk.YES, fill=tk.X, pady=25)
# end Markov button
# Markov button
killMdb = tk.Button(cadre, text=" Markov derivation based on the whole database ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: Markovdb())
killMdb.pack(expand=tk.YES, fill=tk.X)
# end Markov button
# kill button
killSb = tk.Button(cadre, text=" Exit & save program ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: kill_save())
killSb.pack(expand=tk.YES, fill=tk.X, pady=25)
# end kill button
# kill button
killb = tk.Button(cadre, text=" Exit program ", font=(
    "Helvetica", 18), bg="#FFFFFF", fg="#000000", command=lambda: root.destroy())
killb.pack(expand=tk.YES, fill=tk.X)
# end kill button

root.mainloop()  # main loop indicator for tkinter window conditioning the event type program structure
# end tkinter display
