#!/usr/bin/python
import simpleaudio as sa
import numpy as np
from time import sleep

def note_to_hertz(note):
    # This function converts a note to its assigned frequency
    dic ={
        "DO" : 264,
        "RE" : 297,
        "MI" : 330,
        "FA" : 352,
        "SOL": 396,
        "LA" : 440,
        "SI" : 495,
        "Z"  : -1,
    }
    return dic[note]


def shape_to_time(shape):
    # This function converts a shape to an amount of time in seconds
    dict_shape = {
        "r": 1,
        "b": 0.5,
        "n": 0.250,
        "c": 0.125,
        "p": -0.125
    }
    return dict_shape[shape]


def partition_to_list(partition):
    # This function transforms a string partition in a list with notes and their shapes separated in different list
    # values
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
    # This function plays a note for a duration of time equal to its shape
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
    # Main function that plays a partition for the user
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
