#!/usr/bin/python
# This function transforms a string partition in a list with notes and their shapes separated in different list values
def partition_to_list(partition):

    new_partition = ""
    for character in partition:
        if ascii("A") <= ascii(character) <= ascii('Z'):
            new_partition = new_partition + character
        if ascii('a') <= ascii(character) <= ascii("z"):
            new_partition = new_partition + " "
            new_partition = new_partition + character
        if character == ' ':
            new_partition = new_partition + character
    partition_list = new_partition.split()
    return partition_list

