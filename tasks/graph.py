from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = list()
        start = self._root
        stack = [start]

        while stack:
            start = stack.pop()
            if start in visited:
                continue
            visited.append(start)
            for i in reversed(range(len(start.outbound))):
                node = start.outbound[i]
                if node not in visited:
                    stack.append(node)
        return visited

    def bfs(self) -> list[Node]:
        visited = list()
        start = self._root
        queue = [start]

        while queue:
            start = queue.pop(0)
            if start in visited:
                continue
            visited.append(start)
            for node in start.outbound:
                if node not in visited:
                    queue.append(node)
        return visited

