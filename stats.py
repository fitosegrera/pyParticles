#!/usr/bin python
from pyprocessing import *

PFont f;
f = loadFont("UbuntuMono-Regular-48.vlw")
textFont(f, 12)

class Stats:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def display(self, interval):
		text("Interval:" + str(interval), self.x, self.y)