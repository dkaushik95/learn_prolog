visited = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0
}
slt = {
    "A": 150,
    "B": 110,
    "C": 120,
    "D": 80,
    "E": 50,
    "F": 100,
    "G": 0
}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['B', 'D', 'F', 'G'],
    'F': ['B', 'E'],
    'G': ['D', 'E']
}


def find_path(graph, start, end, path=[]):
        visited[start] = 1
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        else:
            smallest = 999
            smallestkey = ''
            for node in graph[start]:
                if slt[node] < smallest:
                    if visited[node] == 1:
                        pass
                    else:
                        smallest = slt[node]
                        for x, y in slt.items():
                            if y == smallest:
                                smallestkey = x
            return find_path(graph, smallestkey, end, path)


def main():
    print graph.keys()
    start = raw_input("Enter the starting node from above: ")
    end = raw_input("Enter the goal node :")
    print "This is the path"
    print find_path(graph, start, end)

if __name__ == '__main__':
    main()
