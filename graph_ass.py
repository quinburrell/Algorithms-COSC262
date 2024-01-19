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

def format_sequence(converters_info_str, source_format, destination_format):
    adj_list = adjacency_list(converters_info_str)  
    parent, distance = dijkstra(adj_list, source_format)
    result = [destination_format]
    if distance[destination_format] == inf:
        return 'No solution!'
    else:
        while result[0] != source_format:
            result = [parent[result[0]]] + result
        return result

def bfs_tree(adj_list, start):
    '''a bfs generating a parent array'''
    Q = []
    parents =[None] * len(adj_list)
    states = ['U'] * len(adj_list)
    states[start] = 'D'
    Q.append(start)
    while Q != []:
        state = Q.pop(0)
        for v in adj_list[state]:
            if states[v[0]] == 'U':
                states[v[0]] = 'D'
                parents[v[0]] = state
                Q.append(v[0])
        states[state] = 'P'
    return parents

def bubbles(physical_contact_info):
    '''returns a list lists, each of which is a component of the graph'''
    adj_list = adjacency_list(physical_contact_info) 
    explored = [False] * len(adj_list)
    if adj_list == []:
        return []
    result = []
    explore_next = 0
    while result == [] or explore_next not in bubble:
        parent = bfs_tree(adj_list, explore_next)
        bubble = [explore_next]
        explored[explore_next] = True
        for vert in range(len(parent)):
            if parent[vert] != None:
                bubble.append(vert)
                explored[vert] = True
            elif explore_next == bubble[0] and explored[vert] == False:
                explore_next = vert
        result.append(bubble)
    return result

def dfs_tree(adj_list, start):
    '''a dfs generating a parent array'''
    parents =[None] * len(adj_list)
    states = ['U'] * len(adj_list)
    states[start] = 'D'
    def dfs_loop(state):
        for v in adj_list[state]:
            if states[v[0]] == 'U':
                parents[v[0]] = state
                states[v[0]] = 'D'
                dfs_loop(v[0])
        states[state] = 'P'
    dfs_loop(start)
    return parents

def starting_order(dependencies):
    '''returns a valid topological ordering of a directed graph'''
    def dfs_loop(state):
        for v in adj_list[state]:
            if states[v[0]] == 'U':
                parents[v[0]] = state
                states[v[0]] = 'D'
                dfs_loop(v[0])
        states[state] = 'P'
        result.append(state)
    result = []
    adj_list = adjacency_list(dependencies)
    parents =[None] * len(adj_list)
    states = ['U'] * len(adj_list)    
    for vert in range(len(adj_list)):
        if states[vert] == 'U':
            dfs_loop(vert)  
    result.reverse()
    return result

def primms(adj, s):
    in_tree = [False] * len(adj)
    dist = [inf] * len(adj)
    parent = [None] * len(adj)
    dist[s] = 0
    while False in in_tree:
        u = next_vertex(in_tree, dist)
        in_tree[u] = True
        for v, weight in adj[u]:
            if not in_tree[v] and weight < dist[v]:
                dist[v] = weight
                parent[v] = u
    return parent, dist
    
def which_walkways(campus_map):
    '''finds the shortest connected tree'''
    result = []
    adj_list = adjacency_list(campus_map)
    parent, dist = primms(adj_list, 0)
    for edge in range(1, len(parent)):
        if edge > parent[edge]:
            result.append((parent[edge], edge))
        else:
            result.append((edge, parent[edge]))
    return result
            
def maximum_energy(city_map, depot_position):
    adj = adjacency_list(city_map)
    parent, dist = dijkstra(adj, depot_position)
    result = 0
    for distance in dist:
        if distance > result and distance != inf:
            result = distance
    return result * 2
            
	
city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(maximum_energy(city_map, 0))
print(maximum_energy(city_map, 1))
print(maximum_energy(city_map, 2))
        