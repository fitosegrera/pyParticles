#!/usr/bin python
from pyprocessing import *

class Stats:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def display(self, i):
		textSize(10)
		text("Bucket#: " + str(i), self.x, self.y)