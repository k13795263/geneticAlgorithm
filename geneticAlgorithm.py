#!/usr/bin/python3
import numpy as np

target = "to be or not to be"
intTarget = []
dnaLength = 18
maxima = 150


for i in range(len(target)):                     #transtation char to int
    intTarget.append(ord(target[i]))


def genes(dnaLength):
     gene = []
     for i in range(dnaLength):
        gene.append(np.random.randint(32, 128))
     return gene
        
def setPopulation(number, DnaLength):            # set population number
     population=[]
     for i in range(number):
        population.append(genes(DnaLength))
     return population

population = setPopulation(maxima, dnaLength)

def fitNess(length, pool, i, target):            
     score = 0
     for j in range(length):
         if pool[i][j] == target[j]:
             score += 1
     return score

     
def creatFitnessPool(pool, target):
     tempPool = []
     length = len(pool[0])
     for i in range(len(pool)):
         score = fitNess(length, pool, i,  target)
         n = (score / length)
         for j in range(round((n+0.01)*100)):
             tempPool.append(pool[i])
     print ('temppooi of length is', len(tempPool))
     return tempPool

matingPool = creatFitnessPool(population,intTarget)

def crossOver (populationNumber, pool):
     mutationRate = 0.01
     child = []
     length = len(pool[0])
     for i in range(populationNumber):
         temp = []
         a = np.random.randint(0, len(pool))
         b = np.random.randint(0, len(pool))
         midPoint = np.random.randint(0, length)
         for k in range(length):
             if (k > midPoint):
                 temp.append(pool[a][k])
             else:
                 temp.append(pool[b][k])
         for j in range(len(temp)):
             if (np.random.random(1) <= mutationRate): 
                 temp[j] = np.random.randint(32, 128)
         child.append(temp)
     
     return child
     
child = crossOver (maxima, matingPool)

def result(pool, length, populationNumber, target):
     value = 0
     while 1:
         i, j = np.shape(pool)
         value += 1
         temp = pool
         for a in range(i):
             if(temp[a] == target):
                 return value
         t = creatFitnessPool(temp, target)
         pool = crossOver (populationNumber, t)

r = result (child, dnaLength, maxima, intTarget)
print ("it is  %d heredity"%r)
