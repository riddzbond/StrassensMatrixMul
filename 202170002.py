# Python Program for implementing DFS on a Directed Graph using Adjacency List method (Recursive Method
# Riddhesh Bonde - 202170002

visitedNodes = set()  # Empty Set from storing visited nodes  
graph = {} # Empty Dictionary for storing the adjacency List
nodes = []
temp_list = []

def nodesInput():
	try: 
	    while True: 
	        nodes.append(int(input("Enter Nodes (press s to stop entering nodes) : ")))
	except: 
	    print(nodes)

def dictInput():
	for i in nodes:
		n = input("Enter Visited Nodes for " + str(i) + " (use ',' to seperate nodes or Enter 0 if Node hasn't visited) : ")
		if n == str(0):
			temp = []
		else:
			temp = n.split(",")
		graph[str(i)] = temp

	print(graph)


nodesInput()
dictInput()

# graph = {
#     '1' : ['2','3'],
#     '2' : ['4', '5'],
#     '3' : ['6'],
#     '4' : [],
#     '5' : ['6'],
#     '6' : []
# }


def dfs(visitedNodes, graph, node):
    if node not in visitedNodes:
        print (str(node) + "\t")
        visitedNodes.add(node)
        for neighbour in graph[node]:
        	dfs(visitedNodes, graph, neighbour)


firstNode = input("Start Traversing from Which Node: ")
print("DFS Traversal Output: \n")
dfs(visitedNodes, graph, firstNode)
