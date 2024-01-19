from math import inf 
def adjacency_list(graph_string):
    lines = graph_string.splitlines()
    for x in range(len(lines)):
        lines[x] = lines[x].split()
    if lines[0][0] == 'D':
        directed = True
    else:
        directed = False
    if len(lines[0]) == 3:
        weight = 0
    else:
        weight = None
    result = []
    for v in range(int(lines[0][1])):
        vertex = []
        for line in lines[1:]: 
            if weight != None:
                weight = int(line[2])
            if int(line[0]) == v:
                vertex.append((int(line[1]), weight))
            elif int(line[1]) == v and directed == False:
                vertex.append((int(line[0]), weight))
        result.append(vertex)
    return result

def distance_matrix(adj_list):
    result = []
    for vertex in range(len(adj_list)):
        temp = [inf] * len(adj_list)
        temp[vertex] = 0
        for edge in adj_list[vertex]:
            temp[edge[0]] = int(edge[1])
        result.append(temp)
    return result
        
def floyd(distance):
    for k in range(len(distance)):
        for i in range(len(distance)):
            for j in range(len(distance)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance
            