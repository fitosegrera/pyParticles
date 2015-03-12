#!/usr/bin python
from pyprocessing import *
import random
import time
import drop

class Emitter:
	def __init__(self, x, y, n):
		self.x = x
		self.y = y
		self.n = n
		self.interval = [None]*n
		self.startTime = [None]*n
		self.ellapsedTime = [None]*n
		for i in range(n):
			self.interval[i] = random.random() * 2
			self.startTime[i] = time.time()
		self.drops = [] 

	def generateSystem(self):
		for i in range(self.n):
			self.ellapsedTime[i] = time.time() - self.startTime[i]	
			if (self.ellapsedTime[i] > self.interval[i]):
				self.startTime[i] = time.time()
				self.drops.append(drop.Drop(self.x, self.y))
				
				print "---------------------------------"
				print "Interval:", self.interval[i]
				print "Start Time:", self.startTime[i]
				print "Ellapsed Time:", self.ellapsedTime[i]

		self.length = len(self.drops)
		for i in range(self.length):
			#print self.drops[i].y
			self.drops[i].update()