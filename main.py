#!/usr/bin python
from pyprocessing import *
import emitter

e = emitter.Emitter(100, 100, 3)
def setup():
	size(800, 800)

def draw():
	global e
	background(0)
	e.generateSystem()

run()