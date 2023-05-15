#--------------Depth First Search Algorithm--------------#

def depthFirstSearch(graph,bond,visited):
    if(bond not in visited):
        print(bond,end="->")
        visited.add(bond)
        for adjacency in graph[bond]:
            depthFirstSearch(graph,adjacency,visited)

#--------------------------------------------------------#

#Non-Directional Graph
graph1={'5':['3','7'],
       '3':['2','4','5'],
       '7':['5','8'],
       '2':['3'],
       '4':['3','8'],
       '8':['4','7']
}#While defining adjacency, traversing order changes according to order of the graph elements.

#Directional Graph 
graph2={'5':['3','7'], 
       '3':['2','4'],
       '7':['8'],
       '2':[],
       '4':['8'],
       '8':[]
}#If adjacencys are not connected to each-other algorithm can't continue

#----------------------------------------------------------#

visited=set()
print("Non-directional graph DFS:")
depthFirstSearch(graph1,'2',visited)

visited=set()
print("Directional graph BFS: ")
depthFirstSearch(graph2,'3',visited)