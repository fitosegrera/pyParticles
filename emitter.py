#!/usr/bin python
from pyprocessing import *
import random
import time
import drop
import bucket

class Emitter:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.randomSeed = 10
		self.interval = random.random() * self.randomSeed
		self.startTime = time.time()
		self.ellapsedTime = 0
		self.drops = []
		self.dropCount = 0
		self.collision = []
		self.collided = False
		
	def generateSystem(self):
		self.ellapsedTime = time.time() - self.startTime	
		if (self.ellapsedTime > self.interval):
			self.startTime = time.time()
			self.drops.append(drop.Drop(self.x, self.y))
			self.dropCount += 1
			self.collision.append(False)

		for i in range(len(self.drops)):
			self.drops[i].update()
			self.collision[i] = self.drops[i].reachedBottom(self.y, self.dropCount)
			if self.collision[i]:
				self.collided = True
				self.drops.pop(i)
			else:
				self.collided = False
			return self.collided