#!/usr/bin/python

import numpy as np
import random


class Particle:
	def __init__(self,weight,state):
		self.weight = weight
		self.state=state



class ParticleFilter:

	def __init__(self, numParticles, transMatrix, obsMatrix):
		self.particles = []
		self.dim,self.dim=transMatrix.shape
		self.numParticles=numParticles
		self.transMatrix=transMatrix
		self.obsMatrix=obsMatrix

		for i in xrange(numParticles):
			self.particles.append( Particle(1/numParticles,random.randint(0,self.dim-1)) )
			#print self.particles[-1].state

		for i in range(10):
			self.predict()
			self.update([0])
			#self.resample()
                        self.resample()
                        for x in range(len(self.particles)): print self.particles[x].state,


	def predict(self):

		#for x in range(len(self.particles)): print self.particles[x].state," ",

		temp = []
		temp = self.particles

		for i in range(self.numParticles):
			currentState=self.particles[i].state
			rnd=random.random()

			for j in range(self.dim):
				if rnd<self.transMatrix[currentState][j]:
					temp[i].state=j
					#print "posizione ",currentState, j
					#print "confronto ",rnd," con ",self.transMatrix[currentState][j], "e minore, quindi", currentState, " diventa", j
				else:
					rnd-=self.transMatrix[currentState][j]

		self.particles=temp
		print
		#for x in range(len(self.particles)): print self.particles[x].state," ",


	def update(self,measures):


		for i in range(self.numParticles):

			self.particles[i].weight =1.0

			for j in range(len(measures)):
				self.particles[i].weight *= self.obsMatrix[self.particles[i].state][measures[j]]

		#for x in range(len(self.particles)): print self.particles[x].weight," ",

		temp=[]
		for i in range(len(self.particles)):
			temp.append(self.particles[i].weight)

		norm= np.linalg.norm(temp)
		for i in range(len(self.particles)):
			self.particles[i].weight /= norm

                for x in range(len(self.particles)): print("{0:.3f}".format(self.particles[x].weight)), 
		#print


	def resample(self):

        	#print "Before resampling:"
		#ifor x in range(len(self.particles)): print self.particles[x].state," ",
		#iprint

        	N=self.numParticles
        	weights=[]
		new_particles=[]
                index = int(random.random() * N)

		maxW=0

		for i in range(N):
            		weights.append(self.particles[i].weight)

        	beta = 0.0
        	mw = max(weights)
        	for i in range(N):
            		beta += random.random() * 2.0 * mw
            		#print "beta =", beta
            		while beta > weights[index]:
                		beta -= weights[index]
                		index = (index + 1) % N
                		#print "\tbeta= %f, index = %d, weight = %f" % (beta, index, weights[index])
            		new_particles.append(self.particles[index])

        	#print "After resampling:"
                #for x in range(len(self.particles)): print self.particles[x].state," ",
        	#print




ParticleFilter(20,np.array([[0.8,0.2],[0.2,0.8]]),np.array([[0.8,0.1,0.1],[0.4,0.4,0.2]]))


