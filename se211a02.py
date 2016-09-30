import math

def findFirstInstanceOf(n, list_to_search):
    # print(n,"in",list_to_search)

    if isinstance(n, list):
        n = n[0]

    for value in list_to_search:
        if isinstance(value, list):
            if n in value:
                return list_to_search.index(value)

    if n in list_to_search:
        return list_to_search.index(n)

    return float('Inf')

"""
Method that returns node index within list given
Also checks contents of sublists within given list
to see if it contains the given node
"""
def getNodeIndex(node, node_list):
    #Node not within sublist
    if node in node_list:
        return node_list.index(node)
    #Node in sublist
    else:
        #Check each element of list given
        for node_to_check in node_list:
            #if n'th element is a list, check if it contains node being checked
            if isinstance(node_to_check, list):
                #Return index of list if node found within sublist
                if node in node_to_check:
                    return node_list.index(node_to_check)

"""
Method that returns node stratification within list given
Also checks contents of sublists within given list
to see if it contains the given node
"""
def getNodeStratification(node, stratif):
    #Checks each level in stratification
    for level in stratif:
        #If node in a given level return it
        if node in level:
            return stratif.index(level)
        #Otherwise check each list within level to see if it contains node
        for entry in level:
            if isinstance(entry, list):
                #Return index checked if found
                if node in entry:
                    return stratif.index(level)

"""
Method that creates a stratification for a given list
of nodes and their respective predecessor nodes
"""
def createStratification(all_nodes, pred_nodes):
    global max_stratification #variable holding max stratification level so far
    stratification = [] #Stratification list to be returned by method

    #Initialise empty stratification levels
    for i in range(len(all_nodes)):
        stratification.append([])

    #Sets each node to be unsolved for now
    solved = [False for i in range(len(all_nodes))]

    #Continues until every node is marked solved
    while False in solved:
        #Go through each nodes (classes already collapsed)
        for i in range(len(all_nodes)):

            #Sets the current node and its predecessors being iterated through
            current_node = all_nodes[i]
            current_predecessors = pred_nodes[i]

            #If current node is not solved
            if not solved[i]:

                #if predecessor list is empty
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

    #Return generated stratification list
    return stratification

