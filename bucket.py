#!/usr/bin python
from pyprocessing import *

class Bucket:
	def __init__(self, x, y, gridSize):
		self.x = x
		self.y = y
		self.cell = width/gridSize

	def display(self):
		#Draw the bucket
		noFill()
		stroke(255)
		line(self.x, self.y, self.x + self.cell, self.y)
		line(self.x, self.y, self.x, self.y - self.cell + self.cell/8)
		line(self.x + self.cell, self.y, self.x + self.cell, self.y - self.cell + self.cell/8)
		return self.y

	def update(self):
		self.y += 1