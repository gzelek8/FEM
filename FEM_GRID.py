import Element as Element
import GlobalData as GlobalData
import Node as Node


class FEM_GRID:
    def __init__(self):
        self.node = []
        self.element = []
        self.make_grid()

    def make_grid(self):
        deltaX = GlobalData.GlobalData.W / (GlobalData.GlobalData.nW - 1)
        deltaY = GlobalData.GlobalData.H / (GlobalData.GlobalData.nH - 1)
        for i in range(GlobalData.GlobalData.nW):
            for j in range(GlobalData.GlobalData.nH):
                if deltaX * i == 0 or deltaY * j == 0 or \
                        deltaX * i == GlobalData.GlobalData.H or deltaY * j == GlobalData.GlobalData.W:
                    self.node.append(Node.Node(deltaX * i, deltaY * j, True))
                else:
                    self.node.append(Node.Node(deltaX * i, deltaY * j, False))
        for i in range(GlobalData.GlobalData.nW - 1):
            for j in range(GlobalData.GlobalData.nH - 1):
                id1 = j + i * GlobalData.GlobalData.nH + 1
                id2 = id1 + GlobalData.GlobalData.nH
                id3 = id2 + 1
                id4 = id1 + 1
                self.element.append(Element.Element(id1, id2, id3, id4))

    def print_element(self, element):
        print(f"Element's {element} nodes: ")
        for node in self.element[element - 1].id:
            print(f" {node} x = {self.node[node - 1].x} y = {self.node[node - 1].y}")

    def return_element(self, element):
        xd = []
        for node in self.element[element - 1].id:
            xd.append((self.node[node - 1].x, self.node[node - 1].y))
        return xd
