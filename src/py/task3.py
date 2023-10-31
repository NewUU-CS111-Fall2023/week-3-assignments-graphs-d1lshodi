# * Author:Muxtorov Dilshod
# * Date:31.10.2023

def print_all_paths(graph, s, d):
    visited = [False] * len(graph)
    path = []
    dfs(graph, s, d, visited, path)

def dfs(graph, s, d, visited, path):
    visited[s] = True
    path.append(s)

    if s == d:
        print(path)
    else:
        for neighbor in graph[s]:
            if not visited[neighbor]:
                dfs(graph, neighbor, d, visited, path)

    path.pop()
    visited[s] = False