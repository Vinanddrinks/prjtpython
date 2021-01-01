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
    partition_list = new_partition.split()
    for element in partition_list:
        if element not in dicnote:
            dicnote[element] = 1
            # creates a key and assigns 1 to its value
        if element in dicnote:
            dicnote[element] += 1
            # if element is already in dic increment the occurrences numbers by 1
    return partition_list, dicnote

print(note_occurrences(partition))