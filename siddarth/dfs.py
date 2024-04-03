graph={
    'p':['q','r','s'],
    'q':['p','r'],
    'r':['p','q','t'],
    's':['p'],
    't':['r']

}

visited=set()
def dfs(visited,graph,node):
    if node  not in graph:
        print("node is not persent in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(visited,graph,i)
print("following is the depth first search")
dfs(visited,graph,'p')
