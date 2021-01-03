#!/usr/bin/python
from read.playpartition import *
from files.readfile import *
from analytics.new_melody import *
from pathlib import Path

# database initialization
if Path('pdata.json').is_file():
    partidic = readfilejson()
else:
    partidic = readfiletxt()
# end database initialization


def list_partidic(database_dictionary):
    list_partition = []
    conversion_list = ""
    for key in database_dictionary:
        if key != list(database_dictionary)[-1]:
            # we get all the partitions but the last entry because that value is not a note but a \n for a new line
            list_partition.append(database_dictionary[key][:-1])
    else:
        # if it is not the last element there is no \n to remove at the end
        list_partition.append(database_dictionary[key])
    for element in list_partition:
        conversion_list = conversion_list + element + " "
    conversion_list = conversion_list[:-1]
    # we remove last " "
    list_partition = conversion_list.split(" ")
    return list_partition


def db_markov(database_dictionary, partition_lenght):
    full_dbpartition = list_partidic(database_dictionary)
