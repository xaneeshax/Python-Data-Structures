

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vetex = start_vertex
        self.target_vertex = target_vertex
        
        
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.predecessor = None
        self.min_distance = float('int')
        
        
class BellamnFord:
    def __init__(self, vertex_list, edge_list, start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False
        
    def find_shortest_path(self):
        self.start_vertex.min_distance = 0
        
        # so we consider V - 1 iterations
        for _ in range(len(self.vertex_list) - 1):
            
            # in every iteration we consider all the edges
            for edge in self.edge_list:
                # we have to calculate whether are there shorter paths
                u = edge.start_vertex
                v = edge.target_vertex
                
                dist = u.min_distance + edge.weight
                
                if dist < v.min_distance:
                    v.predecessor = u
                    v.min_distance = dist
                    
        # after we make V-1 iterations we haev to check negative cycles
        for edge in self.edge_list:
            if self.check_cycle(edge):
                print('Negative cycle detected...')
                return
            
    def check_cycle(self, edge):
        # if the total cost (min_distance) of a give vertex decreases
        # after V-1 iterations it means there is a negative cycle
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:
            self.has_cycle = True
            return True
        else:
            return False
        
    def get_shortest_path(self, vertex):
        if not self.has_cycle:
            print(f"Shortest path exists with value: {vertex.min_distance}")
            node = vertex 
            
            while node is not None:
                print(node.name)
                node = node.predecessor
        else:
            print('There is a negative cycle in teh G(V,E) graph')
            
            
        
            