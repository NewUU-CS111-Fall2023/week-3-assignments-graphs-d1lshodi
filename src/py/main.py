# * Author:Muxtorov Dilshod
# * Date:31.10.2023
from task1 import dfs
from task3 import print_all_paths

print("Task 1")
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
visited = [False] * len(graph)
dfs(graph, 0, visited)

print("Task 2")


print("Task 3")

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
s = 2
d = 3
print_all_paths(graph, s, d) 

print("Task 4")


print("Task 5")


