def main():
    G = read_graph()
    start, finish = input('Введи начало и конец: ').split()
    shortest_distances = dijkstra(G, start)
    shortest_path = get_path(G, shortest_distances, finish)
    print("Len: "+ str(shortest_distances[finish])+",", f'Кратчайший путь: ', *shortest_path)


def get_path(G, shortest_distances, finish):
    path = [finish]
    distance = shortest_distances[finish]
    while distance != 0:
        for neigh, weight in G[finish].items():
            if distance == shortest_distances[neigh] + int(weight):
                path.append(neigh)
                distance = shortest_distances[neigh]
                finish = neigh
    return path[::-1]


def dijkstra(G, start):
    from collections import deque
    deque = deque()
    short_dist = {start: 0}
    deque.append(start)
    while deque:
        curr = deque.popleft()
        for neigh in G[curr]:
            if neigh not in short_dist or short_dist[curr] + int(G[curr][neigh]) < short_dist[neigh]:
                short_dist[neigh] = short_dist[curr] + int(G[curr][neigh])
                deque.append(neigh)
    return short_dist


def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight


def read_graph():
    G = {}
    with open('graph1.txt', 'r') as txt:
        for lineString in txt:
            a, b, weight = lineString.split()
            add_edge(G, a, b, weight)
            add_edge(G, b, a, weight)
    return G


if __name__ == '__main__':
    main()