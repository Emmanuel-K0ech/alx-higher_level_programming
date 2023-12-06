#!/usr/bin/python3
def multiple_returns(sentence):
    letter = None
    length = 0
    if sentence is None or sentence == "":
        return length, letter
    else:
        length = len(sentence)
        letter = sentence[0]
        return length, letter
