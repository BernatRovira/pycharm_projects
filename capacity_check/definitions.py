#!/usr/bin/env python
import numpy as np



import time

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (time.clock() - self.start) * 1000.0
        print('Code block' + self.name + ' took: ' + str(self.took) + ' ms')
