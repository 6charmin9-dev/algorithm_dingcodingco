from collections import deque

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

'''
Q. 인접 리스트가 주어질 때, 모든 노드를 BFS 순서대로 방문하시오.
'''
def bfs_queue(adj_graph, start_node):
    # 구현해보세요!
    visited = []
    queue = deque([start_node])
    while queue:
        cur_node = queue.popleft()
        visited.append(cur_node)
        for neighbor in adj_graph[cur_node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!