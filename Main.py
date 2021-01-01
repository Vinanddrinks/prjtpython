#!/usr/bin/python
#importation block
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

