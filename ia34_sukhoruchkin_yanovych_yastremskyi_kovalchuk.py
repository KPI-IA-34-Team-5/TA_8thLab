class GraphColoring:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.vertices = list(adjacency_list.keys())
        self.color_map = {}
        self.colors = []

    def is_valid(self, vertex, color):
        for neighbor in self.adjacency_list[vertex]:
            if neighbor in self.color_map and self.color_map[neighbor] == color:
                return False
        return True

    def get_mrv_vertex(self):
        uncolored_vertices = [v for v in self.vertices if v not in self.color_map]
        mrv_vertex = None
        min_colors = float('inf')
        for vertex in uncolored_vertices:
            available_colors = sum(1 for color in self.colors if self.is_valid(vertex, color))
            if available_colors < min_colors:
                min_colors = available_colors
                mrv_vertex = vertex
        return mrv_vertex

    def backtrack(self):
        if len(self.color_map) == len(self.vertices):
            return True
        vertex = self.get_mrv_vertex()
        for color in self.colors:
            if self.is_valid(vertex, color):
                self.color_map[vertex] = color
                if self.backtrack():
                    return True
                del self.color_map[vertex]
        return False

    def find_chromatic_number(self):
        for chromatic_number in range(1, len(self.vertices) + 1):
            self.colors = list(range(chromatic_number))
            self.color_map = {}
            if self.backtrack():
                return chromatic_number, self.color_map
        return None, None
    
    def validate(self):
        to_append = []
        for i, ii in self.adjacency_list.items():
            for j in ii:
                if not (j in self.adjacency_list):
                    to_append.append(j) 
                    print(f"Whoops, {j} didn't exist..")
                    continue
                if not (i in self.adjacency_list[j]):
                    self.adjacency_list[j].append(i) 
                    print(f"Whoops, {i} didn't exist in {j}..")
        for i in to_append:
            self.adjacency_list[i] = [] 
        if len(to_append) > 0:
            for i, ii in self.adjacency_list.items():
                for j in ii:
                    if not (i in self.adjacency_list[j]):
                        self.adjacency_list[j].append(i) 
                        print(f"Whoops, {i} didn't exist in {j}..")
                    


adjacency_list = {
    'Madrid': ['Castile and Leon', 'Castile-La Mancha', 'Extremadura'],
    'Catalonia': ['Aragon', 'Valencia'],
    'Valencia': ['Catalonia', 'Murcia', 'Castile-La Mancha'],
    'Galicia': ['Asturias', 'Castile and Leon'],
    'Andalusia': ['Extremadura', 'Castile-La Mancha', 'Murcia'],
    'Murcia': ['Valencia', 'Andalusia'],
    'Aragon': ['Catalonia', 'Navarre', 'Castile and Leon'],
    'Castile and Leon': ['Galicia', 'Asturias', 'Aragon', 'Madrid', 'Extremadura', 'Castile-La Mancha'],
    'Castile-La Mancha': ['Madrid', 'Valencia', 'Extremadura', 'Andalusia'],
    'Extremadura': ['Madrid', 'Castile and Leon', 'Andalusia', 'Castile-La Mancha'],
    'Asturias': ['Galicia', 'Castile and Leon'],
    'Navarre': ['Aragon'],
    'Basque Country': ['Navarre'],
    'Cantabria': ['Asturias'],
    'La Rioja': ['Aragon', 'Castile and Leon'],
    'aaa': ['bbb', 'ccc']
}

gc = GraphColoring(adjacency_list)
gc.validate()
print()
chromatic_number, color_assignment = gc.find_chromatic_number()

print(f"Chromatic Number: {chromatic_number}")
for vertex, color in color_assignment.items():
    print(f"{vertex}: Color {color}")