#--------------Breadth First Search Algorithm--------------#

queue=[]

def breadthFirstSearch(graph,bond): 
    visited.append(bond)
    queue.append(bond)
    while(queue):
        m=queue.pop(0)
        print(m,end="->")
        for adjacency in graph[m]:
            if (adjacency not in visited):
                visited.append(adjacency)
                queue.append(adjacency)

#----------------------------------------------------------#

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

graph3={'1':['2'],
       '2':['3','1'],
       '3':['4','2'],
       '4':['5','3'],
       '5':['6','4'],
       '6':['7','5'],
       '7':['6']
}

#----------------------------------------------------------#

visited=[]
print("Non-directional graph BFS: ")
breadthFirstSearch(graph1,'5')

visited=[]
print("Directional graph BFS: ")
breadthFirstSearch(graph2,'2')

visited=[]
print("Directional graph BFS: ")
breadthFirstSearch(graph3,'1')
