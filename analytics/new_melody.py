#!/usr/bin/python
from random import randint
from random import choice

partition = "SOLc p Zc SOLn LAn SOLn DOn Zc SIb SOLc p Zc SOLn LAn SOLn REn Zc DOb SOLc p Zc SOLn SOLn MIn DOn Zc SIn LAn FAc p Zc FAn MIn DOn REn DOr"

# This function creates 2 dictionaries that will help us apply markov law, one for the successive notes and one for
# the notes themselves and their number of occurrences
def dicnotes(partition):
    dicnote = {
        'DO': [], 'RE': [], 'MI': [], 'FA': [], 'SO': [], 'LA': [], 'SI': []
    }
    succdic = {
        'DO': [], 'RE': [], 'MI': [], 'FA': [], 'SO': [], 'LA': [], 'SI': []
    }
    split_part = partition.split(" ")
    for idx, note in enumerate(split_part):
        if note[:2] in dicnote:
            # we navigate the list using a slice of :2 to make it simpler to find notes by only comparing the first 2
            # letters and use the enumerate to avoid index errors
            dicnote[note[:2]].append(note)
            if idx != len(split_part)-1:
                if split_part[idx+1][0] != 'Z' and split_part[idx+1][0] != 'p':
                    # We do not add the silences as successors we will keep them in the same position to keep the same
                    # rythm
                    succdic[note[:2]].append(split_part[idx+1])
    return dicnote, succdic


# We will now use our dictionaries to apply markov law we will check on both dictionaries the presence of the notes and
# remove from the occurrences dictionary a note once we use it. When the dictionary is empty we have a new partition
# that follows markov's law
def markov_partition(partition):
    new_song = []
    dicnote, succdic = dicnotes(partition)
    lenght = len(dicnote["DO"])
    most_common_note = ""
    for note in dicnote:
        if lenght <= len(dicnote[note]):
            lenght = len(dicnote[note])
            most_common_note = note
    # Finds the most common note and its value
    randomvalue = randint(0, len(dicnote[most_common_note])-1)
    note = dicnote[most_common_note][randomvalue]
    dicnote[note[:2]].remove(note)
    while dicnote:
        # Main loop to create markov's partition
        if note[:2] in dicnote:
            randomvalue = randint(0, len(dicnote[note[:2]]) - 1)
            note = dicnote[note[:2]][randomvalue]
        else:
            key = choice(list(dicnote))
            randomvalue = randint(0, len(dicnote[key]) - 1)
            note = dicnote[key][randomvalue]
        dicnote[note[:2]].remove(note)
        note = succdic[note[:2]][randint(0, len(succdic[note[:2]]) - 1)]
        new_song.append(note)
        for key, value in list(dicnote.items()):
            if not value:
                del dicnote[key]
                del succdic[key]
    return new_song


def insert_silences(new_song, partition):
    # since it is not said on the project folder we decided we would keep all the silences at their positions to keep
    # the same rythm for our new song therefore this program adds the silences to the new partition at their respective
    # places
    silences_position = []
    final_song = []
    split_part = partition.split(" ")
    for idx, val in enumerate(split_part):
        # This loop checks where are the silences position in the main partition and get a tuple with its position and
        # value
        if val == "p" or val[:1] == "Z":
            silences_position.append((idx, val))
    for i in range(len(split_part)):
        # This loop compares both lists and adds silences at their respective positions while creating the final song
        # with the new_song variable gotten from the markov_partition() function
        if silences_position and silences_position[0][0] == i:
            silence = silences_position.pop(0)
            final_song.append(silence[1])
            # adds silence
        elif new_song:
            note = new_song.pop(0)
            final_song.append(note)
            # adds note
    return final_song
