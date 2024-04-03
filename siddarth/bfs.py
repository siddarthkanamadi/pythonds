garph={
    'p':['q','r','s'],
    'q':['p','r'],
    'r':['p','q','t'],
    's':['p'],
    't':['r'],
}  
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="")
        for neighbuor in graph[m]:
            if neighbuor not in visited:
                visited.append(neighbuor)
                queue.append(neighbuor)
print("following is the breadth -fisrt search")
bfs(visited,garph,'p')