"""
Method that collapses a cycle found using the recursive Depth First Search (DFS)
below, and appends it to the modified arrays that will be stratified later
"""
'''
def collapseCycle(cycle_to_compute):
    print(cycle_to_compute)
    cycle = []
    for c in cycle_to_compute:
        if isinstance(c, list):
            for item in c:
                cycle.append(str(item))
        else:
            cycle.append(str(c))
    cycle = list(set(cycle))
    print("c",cycle)

    #Initialise arrays that will hold values as the values are removed from modified array
    new_node = []
    new_pred = []
    new_adj = []

    #Goes through all cycle nodes passed in
    for node in cycle:

        node = [node] #Set the current node to be list containing itself
        # print("upd",updated_nodes_array,"nod",node)
        index = updated_nodes_array.index(node) #Gets index of the node in the origin list
        new_node.append(node[0]) #Add current node to the new temp list

        #For each predecessor of current node in cycle, add that to temp list
        for pred in predecessor_array[index]:
            new_pred.append(pred)

        #For each adjacent node of current node, add that to temp list
        for adj in adjacent_array[index]:
            new_adj.append(adj)

        # print("nn", new_node)
        # print("np", new_pred)
        # print("na", new_adj)

        #Index of modified list to remove values from

        # index_to_remove = modified_nodes_array.index(node[0])
        index_to_remove = findFirstInstanceOf(node[0], modified_nodes_array)
        # print(modified_nodes_array,".",node,"..", index_to_remove)

        if index_to_remove is not False:
            #Remove current node from modified lists
            modified_adjacency_array.pop(index_to_remove)
            modified_predecessor_array.pop(index_to_remove)
            # print("modnod", modified_nodes_array, node)
            modified_nodes_array.pop(index_to_remove)

    # print("nn", new_node)
    # print("np", new_pred)
    # print("na", new_adj)

    #Remove all duplicate nodes in new collapsed adjacency & predecessor list
    # for n in new_node:
    #     if n in new_adj:
    #         new_adj.remove(n)
    #     if n in new_pred:
    #         new_pred.remove(n)
    # new_pred = list(set(new_pred))
    new_adj = list(set(new_adj))
    new_pred_temp = []
    new_adj_temp = []

    for n in new_adj:
        if n not in new_node:
            new_adj_temp.append(n)
    for n in new_pred:
        if n not in new_node:
            new_pred_temp.append(n)

    new_pred = new_pred_temp
    new_adj = new_adj_temp

    # print("nn", new_node)
    # print("np", new_pred)
    # print("na",new_adj)

    #Add new temp lists to modified lists (collapsed cycle)
    modified_nodes_array.append(new_node)
    modified_predecessor_array.append(list(set(new_pred)))
    modified_adjacency_array.append(list(set(new_adj)))

    print(modified_nodes_array,"modified nodes array AFTER COLLAPSE",len(modified_nodes_array))
    print(modified_predecessor_array,"pred",len(modified_predecessor_array))
    print(modified_adjacency_array,len(modified_adjacency_array),"\n~~~~")
''' #OLD VERSION
def collapseCycle(cycle_in):
    print("cycle found", cycle_in)
    global nodes_visited
    global nodes_visited_list
    global modified_nodes_array
    global modified_predecessor_array
    global modified_adjacency_array
    global nodes_array
    global predecessor_array
    global adjacent_array
    # new_node = []
    new_pred = []
    new_adj = []

    '''
    TODO

    NEED TO FIGURE OUT HOW TO GET ALL ELEMENTS OF COLLAPSED NODE IF PART OF IT IN THE CYCLE

    #flatten cycle
    cycle_to_process = []
    for node in cycle_in:
        if isinstance(node, list):
            for element in node:
                cycle_to_process.append(element)
        else:
            cycle_to_process.append(node)
    '''
    cycle_to_process = []
    for node in cycle_in:
        index_of_cycle_node = findFirstInstanceOf(node, modified_nodes_array)
        # if isinstance(modified_nodes_array[index_of_cycle_node], list) and len(modified_nodes_array[index_of_cycle_node]) > 1:
        if isinstance(modified_nodes_array[index_of_cycle_node], list):

            for i in modified_nodes_array[index_of_cycle_node]:
                cycle_to_process.append(i)
        else:
            cycle_to_process.append(node)



    #remove duplicates
    cycle_to_process = list(set(cycle_to_process))

    #for each value in cycle
    for value in cycle_to_process:
        #if value still in modified list
        # print("a", value, modified_nodes_array)
        index_of_value = findFirstInstanceOf(value, modified_nodes_array)

        if index_of_value != float('Inf'):
            #remove it from modified list, pred list and adj list
            modified_nodes_array.pop(index_of_value)
            modified_predecessor_array.pop(index_of_value)
            modified_adjacency_array.pop(index_of_value)

        #get pred and adj for that node from original unedited lists
        index_of_value_unedited_list = nodes_array.index(value)
        # print(predecessor_array[index_of_value_unedited_list],'aaa')
        for x in predecessor_array[index_of_value_unedited_list]:
            new_pred.append(x)
        for x in adjacent_array[index_of_value_unedited_list]:
            new_adj.append(x)
        # new_pred.append(predecessor_array[index_of_value_unedited_list])
        # new_adj.append(adjacent_array[index_of_value_unedited_list])

        # print('val', value)
        # print(cycle_to_process)
        # print(new_pred)
        # print(new_adj)



    #remove duplicates from new pred & adj lists
    cycle_to_process = list(set(cycle_to_process))
    new_pred = list(set(new_pred))
    new_adj = list(set(new_adj))

    #for each value in cycle
    for value in cycle_to_process:
        #if value in new pred, remove it
        if value in new_pred:
            new_pred.remove(value)
        #if value in new adj, remove it
    for value in cycle_to_process:
        if value in new_adj:
            new_adj.remove(value)

    #add new cycle to modified lists(3)
    modified_nodes_array.append(cycle_to_process)
    modified_predecessor_array.append(new_pred)
    modified_adjacency_array.append(new_adj)

    print(cycle_to_process,'c')
    print(new_pred,'p')
    print(new_adj,'a')
    print("collapsed", cycle_to_process)


