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

def reaching_vertices(adj_list, target):
    results = [target]
    for x in range(len(adj_list)):
        bfs_parents = bfs_tree(adj_list, x)
        if bfs_parents[target] is not None:
            results.append(x)
    return results

graph_string = """\
D 3
0 1
1 0
0 2
"""

adj_list = adjacency_list(graph_string)
print(sorted(reaching_vertices(adj_list, 0)))
print(sorted(reaching_vertices(adj_list, 1)))
print(sorted(reaching_vertices(adj_list, 2)))
