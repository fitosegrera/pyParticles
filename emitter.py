#!/usr/bin python
from pyprocessing import *
import random
import time
import drop

class Emitter:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.interval = random.random() * 5
		self.startTime = time.time()
		self.ellapsedTime = 0
		self.drops = [] 

	def generateSystem(self):
		self.ellapsedTime = time.time() - self.startTime	
		if (self.ellapsedTime > self.interval):
			self.startTime = time.time()
			self.drops.append(drop.Drop(self.x, self.y))
			
			print "---------------------------------"
			print "Interval:", self.interval
			print "Start Time:", self.startTime
			print "Ellapsed Time:", self.ellapsedTime

		self.length = len(self.drops)
		for i in range(self.length):
			#print self.drops[i].y
			self.drops[i].update()