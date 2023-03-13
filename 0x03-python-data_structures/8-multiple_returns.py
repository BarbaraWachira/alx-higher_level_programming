#!/usr/bin/python3
def multiple_returns(sentence):
    i = 0
    if sentence:
        first = sentence[0]
    else:
        first = None
    for ch in sentence:
        i += 1
    res = (i, first)
    return (res)
