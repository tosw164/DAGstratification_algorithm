import math
import time

def returnCycle(input_graph):
	return

def createStratification():
    global max_stratification
    stratification = []
    for i in range(len(updated_nodes_array)):
        stratification.append([])

    solved = [False for i in range(len(updated_nodes_array))]
    while False in solved:
        for node in updated_nodes_array:
            current_index = updated_nodes_array.index(node)
            if not solved[current_index]:
                if len(predecessor_array[current_index]) == 0: #strat = 0
                    stratification[0].append(updated_nodes_array[current_index])
                    solved[current_index] = True

                    if 0 > max_stratification:
                        max_stratification = 0

                else: #Not stratification = 0
                    node_predicates = predecessor_array[current_index]
                    predicate_stratifications = [float('Inf') for x in range(len(node_predicates))]

                    # print("notsolved",node)
                    # print('nodpred',node_predicates)
                    # print("predstra", predicate_stratifications)

                    for pred in node_predicates:
                        # print("p",pred)
                        # print(node_predicates)
                        index = updated_nodes_array.index([pred])
                        # print('i',index)
                        if solved[index]: #if already solved
                            #add its stratification to compare
                            for level in stratification:
                                level_number = stratification.index(level)
                                # print(level_number)
                                # print(pred,level)
                                if [pred] in level:
                                    predicate_stratifications[node_predicates.index(pred)] = level_number
                                    break
                    # print('ps',predicate_stratifications)
                    if float('Inf') not in predicate_stratifications:
                        new_stratification = max(predicate_stratifications)+1

                        if new_stratification > max_stratification:
                            max_stratification = new_stratification

                        stratification[new_stratification].append(node)
                        solved[current_index] = True

                    # print(node,"preds",node_predicates)

        # break
    #     print(stratification)
    #     print(solved)
    #     time.sleep(1)
    #
    # for s in stratification:
    #     print(s)

    return stratification

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
            for adjacent_node in adjacent_array[current_index]:
                somestack.append([adjacent_node])


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
    # line_input = [int(i) for i in input().rstrip().split(" ")]
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

updated_nodes_array = []
for node in nodes_array:
    updated_nodes_array.append([node])

# print("nodarray",nodes_array)
# print("updarray",updated_nodes_array)
# print("prdarray",predecessor_array)
# print("adjarray",adjacent_array)
finished_stratification = createStratification()

print("DAG")
print(max_stratification+1)

for i in range(max_stratification+1):
    level = finished_stratification[i]
    print(len(level))
    for node in level:
        print(" ".join(node))


# for i in range(len(nodes_array)):
    # print(nodes_array[i], "predicates",predecessor_array[i],"adjacents",adjacent_array[i])