"""
Method that implements a modified recursive Depth First Search (DFS)
algorithm to check for cycles, collapse them and populate a list data structure
representing list of nodes (and collapsed cycles) to stratisfy

Takes the modified node array, edge array, and node to process as inputs
and recursively calls itself on adjacent nodes to current node
"""
'''
def recursiveDFS(nodes, edges, given_node):
    #Allows usage of variables created in main
    global original_nodes
    global nodes_visited
    global nodes_visited_list
    global modified_adjacency_array
    global modified_nodes_array
    global modified_predecessor_array
    global non_DAG

    global cycle_found

    #Index of current node in the modified list
    given_node_index = nodes.index(given_node)

    #Flags current node as visited and adds it to visited history list
    nodes_visited[given_node_index] = True
    nodes_visited_list.append(given_node)

    # print("nod",nodes)
    # print("nvl",nodes_visited_list)
    # print("\t\tnodes", nodes)

    #For each node adjacent to current node
    for node in edges[given_node_index]:
        # print("node",given_node,"edge",node)
        #if node hasn't already been visited
        if not nodes_visited[original_nodes.index(node)]:
            check = recursiveDFS(nodes, edges, node) #Call this method on that node
            if check:
                return True
        #If node has been visited already(cycle possibly detected)
        else:
            # cycle detected
            # for n in nodes_visited_list:

            found_or_not = findFirstInstanceOf(node, nodes_visited_list)
            # print("asdf.",nodes,"\nasdf",node, nodes_visited_list, found_or_not)
            if found_or_not is not False:
            # if node in nodes_visited_list:
            #     nodes_visited_list.append(node)

                #Saves values of cycle detected
                # if found_or_not is not False and found_or_not != 0:
                #     cycle_found = nodes_visited_list[found_or_not-1:]
                # else:
                #     cycle_found = nodes_visited_list[0:]
                cycle_found = nodes_visited_list[found_or_not:]
                print("Node visited list",nodes_visited_list,"current", node)


                #Calls collapse cycle method, to remove cycle and add new node representing cycle
                collapseCycle(cycle_found)

                #Remove current node from history
                nodes_visited_list.remove(given_node)

                #Set flag. Therefore digraph is not DAG
                non_DAG = True

                cycle_found = True

                #Return that cycle was found for this start node
                return True

    #Remove current node from history list (branch already processed)
    nodes_visited_list.remove(given_node)

    #Return that cycle was not found for this start node
    return False
''' #OLD VERSION
def recursiveDFS(node_in):
    global nodes_visited
    global nodes_visited_list
    global cycle_found
    global non_DAG

    if isinstance(node_in, list) and len(node_in) == 1:
        node_in = node_in[0]

    #get index of current node in modified list
    index_of_node = findFirstInstanceOf(node_in, modified_nodes_array)

    # print(index_of_node,'noind')
    #set this node to visited
    nodes_visited[index_of_node] = True
    #add this node to visited list
    nodes_visited_list.append(node_in)
    # print(node_in,nodes_visited_list,"noin, novilist")

    print('dfs_start noin', node_in, 'adjs', modified_adjacency_array[index_of_node])


    # print(node_in, modified_nodes_array,'noin, monoar', nodes_visited_list)

    #for each node adjacent to current node
    for adjacent_node in modified_adjacency_array[index_of_node]:
        # print("adjnod monoa")
        adjacent_node_index = findFirstInstanceOf(adjacent_node, modified_nodes_array)

        print('adjno & index', adjacent_node, adjacent_node_index,'noin',node_in)
        # print(nodes_visited)

        #If nod hasn't been visited yet
        if not nodes_visited[adjacent_node_index]:
            #call recurisve() on it
            recursiveDFS(adjacent_node)

            #KILL RECURSION SOME MORE
            if cycle_found:
                return

         #else if node has been visited (cycle detected)
        else:
            # if findFirstInstanceOf(adjacent_array, nodes_visited_list) is float('Inf'):
            if True:
                print('alreadyvisit', adjacent_node, nodes_visited_list)
                #Identify path from first occurence of repeated node to second time
                first_occurence_index = findFirstInstanceOf(adjacent_node, nodes_visited_list)

                if first_occurence_index != float('Inf'):

                    cycle_to_collapse = nodes_visited_list[first_occurence_index:]
                    # print('nod', adjacent_node, 'novilist', nodes_visited_list, 'fiocin', first_occurence_index)

                    #Collapse() this cycle
                    print('cycletocollapse', cycle_to_collapse, nodes_visited_list, adjacent_node)
                    collapseCycle(cycle_to_collapse)

                    #set non_DAG and start_again
                    non_DAG = True
                    cycle_found = True

                    #KILL RECURISON HERE
                    return

    print('allgood',nodes_visited_list)
    nodes_visited_list.remove(node_in)
    return

