class Element:
    def __init__(self, node1, node2, node3, node4):
        self.id = []
        self.HBC = []
        self.HL = []
        self.P = []
        self.id.append(node1)
        self.id.append(node2)
        self.id.append(node3)
        self.id.append(node4)

    def __str__(self):
        return f"Element[{self.id}]"
