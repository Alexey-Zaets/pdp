def dfs(graph: dict, start: str, visited: None | set = None) -> set:
    """
    graph = {
        'Amin': {'Wasim', 'Nick', 'Mike'},
        'Wasim': {'Imran', 'Amin'},
        'Imran': {'Wasim', 'Faras'},
        'Faras': {'Imran'},
        'Mike': {'Amin'},
        'Nick': {'Amin'},
    }
        """
    if visited is None:
        visited = set()

    visited.add(start)
    for next_item in graph[start] - visited:
        dfs(graph, next_item, visited)
    return visited