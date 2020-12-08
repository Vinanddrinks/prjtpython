#!/usr/bin/python
import simpleaudio as sa
import numpy as np

partition = "SOLc p Zc SOLn LAn SOLn DOn Zc SIb SOLc p Zc SOLn LAn SOLn REn Zc DOb SOLc p Zc SOLn SOLn MIn DOn Zc SIn LAn FAc p Zc FAn MIn DOn REn DOr"


def play_note(note, shape):
    frequency_note = note_to_hertz(note)
    duration = shape_to_time(shape)
    note_array = np.linspace(0, duration, duration*44100, False)
    # we create the note sine wave
    note = np.sin(frequency_note*note_array*2*np.pi)
    # the sound has to be on 16bit
    sound = note * (2**15 - 1) / np.max(np.abs(note))
    sound = sound.astype(np.int16)
    play_sound = sa.playbuffer(sound, 1, 2, 44100)
    play_sound.wait_done()



play_note("SOL", 'c')




