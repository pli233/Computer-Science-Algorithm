import sys

class Graph:
    def __init__(self):
        self.graph = {}
        self.haschild = set()
    # function to add an edge to graph
    def addEdge(self,u,v):
        if v !="":
            self.haschild.add(u) 
        if u not in self.graph.keys():
            self.graph[u] = []
        self.graph[u].append(v)
    def hasChild(self,u):
        if u in self.haschild:
            return True
        return False
    
result = []   
def DFS(visited,graph,node):
    global result
    if node not in visited:
        #print(node, end=" ")
        result+=node
        result+= " "
        visited.add(node)
        if graph.hasChild(node):
            for child in graph.graph[node]:
                if child not in visited:
                    DFS(visited,graph,child)
        
#1. read files and store them line by line in a list


file_content= sys.stdin.read().splitlines()
contents_by_line = []
for i in file_content:
    contents_by_line.append(i.rstrip())

#2. extract how many instances do we have, 
# transfer it to int and delete it from the content list
instances_num = int(contents_by_line[0])
contents_by_line = contents_by_line[1:]

#3. add edges: use two for loop to do so
for instance in range(instances_num):
    #extract the number of nodes
    nodes_num = int(contents_by_line[0])
    #extract the instance
    current_instance = contents_by_line[1:nodes_num+1]
    #create a graph based on a instance
    graph = Graph()
    nodes_in_graph = []
    
    #each line in an instance represent a node, go through each line
    index = 0
    for line in current_instance:
        #transfer each line to a str list
        node_list = line.split(" ")
        #take out the current node, it is at the first place of a line
        main_node = node_list[0]
        nodes_in_graph.append(main_node)
        if(index ==0):
            root = main_node
        #the remain contents are nodes connect to the current node
        other_nodes = node_list[1:]
        #add edges to current instance graph
        for node in other_nodes:
            graph.addEdge(main_node,node)
        index+=1
            
    #4. use DFS to print the current graph
    visited = set()
    result = ""
    ans = ""
    for node in nodes_in_graph:
        if(node not in visited):
            DFS(visited,graph,node)
    print(result.rstrip())
    #delete content in the previous instance, continue for loop
    contents_by_line = contents_by_line[nodes_num+1:]

    