#!/usr/bin python
from pyprocessing import *

class Bucket:
	def __init__(self, x, y, gridSize):
		self.x = x
		self.y = y
		self.cell = width/gridSize

	def display(self):
		noFill()
		stroke(255)
		line(self.x, self.y, self.x + self.cell, self.y)