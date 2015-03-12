#!/usr/bin python
from pyprocessing import *
import emitter
import bucket

n = 5
e = [None]*n
b = [None]*n

def setup():
	global e, n
	size(800, 800)
	gridSize = 11
	buckInitPos = width/4
	cell = width/gridSize
	for i in range(n):
		e[i] = emitter.Emitter(((i + (i+1))*cell) + cell/2, 100)
		b[i] = bucket.Bucket((i + (i+1))*cell, buckInitPos, gridSize)

def draw():
	global e, n
	background(0)
	for i in range(n):
		e[i].generateSystem()
		b[i].display()

run()