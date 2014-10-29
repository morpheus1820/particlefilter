
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

		for i in range(100):
			self.predict()
			self.update([0])
			self.resample()


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
					print "posizione ",currentState, j
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

		for x in range(len(self.particles)): print self.particles[x].weight," ",
		print


	def resample(self):

		for x in range(len(self.particles)): print self.particles[x].state," ",
		print
		
		resampled=[]
		resampled=self.particles
		maxW=0
		for i in range(len(self.particles)):
			if self.particles[i].weight> maxW:
				maxW=self.particles[i].weight

	   	beta=0;
    		index=random.randint(0,self.numParticles)
    		for i in range(self.numParticles):
			beta=beta+random.random()*2*maxW
			while beta>self.particles[i].weight:
				beta=beta-self.particles[i].weight
				index=index+1
				if index==self.numParticles-1:
					index=index-self.numParticles+1
			
	
			resampled[i]=self.particles[index]

		self.particles=resampled

		for x in range(len(self.particles)): print self.particles[x].state," ",

ParticleFilter(20,np.array([[0.8,0.2],[0.2,0.8]]),np.array([[0.8,0.1,0.1],[0.4,0.4,0.2]]))


# function []=ParticleFilter(fwd_Noise,turn_Noise,sense_Noise,turn_Angle,distance,grid_Size,no_Particles,no_Robots,no_Iterations)
# myRobot=robot(grid_Size);
# C=[1,0,0;0,1,0;0,0,1];
# N=no_Particles;

# for i=1:N
#     particle=robot(grid_Size);
#     particle=particle.SetNoise(fwd_Noise,turn_Noise,sense_Noise);
#     P(i)=particle;
#     clear x;
# end

# for i=1:N
#     X(i)=P(i).x;
#     Y(i)=P(i).y;
#     O(i)=P(i).orientation;
# end

# disp(myRobot.eval(P));
# for k=1:no_Iterations
    
#     scatter(X,Y,10,[C(1,:)]);
#     set(gca,'XLim',[0,grid_Size],'YLim',[0,grid_Size]);
#     drawnow;
# %     linkdata on;
    
#     myRobot = myRobot.Move(turn_Angle,distance);
#     Z = myRobot.Sense();
    
#     for i=1:N
#         P(i)=P(i).Move(turn_Angle,distance);
#     end

#     for i=1:N
#         W(i)=P(i).measurementProb(Z);
#     end

#     norm=sum(W);
#     W=W./norm; %normalized weight array

#     mW=max(W);
#     beta=0;
#     index=randi(N);
#     for i=1:N
#         beta=beta+rand(1)*2*mW;
#         while(beta>W(index))
#             beta=beta-W(index);
#             index=index+1;
#             if(index==N)
#                 index=index-N+1;
#             end
#         end
#         P1(i)=P(index);
#     end
#     P=P1;
    
#     for i=1:N
#     X(i)=P(i).x;
#     Y(i)=P(i).y;
#     O(i)=P(i).orientation;
#     end
    
#     disp(myRobot.eval(P));
# end

# for i=1:N
#     X(i)=P(i).x;
#     Y(i)=P(i).y;
#     O(i)=P(i).orientation;
# end
# end
