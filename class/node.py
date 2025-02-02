class Node:
    def __init__(self, depth = 0 , cost = 0 , parent = None , state = None):
        self.depth = depth
        self.cost = cost
        self.parent = parent
        self.state = state

    def __str__(self):
        return f"Node\nDepth = {self.depth}\nCost = {self.cost}"

    

