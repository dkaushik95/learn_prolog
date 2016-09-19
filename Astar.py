slt = {
    "A": 150,
    "B": 110,
    "C": 120,
    "D": 80,
    "E": 50,
    "F": 100,
    "G": 0
}

cost = {
    "A": 50,
    "B": 10,
    "C": 20,
    "D": 40,
    "E": 50,
    "F": 10,
    "G": 0
}

visited = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
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

def find_path(graph, start, end, path=[], total_cost=0, hurestic={}):
        visited[start] = 1
        path = path + [start]
        total_cost += cost[start]
        if start == end:
        	smallest = 999
        	smallestnode = ''
        	for x, y in hurestic.items():
        		if smallest > y:
        			smallestnode = x
        			smallest = y
        	if smallest < slt[start] + cost[x]:
        		total_cost = hurestic[smallestnode]
        		return find_path(graph, start, end, path, total_cost, hurestic)
        	return path
        if start not in graph:
            return None
        else:
            smallest = 999
            smallestkey = ''
            for node in graph[start]:
                if slt[node] + cost[node] < smallest:
                    if visited[node] == 1:
                        pass
                    else:
                        smallest = slt[node] + cost[node]
                        total_cost += smallest
                        for x, y in slt.items():
                            if y == smallest:
                                smallestkey = x
                                hurestic[x] = (slt[x] + cost[x])
            return find_path(graph, smallestkey, end, path, total_cost, hurestic)
def main():
    print graph.keys()
    start = raw_input("Enter the starting node from above: ")
    end = raw_input("Enter the goal node :")
    print "This is the path"
    print find_path(graph, start, end)

if __name__ == '__main__':
    main()
