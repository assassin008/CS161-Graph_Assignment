def read_graph(file_path):
    graph = {}
    rev_graph = {}
    with open(file_path, 'r') as f:
        for line in f:
            tail, head = map(int, line.split())
            if tail not in graph:
                graph[tail] = []
            if head not in rev_graph:
                rev_graph[head] = []
            graph[tail].append(head)
            rev_graph[head].append(tail)
    return graph, rev_graph

def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph.get(node, []):
        if not visited.get(neighbor, False):
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def reverse_dfs(graph, node, visited, scc):
    visited[node] = True
    scc.add(node)
    for neighbor in graph.get(node, []):
        if not visited.get(neighbor, False):
            reverse_dfs(graph, neighbor, visited, scc)

def kosaraju(graph, rev_graph):
    visited = {}
    stack = []
    for node in graph:
        if not visited.get(node, False):
            dfs(graph, node, visited, stack)

    visited = {}
    sccs = []
    while stack:
        node = stack.pop()
        if not visited.get(node, False):
            scc = set()
            reverse_dfs(rev_graph, node, visited, scc)
            sccs.append(scc)
    return sccs

def main(file_path):
    graph, rev_graph = read_graph(file_path)
    sccs = kosaraju(graph, rev_graph)
    scc_sizes = sorted([len(scc) for scc in sccs], reverse=True)
    print(','.join(map(str, scc_sizes[:5])))

if __name__ == '__main__':
    main('/mnt/data/file2.txt')
