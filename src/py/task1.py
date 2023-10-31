def dfs(graph, start_node, visited):
    visited[start_node] = True
    print(start_node)

    for neighbor in graph[start_node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)



