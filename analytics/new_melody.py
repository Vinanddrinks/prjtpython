#!/usr/bin/python

partition = "SOLc SOLc SOLc LAn SOLn REn SOLc SOLc SOLc LAn SOLn REn DOc SIc LAc SIn DOc SIn LAn DOc SIc LAc SIn DOc SIn LAn SOLc SOLc SOLc LAn SOLn REn SOLc SOLc SOLc LAn SOLn REn"


def note_occurrences(partition):
    dicnote={

    }
    new_partition = ""
    for character in partition:
        if ascii("A") <= ascii(character) <= ascii('Z'):
            new_partition = new_partition + character
        if character == ' ':
            new_partition = new_partition + character
    new_partition = new_partition + " END"
    # we add this END value to help us avoid index errors later when coding for the successors notes
    note_list = new_partition.split()
    for element in note_list:
        if element not in dicnote:
            dicnote[element] = 0
            # creates a key and assigns 0 to its value
        if element in dicnote:
            dicnote[element] += 1
            # if element is already in dic increment the occurrences numbers by 1
    return note_list, dicnote


note_list, dicnote = note_occurrences(partition)

def successor_notes(note_list):
    succdic = {

    }
    for i in range(len(note_list) - 1):
        if note_list[i] not in succdic:
            succdic[note_list[i]] = note_list[i+1]
        if note_list[i] in succdic:
            succdic[note_list[i]] = note_list[i+1]
    return succdic



print(successor_notes(note_list))