#!/usr/bin python
from pyprocessing import *
import emitter
import bucket
import stats

n = 5
e = [None]*n
b = [None]*n
s = [None]*n
cell = 0

def setup():
	global b, e, n, s, cell
	size(800, 800)
	gridSize = 11
	cell = width/gridSize
	buckInitPos = width/4
	for i in range(n):
		e[i] = emitter.Emitter(((i + (i+1))*cell) + cell/2, 100)
		b[i] = bucket.Bucket((i + (i+1))*cell, buckInitPos, gridSize)
		s[i] = stats.Stats((i + (i+1))*cell, height - height/10 + 20)

def draw():
	global b, e, n, cell
	background(0)
	line(cell/2, height - height/10, width - cell/2, height - height/10)
	for i in range(n):
		collided = e[i].generateSystem()
		b[i].display()
		#s[i].display(i)
		if collided == True:
			b[i].update()
		
run()