import math

def createStratification(all_nodes, pred_nodes):
    global max_stratification
    stratification = []
    for i in range(len(all_nodes)):
        stratification.append([])

    solved = [False for i in range(len(all_nodes))]
    while False in solved:
        for node in all_nodes:
            current_index = all_nodes.index(node)
            if not solved[current_index]:
                if len(pred_nodes[current_index]) == 0: #strat = 0
                    stratification[0].append(all_nodes[current_index])
                    solved[current_index] = True

                    if 0 > max_stratification:
                        max_stratification = 0

                else: #Not stratification = 0
                    node_predicates = pred_nodes[current_index]
                    predicate_stratifications = [float('Inf') for x in range(len(node_predicates))]

                    for pred in node_predicates:
                        index = all_nodes.index([pred])
                        if solved[index]: #if already solved
                            #add its stratification to compare
                            for level in stratification:
                                level_number = stratification.index(level)
                                if [pred] in level:
                                    predicate_stratifications[node_predicates.index(pred)] = level_number
                                    break
                    if float('Inf') not in predicate_stratifications:
                        new_stratification = max(predicate_stratifications)+1

                        if new_stratification > max_stratification:
                            max_stratification = new_stratification

                        stratification[new_stratification].append(node)
                        solved[current_index] = True

    return stratification

def collapseCycle(cycle):
    new_node = []
    new_pred = []
    new_adj = []
    # print(modified_nodes_array)
    # print(modified_predecessor_array)
    # print(modified_adjacency_array)
    # print("c",cycle)
    # print(modified_nodes_array)
    # print(modified_predecessor_array)
    # print(modified_adjacency_array)
    for node in cycle:
        # print(node)
        node = [node]
        index = updated_nodes_array.index(node)
        new_node.append(node[0])
        for pred in predecessor_array[index]:
            new_pred.append(pred)
        for adj in adjacent_array[index]:
            new_adj.append(adj)

        index_to_remove = modified_nodes_array.index(node[0])
        # print(index_to_remove)
        modified_adjacency_array.pop(index_to_remove)
        modified_predecessor_array.pop(index_to_remove)
        modified_nodes_array.remove(node[0])

    for n in new_node:
        if n in new_adj:
            new_adj.remove(n)
        if n in new_pred:
            new_pred.remove(n)
    # print("nn",new_node)
    # print(new_pred)
    # print("na",new_adj)
    modified_nodes_array.append(new_node)
    modified_predecessor_array.append(list(set(new_pred)))
    modified_adjacency_array.append(list(set(new_adj)))


    # print(modified_nodes_array)
    # print(modified_predecessor_array)
    # print(modified_adjacency_array)


#DFS implementation, returns False if no
def recursiveDFS(nodes, edges, given_node):
    global original_nodes
    global nodes_visited
    global nodes_visited_list
    global modified_adjacency_array
    global modified_nodes_array
    global modified_predecessor_array

    # print("n",modified_nodes_array)
    # print("p",modified_predecessor_array)
    # print("a",modified_adjacency_array)

    # print(nodes, given_node)
    given_node_index = nodes.index(given_node)

    nodes_visited[given_node_index] = True
    nodes_visited_list.append(given_node)
    if given_node not in modified_nodes_array:
        modified_nodes_array.append(given_node)
        modified_adjacency_array.append(adjacent_array[given_node_index])
        modified_predecessor_array.append(predecessor_array[given_node_index])

    for node in edges[given_node_index]:
        # print("n,e,nds",node, edges[given_node_index], nodes)
        # print("nv",nodes_visited)
        # print(nodes,".", given_node)
        if not nodes_visited[original_nodes.index(node)]:
            # print(node)
            recursiveDFS(nodes, edges, node)
        else: #cycle possibly detected
            if node in nodes_visited_list: #cycle detected
                # print(nodes_visited_list)
                cycle_found = nodes_visited_list[nodes_visited_list.index(node):]
                # print("cycle: ",cycle_found)
                collapseCycle(cycle_found)
                nodes_visited_list.remove(given_node)
                return True
    # nodes_visited[given_node_index] = False
    nodes_visited_list.remove(given_node)

    return False



def rDFS():
    running = True
    while running:
        for node in modified_nodes_array:
            running = recursiveDFS(modified_nodes_array, modified_adjacency_array, node)
'''
1  procedure DFS(G,v):
2      label v as discovered
3      for all edges from v to w in G.adjacentEdges(v) do
4          if vertex w is not labeled as discovered then
5              recursively call DFS(G,w)
'''

#MAIN HERE~~~~~~~~~~~~~~~~~
#Arrays to populate that represent graph
max_stratification = -1
nodes_array = []
predecessor_array = []
adjacent_array = []

#Gets number of vertex
lines_to_get = int(input().rstrip())

#Process each vertex input
for i in range(lines_to_get):
    #Get input for line and convert to int from string
    line_input = input().rstrip().split(" ")

    #Populate arrays based on input
    for j in line_input:
        if j not in nodes_array:
            nodes_array.append(j)
            adjacent_array.append([])
            predecessor_array.append([])

    #Update predecessor array
    predecessor_array[nodes_array.index(line_input[1])].append(line_input[0])

    #Update Adjacent Array
    adjacent_array[nodes_array.index(line_input[0])].append(line_input[1])

#Makes the nodes array values into lists
updated_nodes_array = []
for node in nodes_array:
    updated_nodes_array.append([node])

# print(nodes_array)
# print(predecessor_array)
# print(adjacent_array)


#Check non recursive DFS
# DFSonUpdatesNodesArray()

#Check recursive DFS
original_nodes = []
for i in nodes_array:
    original_nodes.append(i)
nodes_visited = [False for i in range(len(nodes_array))]
nodes_visited_list = []
modified_nodes_array = []
for i in nodes_array:
    modified_nodes_array.append(i)
modified_predecessor_array = []
for i in predecessor_array:
    modified_predecessor_array.append(i)
modified_adjacency_array = []
for i in adjacent_array:
    modified_adjacency_array.append(i)
# recursiveDFS(updated_nodes_array, adjacent_array, updated_nodes_array[0][0])
rDFS()

for i in range(len(modified_nodes_array)):
    print(modified_nodes_array[i],modified_predecessor_array[i],modified_adjacency_array[i])
# print(modified_nodes_array)
# print(modified_predecessor_array)
# print(modified_adjacency_array)

#Does stratification
finished_stratification = createStratification(modified_nodes_array, modified_predecessor_array)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("DAG")
print(max_stratification+1)

for i in range(max_stratification+1):
    level = finished_stratification[i]
    print(len(level))
    for node in level:
        print(" ".join(node))

'''
Some algorithm
INPUTS: Vertices & Edges

set index = 0
set S = empty

for each vertex in V
    if index of vertex undefined
        call strongConnect(vertex)


def strongConnect(vertex)
    #set depth index of vertex to smallest unused index
    vertexindex = index
    vertex_lowlink = index

    index+=1
    push vertex onto S
    set v_onStack = TRUE
'''

'''
OLD Non recursive DFS

def DFSonUpdatesNodesArray():
    # DFS attempt:
    visited = [False for i in range(len(updated_nodes_array))]
    somestack = []
    somestack.append(updated_nodes_array[0])
    while len(somestack) > 0:
        current_node = somestack.pop()
        current_index = updated_nodes_array.index(current_node)

        if not visited[current_index]:
            visited[current_index] = True
            print(current_node)
            for adjacent_node in adjacent_array[current_index]:
                somestack.append([adjacent_node])'''
