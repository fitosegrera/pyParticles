#!/usr/bin python
from pyprocessing import *

class Drop:

	#Setup a drop emitter
	def __init__(self, x, y):
		self.x = x
		self.r = 3
		self.y = 1
		self.speed = 1.2

	#update the speed of the particle by with its increment
	def update(self):
		self.y *= self.speed
		fill(255)
		ellipse(self.x, self.y, self.r, self.r)

	#Check if the drop reached the bottom of an obstacle
	def reachedBottom(self, dropPos, total):
		for i in range(total):
			if (self.y >= (dropPos - self.r*20)):
				return True
			else:
				return False