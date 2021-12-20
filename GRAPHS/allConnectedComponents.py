import queue

class GRAPH:
    def __init__(self,n):
        self.n = n
        self.adj = [[0]*n for i in range(n)]
        
    def addEdge(self,v1,v2):
        self.adj[v1][v2]=1
        self.adj[v2][v1]=1
        
    
    def bfs(self,visited,sv):
        if self.n==0:
            return 
        
        q = queue.Queue()
        q.put(sv)
        
        li = []
        li.append(sv)
        
        while not q.empty():
            node = q.get()
            visited[node]=True
            
            for i in range(self.n):
                if self.adj[node][i]==1 and visited[i]==False:
                    visited[i]=True
                    li.append(i)
                    q.put(i)
        
        li.sort()            
        for x in li:
            print(str(x),end=" ")
        
        
       
l = [int(x) for x in input().strip().split()]
vertices = l[0]
edges = l[1]

g = GRAPH(vertices)

for i in range(edges):
    edgPair = [int(x) for x in input().strip().split()]
    g.addEdge(edgPair[0], edgPair[1])
    

visited = [False for i in range(vertices)]
for i,x in enumerate(visited):
    if x==False:
        g.bfs(visited,i)
        print()
        
        