"""
Method that calls the recursive DFS method above until no more cycles were found and processed
"""
'''
def DfsCollapseAllCycles():
    global cycle_found

    cycle_found = False

    running = True
    # while running:
    for z in range(10000):
        #Setting to False here terminates while loop if 0 cycles found and processed
        #Doing DFS on all nodes
        running = False
        nodes_visited = [False for i in range(len(modified_nodes_array))]

        # print("~~~~~~~~~~~~~~~\n",modified_nodes_array)
        # print(modified_predecessor_array)
        # print(modified_adjacency_array)

        #Calls the recursive DFS algorithm on each node in modified list
        print("start again")
        for node in modified_nodes_array:
            #If True returned (Cycle/s found and processed) then run for loop again
            checks = recursiveDFS(modified_nodes_array, modified_adjacency_array, node)
            # if recursiveDFS(modified_nodes_array, modified_adjacency_array, node):
            # running = True
            # print(cycle_found)
            if checks:
                # print('yay')
                running = True
                cycle_found = False
                break
        # print("b",running)
''' #OLD VERSION
def DfsCollapseAllCycles():
    global cycle_found
    global non_DAG
    global nodes_visited_list
    global nodes_visited

    print(modified_nodes_array)

    while True:
        cycle_found = False
        for node in modified_nodes_array:

            print('~~~~\n',modified_nodes_array, "modified nodes array START", len(modified_nodes_array))
            print(modified_predecessor_array, "pred", len(modified_predecessor_array))
            print(modified_adjacency_array, len(modified_adjacency_array), "\n~~~~")

            nodes_visited = [False for i in range(len(modified_nodes_array))]
            nodes_visited_list = []

            print('novi', nodes_visited,'novili', nodes_visited_list)
            recursiveDFS(node)
            print('cyfo',cycle_found)
            if cycle_found:
                break
            else:
                return
        # break




"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MAIN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Initialisation: Inputs and variable collection. Processing digraph too.
"""

non_DAG = False         #Flag signifying if any cycles found (DAG or not)
max_stratification = 0  #Maximum stratification level populated when doing stratification
nodes_array = []        #Original nodes list created when getting inputs
predecessor_array = []  #Original predecessors of nodes obtained after getting inputs
adjacent_array = []     #Original adjacent nodes of nodes obtained after getting inputs

cycle_found = False

#Gets number of vertex
lines_to_get = int(input().rstrip())

#Process each vertex input
for i in range(lines_to_get):
    #Get input of edge
    line_input = input().rstrip().split(" ")
    for x in range(len(line_input)):
        line_input[x] = int(line_input[x])

    #For each node in input
    for j in line_input:
        #If not already seen
        if j not in nodes_array:
            nodes_array.append(j)         #Add it to nodes array
            adjacent_array.append([])     #Initialise adjacency list for that node
            predecessor_array.append([])  #Initialise predecessor list for that node

    #Update predecessor array from line input
    predecessor_array[nodes_array.index(line_input[1])].append(line_input[0])

    #Update Adjacent Array form line input
    adjacent_array[nodes_array.index(line_input[0])].append(line_input[1])

#Makes the nodes array values into lists
updated_nodes_array = []
for node in nodes_array:
    updated_nodes_array.append([node])

#Create copy of original nodes from input
original_nodes = []
for i in nodes_array:
    original_nodes.append(i)

#Create list of booleans representing if node has been visited or not (for DFS)
nodes_visited = [False for i in range(len(nodes_array))]
nodes_visited_list = []

#Create editable list used to represent nodes after collapsing cycles
modified_nodes_array = []
for i in nodes_array:
    modified_nodes_array.append(i)

#Create editable list used to represent node predecessors after cycle collapses
modified_predecessor_array = []
for i in predecessor_array:
    modified_predecessor_array.append(i)

#Create editable list used to represent adjacent nodes after cycle collapses
modified_adjacency_array = []
for i in adjacent_array:
    modified_adjacency_array.append(i)
# collapseCycle([[2,3],1])

print(modified_nodes_array, "modified nodes array START", len(modified_nodes_array))
print(modified_predecessor_array, "pred", len(modified_predecessor_array))
print(modified_adjacency_array, len(modified_adjacency_array), "\n~~~~")
#Call method to iteratively perform Depth First Search to collapse all cycles in digraph
DfsCollapseAllCycles()

"""
PRINTING OF OUTPUT
"""

print(modified_nodes_array, "fin")
print(modified_predecessor_array,"pred")
print(modified_adjacency_array)


#Prints depending on state of flag set above
if non_DAG:
    print("nonDAG")
else:
    print("DAG")



# Does stratification on modified lists created from DFS
finished_stratification = createStratification(modified_nodes_array, modified_predecessor_array)

#Prints number of stratification levels generated
print(max_stratification+1)

#For each level in stratification, print nodes
for i in range(max_stratification+1):

    #Hold all nodes within stratification in list
    current_stratification = finished_stratification[i]
    level = []
    for node in current_stratification:
        if node not in level:
            level.append(node)

    #Print number of nodes in level
    print(len(level))

    #For each node print its value (or values if collapsed cycle)
    for node in level:
        if isinstance(node, list):
            print(" ".join([str(i)for i in node]))
        else:
            print(node)
