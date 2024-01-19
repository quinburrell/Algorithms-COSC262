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

def transpose(adj_list):
    result = [[]] * len(adj_list)
    for vertex in range(len(adj_list)):
        for edge in adj_list[vertex]:
            result[edge[0]] = result[edge[0]] + [(vertex, edge[1])]
    return result

def hub_check(adj_list, start):
    '''a dfs generating a parent array'''
    states = ['U'] * len(adj_list)
    states[start] = 'D'
    def dfs_loop(state):
        for v in adj_list[state]:
            if states[v[0]] == 'U':
                states[v[0]] = 'D'
                dfs_loop(v[0])
        states[state] = 'P'
    dfs_loop(start)
    if 'U' in states:
        return False
    else:
        return True

def is_strongly_connected(adj_list):
    if hub_check(adj_list, 0) == True:
        trans = transpose(adj_list)
        if hub_check(trans, 0) == True:
            return True
        else:
            return False
    else:
        return False
    
def next_vertex(in_tree, distance):
    current = None
    for i in range(len(in_tree)):
        if in_tree[i] == False:
            if current == None or distance[i] <= distance[current]:
                current = i
    return current

def dijkstra(adj_list, start):
    in_tree = [False] * len(adj_list)
    distance = [inf] * len(adj_list)
    parent = [None] * len(adj_list)
    distance[start] = 0
    last = None
    while False in in_tree:
        u = next_vertex(in_tree, distance)
        if u == last:
            break
        in_tree[u] = True
        for (v, weight) in adj_list[u]:
            if in_tree[v] == False and distance[u] + weight <= distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
        last = u
    return parent, distance

from math import inf
graph_string = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""
print(dijkstra(adjacency_list(graph_string), 0))
print(dijkstra(adjacency_list(graph_string), 2))