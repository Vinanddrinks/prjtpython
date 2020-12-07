#!/usr/bin/python
def shape_to_time(shape):

    dict_shape = {
        "r": 1,
        "b": 0.5,
        "n": 0.250,
        "c": 0.125,
        "p": -0.125
    }
    return dict_shape[shape]

    print(shape_to_time("r"))