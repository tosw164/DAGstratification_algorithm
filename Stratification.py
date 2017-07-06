import math

def getNodeIndex(node, node_list):
    if node in node_list:
        return node_list.index(node)
    else:
        for node_to_check in node_list:
            if isinstance(node_to_check, list):
                if node in node_to_check:
                    return node_list.index(node_to_check)

def getNodeStratification(node, stratif):
    for level in stratif:
        if node in level:
            return stratif.index(level)
        for entry in level:
            if isinstance(entry, list):
                if node in entry:
                    return stratif.index(level)



def createStratification(all_nodes, pred_nodes):
    global max_stratification
    stratification = []

    #Initialise empty stratification levels
    for i in range(len(all_nodes)):
        stratification.append([])

    solved = [False for i in range(len(all_nodes))]
    while False in solved:
        for i in range(len(all_nodes)):
            current_node = all_nodes[i]
            current_predecessors = pred_nodes[i]
            # print(current_node, current_predecessors)

            if not solved[i]:

                #if pred empty
                if len(current_predecessors) == 0:
                    #set to 0 in stratification
                    stratification[0].append(all_nodes[i])
                    #set solved = True
                    solved[i] = True

                else: #(node has predecessors)
                    #create list of stratifications
                    predicate_stratifications = []
                    #for each predecessor
                    for pred in current_predecessors:
                        #locate its index in all nodes list
                        pred_index = getNodeIndex(pred, all_nodes)
                        #if that level is solved
                        if solved[pred_index]:
                            #add its level to list
                            predicate_stratifications.append(getNodeStratification(pred, stratification))
                        else: #else
                            #add Infinity to list
                            predicate_stratifications.append(float('Inf'))

                        #if Infinity not in list
                        if float('Inf') not in predicate_stratifications:
                            #find max() and +1
                            new_stratification = max(predicate_stratifications) + 1

                            #update stratification max if need be
                            if new_stratification > max_stratification:
                                max_stratification = new_stratification

                            #add to stratification
                            stratification[new_stratification].append(current_node)

                            #set solved = True
                            solved[i] = True

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
    global non_DAG

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
                non_DAG = True
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
non_DAG = False
max_stratification = 0
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
rDFS()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if non_DAG:
    print("nonDAG")
else:
    print("DAG")

    # Does stratification
    finished_stratification = createStratification(modified_nodes_array, modified_predecessor_array)

    print(max_stratification+1)

    for i in range(max_stratification+1):
        current_stratification = finished_stratification[i]
        level = []
        for node in current_stratification:
            if node not in level:
                level.append(node)
        print(len(level))
        for node in level:
            if isinstance(node, list):
                print(" ".join(node))
            else:
                print(node)
