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

graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))

graph_string = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(dijkstra(adjacency_list(graph_string), 0))
print(dijkstra(adjacency_list(graph_string), 2))