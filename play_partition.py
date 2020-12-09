#!/usr/bin/python
import simpleaudio as sa
import numpy as np
partition = "SOLc p Zc SOLn LAn SOLn DOn Zc SIb SOLc p Zc SOLn LAn SOLn REn Zc DOb SOLc p Zc SOLn SOLn MIn DOn Zc SIn LAn FAc p Zc FAn MIn DOn REn DOr"

def note_to_hertz(note):
    dic ={
        "DO" : 264,
        "RE" : 297,
        "MI" : 330,
        "FA" : 352,
        "SOL": 396,
        "LA" : 440,
        "SI" : 495,
        "Z"  : 0,
    }
    return dic[note]


def shape_to_time(shape):

    dict_shape = {
        "r": 1,
        "b": 0.5,
        "n": 0.250,
        "c": 0.125,
        "p": -0.125
    }
    return dict_shape[shape]


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


def play_note(note, shape):
    frequency_note = note_to_hertz(note)
    duration = shape_to_time(shape)
    note_array = np.linspace(0, duration, int(duration*44100), False)
    # we create the note sine wave
    note = np.sin(frequency_note*note_array*2*np.pi)
    # the sound has to be on 16bit
    sound = note * (2**15 - 1) / np.max(np.abs(note))
    sound = sound.astype(np.int16)
    play_sound = sa.play_buffer(sound, 1, 2, 44100)
    play_sound.wait_done()


def play_partition(partition):
    note_list = ["SOL", "LA", "SI", "RE", "MI", "FA", "DO"]
    note_shape = ["r", "b", "n", "c", "p"]
    partition = partition_to_list(partition)
    for element in partition:
        if element in note_list:
            return play_note(element, element)
        if element == "p":
            return play_note('Z', "p")


play_partition(partition)







