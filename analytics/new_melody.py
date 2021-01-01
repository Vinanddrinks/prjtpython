#!/usr/bin/python
from random import randint
from random import choice

partition = "SOLc SOLc SOLc LAn SOLn REn SOLc SOLc SOLc LAn SOLn REn DOc SIc LAc SIn DOc SIn LAn DOc SIc LAc SIn DOc SIn LAn SOLc SOLc SOLc LAn SOLn REn SOLc SOLc SOLc LAn SOLn REn"

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


new_song = markov_partition(partition)
print(new_song)
print(len(new_song))