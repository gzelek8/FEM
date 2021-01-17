class Node:
    def __init__(self, x, y, bc):
        self.x = x
        self.y = y
        self.BC = bc

    def __str__(self):
        return f"Node({self.x},{self.y} , {self.BC})"
