class Edge:
    
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
        
        
    
class Node:
    
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = float('inf')
        
        
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    
import heapq
class Djkistra:
    
    def __init__(self):
        self.heap = []
        
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        
        # iterate until the heap ain't empty
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            
            if actual_vertex.visited:
                continue
            
            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight
                
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(self.heap, v)
                    
            actual_vertex.visited = True
            
            
    def get_shortest_path(self, vertex):
        print(f"Shortest path to vertex: {vertex.min_distance}")
        
        actual_vertex = vertex
        while actual_vertex.predecessor is not None: 
            print(actual_vertex.name)
            actual_vertex = actual_vertex.predecessor
        
        
        
        
     
    