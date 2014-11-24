#!/usr/bin/env python

# code to map shortest path
# usage: 
# -l for list of members in graph
#
# TO DO
# -s for sorted list of members in graph
# functionise

import re, sys, Queue

# create classes for the graph functions
# need to put in external module, but need them here for lab (no extra modules/files)
#############################################################################################

# class for vertex/node information
class Vertex:
   # initialise new vertex
   def __init__(self, name):
      self.id = name
      self.connectedTo = {}
   
   # add connected nodes 
   def addNeighbor(self, neighbor, weight = 0):
      self.connectedTo[neighbor] = weight
   
   # return the string (for printing)
   def __str__(self):
      return str(self.id)# + ' connectedTo: ' + str([x.id for x in self.connectedTo])      

   # return the keys from teh connectedTo dict
   def getConnections(self):
      return self.connectedTo.keys()

   def getId(self):
      return self.id
   
   def getWeight(self, neighbor):
      return self.connectedTo[neighbor]



# graph data structure 
class Graph:
   # self referes to the object being called on
   def __init__(self):
      # init dict for vertices
      self.vertList = {}
      # init new vert count
      self.numVertices = 0
   
   # add a vertex to the graph, updating count etc.
   # better to use the add edge method below    
   def addVertex(self, name):
      # method called on graph, increments the vert count 
      self.numVertices = self.numVertices+1
      newVertex = Vertex(name)
      self.vertList[name] = newVertex
      return newVertex      

   # check a vertex and return its value etc. 
   def getVertex(self, vertex):
      if vertex in self.vertList:
         return self.vertList[vertex]
      else:
         return None
   
   # __contains__ used for:  'for key in object:' 
   def __contains__(self,vertex ):
      return vertex in self.vertList
      
   # add an edge, populate req. members of class   
   def addEdge(self, v1, v2, cost = 0):
      if v1 not in self.vertList:
         nv = self.addVertex(v1)
      if v2 not in self.vertList:
         nv = self.addVertex(v2)
      self.vertList[v1].addNeighbor(self.vertList[v2], cost)

   # return vert keys (ie, all the of the node names)
   def getVertices(self):
      return self.vertList.keys()
   
   # iterator for class
   def __iter__(self):
      return iter(self.vertList.values())
      
   def numVertices(self):
      return self.numVertices


#############################################################################################



if (len(sys.argv) < 3):
   sys.exit('Usage: %s <start location> <finish location>' % sys.argv[0])

lFlag = 0;
if (len(sys.argv) > 3 and sys.argv[1] == "-l"):
   lFlag = 1
   sys.argv.remove("-l")


# take in start/end locations for graph    
source = sys.argv[1]
target = sys.argv[2]



# CREATE GRAPH
newGraph = Graph()

# take in list of connections
for line in sys.stdin:
   line = line.rstrip('\n')
   wordList = str.split(line)
   
   if (len(wordList) != 3):
      print "Could not process input:", wordList, "incorrect number of variables"
      continue
   # need further checking here to sanitise input 
   
   # one addEdge here would make directed graph, want undirected   
   newGraph.addEdge(wordList[0], wordList[1], wordList[2])
   #add other direction at same time for undirected graph
   newGraph.addEdge(wordList[1], wordList[0], wordList[2])

# make sure source/taget are in graph
if (not(newGraph.getVertex(source)) or not(newGraph.getVertex(target))):
   sys.exit("Source or Target not in graph, exiting.")
    

#PRINT GRAPH OUT (DEBUG ONLY)
if (lFlag):  
   for v in newGraph:
      for w in v.getConnections():
         print("%s    \t=====>  \t%s   \t %s" % (v.getId(), w.getId(), v.getWeight(w) ) )
   sys.exit()





##FIND SHORTEST PATH   

distance = {}
distance[source] = 0
previous = {}
vertList = {}

printList = []


for vertex in newGraph:
   if (vertex != source):
      distance[vertex] = 9999999999
      previous[vertex] = "undefined"
      #print "'%s'" % vertex
   vertList[vertex] = distance[vertex]



# vertlist is now a "priorityqueue"
currentNode = newGraph.getVertex(source)
targetNode = newGraph.getVertex(target)

distance[currentNode] = 0

#print source

while(currentNode != targetNode ):

   del vertList[currentNode]
   
   connectionList = currentNode.getConnections()
   
   for vertex in  connectionList:
      
      altRoute = distance[currentNode] + int(currentNode.getWeight(vertex))
      #print altRoute      
            
      if (altRoute < distance[vertex]):
         distance[vertex] = altRoute
         previous[vertex] = currentNode
         vertList[vertex] = distance[vertex]

 
   currentNode = sorted(vertList, key=vertList.get)[0]

tempNode = targetNode
sumDistance = 0   
while (previous[tempNode] != "undefined"):
   printList.append(previous[tempNode])
   sumDistance += int(tempNode.getWeight(previous[tempNode]))
   tempNode = previous[tempNode]
   

print "Shortest route is length = ", sumDistance,":",  
        
while (len(printList)):
   print printList.pop(),
print target,"." 


