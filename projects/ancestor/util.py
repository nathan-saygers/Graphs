
# Note: This Queue class is sub-optimal. Why?


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Breadth first traversal

        q = Queue()
        q.enqueue(starting_vertex)

        # Keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:
            # Dqueue first vert
            v = q.dequeue()

            # If it's not been visited
            if v not in visited:
                print(v)

                # Mark visited
                visited.add(v)

                # Queue up the neighbors of the dequeued / visited vertex
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        # Depth first traversal:

        s = Stack()
        s.push(starting_vertex)

        # Keep track of visited nodes
        visited = set()

        # Repeat until stack is empty
        while s.size() > 0:
            # Pop first vert
            v = s.pop()

            # If it's not been visisted
            if v not in visited:
                print(v)

                # Mark as visited
                visited.add(v)

                # add to the stack the neighbors of the popped vertex
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex):
        # create list for printing, at the end of function
        result = []
        # create an object for tracking which nodes have been visisted
        visited_log = {}
        # create helper function that accepts a vertex

        def dft(vertex):
            # Helper function returns early if the vert is empty
            if vertex == None:
                print('vertex == none')
                return
            # Helper function places the vertex it accepts into visisted
            visited_log[vertex] = True
            # Helper pushes visited vertex into result array
            result.append(vertex)
            # Loop over all the values in the adjancencyList for that vertex
            for neighbor in self.get_neighbors(vertex):
                # For any values not visited recursively invoke the hlper function on that vertex
                try:
                    if neighbor not in visited_log:
                        dft(neighbor)
                except KeyError:
                    continue
        # Invoke helper function with starting vertex
        dft(starting_vertex)
        # Return the result array
        for n in result:
            print(n)

    def bfs(self, starting_vertex, destination_vertex):
        # Breadth first traversal
        q = Queue()
        q.enqueue(starting_vertex)
        result = []

        # Keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:
            # Dqueue first vert
            v = q.dequeue()

            # If it's not been visited
            if v not in visited:
                result.append(v)

                # Mark visited
                visited.add(v)

                # Queue up the neighbors of the dequeued / visited vertex
                if v == destination_vertex:
                    return result

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dfs(self, starting_vertex, destination_vertex):
        # Depth first traversal:

        s = Stack()
        s.push(starting_vertex)
        result = []

        # Keep track of visited nodes
        visited = set()

        # Repeat until stack is empty
        while s.size() > 0:
            # Pop first vert
            v = s.pop()

            # If it's not been visited
            if v not in visited:
                result.append(v)

                # Mark as visited
                visited.add(v)

                if v == destination_vertex:
                    return result

                # add to the stack the neighbors of the popped vertex
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dfs_recursive(self, start_vert, target_value, visited=None, path=None):

        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(start_vert)

        # Copy the path list and add the new vert to the copy
        path = path + [start_vert]

        # Base Case
        if start_vert == target_value:
            return path

        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, target_value, visited, path)

                if new_path:
                    return new_path

        # return none if target not found
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
