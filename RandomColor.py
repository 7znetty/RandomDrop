import random

def getColor():
    list = [0xffbf7f,
            0xffff7f,
            0xbfff7f,
            0x7fff7f,
            0x7fffbf,
            0x7fffff,
            0x7fbfff,
            0x7f7fff,
            0xbf7fff,
            0xff7fff,
            0xff7fbf,
            0xff7f7f]
    
    return random.choice(list)