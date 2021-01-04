#!/usr/bin/python
# authors : Giuliano Riccardi
# this file is here to apply Markov's Law on the whole database, it is not in the same file as the markov application
# on a song to make it easier to import other functions to use in this folder and also use the database dictionary
from read.playpartition import *
from files.readfile import *
from analytics.new_melody import *
from pathlib import Path
from random import randint


def list_partidic(database_dictionary):
    # Converts the database in a single partition list takes as variable a dictionary and returns a list
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


def succdic(partition):
    # This function gets the successive notes from a note inside a partition just like we did for applying markov's law
    # on a song it takes as variable a string and returns a dictionary
    note_list = ['DO', 'RE', 'MI', 'FA', 'SO', 'LA', 'SI', 'Z', 'p']
    succdic = {
        'DO': [], 'RE': [], 'MI': [], 'FA': [], 'SO': [], 'LA': [], 'SI': [], 'p': [], 'Z': []
    }
    for idx, note in enumerate(partition):
        if note != "Z" and note[:2] in note_list:
            if idx != len(partition)-1:
                succdic[note[:2]].append(partition[idx+1])
        if "Z" in note:
            if idx != len(partition)-1:
                succdic[note[:1]].append(partition[idx+1])
    return succdic


def db_markov(database_dictionary, partition_lenght):
    # applies the markov law on the whole database it takes as input the database as a dictionary and a user given
    # length of partition (silences are counted as elements of the partition) and returns a string ready to be played
    full_dbpartition = list_partidic(database_dictionary)
    successive_dic = succdic(full_dbpartition)
    most_common_note = 'DO'
    note_list = ['DO', 'RE', 'MI', 'FA', 'SO', 'LA', 'SI']
    markov_database = []
    string_song = ''
    # we find the most common note by seen which note has the most successors
    for key in successive_dic:
        if len(successive_dic[key]) >= len(successive_dic[most_common_note]):
            most_common_note = key
    # Now we start applying markov's law randomly as many times as the user asked for
    random_value = randint(0, len(successive_dic[most_common_note])-1)
    note = successive_dic[most_common_note][random_value]
    for i in range(partition_lenght):
        markov_database.append(note)
        if note[:1] == "Z":
            # We enter the case it is a silence duration
            random_value = randint(0, len(successive_dic[note[:1]]) - 1)
            note = successive_dic[note[:1]][random_value]
        if note == 'p':
            # We enter the case it is a pause
            random_value = randint(0, len(successive_dic[note]) - 1)
            note = successive_dic[note][random_value]
        if note[:2] in note_list:
            # We enter the case it is a note list
            random_value = randint(0, len(successive_dic[note[:2]])-1)
            note = successive_dic[note[:2]][random_value]
    # Now we have to convert this new partition in a string ready to be played by our play_music() function
    for element in markov_database:
        string_song = string_song + element + " "
    # We remove last " ".
    string_song = string_song[:-1]
    return string_song
