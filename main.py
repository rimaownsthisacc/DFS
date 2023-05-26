from timeit import default_timer as timer
start = timer()

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': ['E','H'],
    'H': ['G', 'E', 'A']
}

visited = set()  # Set to keep track of visited nodes.
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(visited, graph, 'A')
end = timer()
res = end - start
final_time = res * 1000
print("the execution time is = ", final_time)
