#!/usr/bin/python
# authors : Vincent Labouret, Giuliano Riccardi
# This folder is in the project to contain all the functions needed to play a function and manipulate strings from
# given to make them readable by the play() function and it does not take into account markov because it does not create
# new partitions but manipulates already existing ones
import simpleaudio as sa
import numpy as np
from time import sleep


def note_to_hertz(note):
    # This function converts a note to its assigned frequency it takes as input a string and returns an integer that is
    # the hertz frequency of the note
    dic ={
        "DO" : 264,
        "RE" : 297,
        "MI" : 330,
        "FA" : 352,
        "SOL": 396,
        "LA" : 440,
        "SI" : 495,
    }
    return dic[note]


def shape_to_time(shape):
    # This function converts a shape to an amount of time in seconds takes as input a string and returns a float value
    # that is the pause duration
    dict_shape = {
        "r": 1,
        "b": 0.5,
        "n": 0.250,
        "c": 0.125,
    }
    return dict_shape[shape]


def inversion_note(note):
    # This function inverses a note takes as input a string and returns a string
    # We will use the definition of an inverted note that was given in the python project to invert a note which is we
    # get the value of the note % len(inversion_list) of len(inversion_list) - note_position (that we get using .index
    # function)
    inversion_list = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    inversion_index = (len(inversion_list) - (inversion_list.index(note))) % (len(inversion_list))
    return inversion_list[inversion_index]


def transposition_note(note, transposition_value):
    # This function transposes a note it takes as input a string and an integer value and returns a string corresponding
    # to the transposed value of the note
    # We will get the transposition note by looking at the index of the note and then adding the transposition value
    # while keeping it all modulo len(transposition_list) to avoid indexing errors
    transposition_list = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    transposed_index = (transposition_list.index(note) + transposition_value) % (len(transposition_list))
    return transposition_list[transposed_index]


def partition_to_list(partition):
    # This function transforms a string partition in a list with notes and their shapes separated in different list
    # values it takes as input a string
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


def transposition_partition(partition, transposition_value):
    # This function transforms the partition in a transposed version of it ready to be played it takes as input a string
    # and an integer value (corresponding to the transposition value)
    partition = partition_to_list(partition)
    transposed_partition = []
    for note in partition:
        if ascii("A") <= ascii(note) <=ascii("Y"):
            transposed_partition.append(transposition_note(note, transposition_value))
        else:
            transposed_partition.append(note)
    return transposed_partition


def inversion_partition(partition):
    # This function transforms a partition in its inverted partition ready to be played it takes as input a string
    partition = partition_to_list(partition)
    inverted_partition = []
    for note in partition:
        if ascii("A") <= ascii(note) <= ascii("Y"):
            inverted_partition.append(inversion_note(note))
        else:
            inverted_partition.append(note)
    return inverted_partition


def play_note(note, shape):
    # This function plays a note for a duration of time equal to its shape it takes as input a string and another string
    # and returns nothing because it plays a sound instead
    # fade, fade_in, fade_out help to slowly get to the sin value for the "fade" first and last values of my sin wave
    # therefore helping the transition from a note to a silence to be smoother
    fade = 100
    fade_in = np.arange(0., 1., 1/fade)
    fade_out = np.arange(1., 0., -1/fade)
    frequency_note = note_to_hertz(note)
    duration = np.abs(shape_to_time(shape))
    note_array = np.linspace(0, duration, int(duration*44100), False)
    # note_array is the basis "duration" of the note
    # we create the note sine wave
    note = np.sin(frequency_note*note_array*2*np.pi)
    # we set the first and last 100 values of the sin wave to get to their values slowly reducing therefore clicking
    # sounds
    note[:fade] = np.multiply(note[:fade], fade_in)
    note[-fade:] = np.multiply(note[-fade:], fade_out)
    # the sound has to be on 16bit
    sound = note * (2**15 - 1) / np.max(np.abs(note))
    sound = sound.astype(np.int16)
    play_sound = sa.play_buffer(sound, 1, 2, 44100)
    play_sound.wait_done()


def play_partition(partition):
    # Main function that plays a partition for the user it takes as input a string and returns 0 if everything went
    # according to plan during its launching (it will play the partition)
    note_list = ["SOL", "LA", "SI", "RE", "MI", "FA", "DO"]
    note_shape = ["r", "b", "n", "c", "p"]
    partition = partition_to_list(partition)
    for index, element in enumerate(partition):
        if element in note_list:
            play_note(element, partition[index+1])
        if element == "p":
            sleep(0.125)
        if element == "Z":
            sleep_time = shape_to_time(partition[index+1])
            sleep(sleep_time)
    return 0


def main_transposition_play(partition, transposition_value):
    # this function transposes and plays a partition with an user given transposition value takes as value a string and
    # an integer and returns 0 if it was able to correctly play the string (returns sounds)
    note_list = ["SOL", "LA", "SI", "RE", "MI", "FA", "DO"]
    partition = transposition_partition(partition, transposition_value)
    for index, element in enumerate(partition):
        if element in note_list:
            play_note(element, partition[index+1])
        if element == "p":
            sleep(0.125)
        if element == "Z":
            sleep_time = shape_to_time(partition[index+1])
            sleep(sleep_time)
    return 0


def main_inversion_play(partition):
    # This function inverts and plays a partition given or chosen by the user takes as input a string and returns
    # 0 if it was able to correctly play the inverted string given (it will return sounds)
    note_list = ["SOL", "LA", "SI", "RE", "MI", "FA", "DO"]
    partition = inversion_partition(partition)
    for index, element in enumerate(partition):
        if element in note_list:
            play_note(element, partition[index+1])
        if element == "p":
            sleep(0.125)
        if element == "Z":
            sleep_time = shape_to_time(partition[index+1])
            sleep(sleep_time)
    return 0
