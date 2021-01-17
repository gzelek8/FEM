import math

w1 = (18 - math.sqrt(30)) / 36
w2 = (18 + math.sqrt(30)) / 36


class Element4Node:
    weight_2_p = [1, 1, 1, 1]
    weight_3_p = [5 / 9, 8 / 9, 5 / 9]
    weight_4_p = [w1, w2, w2, w1]

    def __init__(self, amount_of_node):
        self.localPoints = []
        if amount_of_node == 2:
            self.ksi = [-(1 / math.sqrt(3)), (1 / math.sqrt(3))]
            self.eta = [-(1 / math.sqrt(3)), (1 / math.sqrt(3))]
            for eta in self.eta:
                for ksi in self.ksi:
                    self.localPoints.append((ksi, eta))
        elif amount_of_node == 3:
            self.ksi = [-(math.sqrt(3 / 5)), 0, (math.sqrt(3 / 5))]
            self.eta = [-(math.sqrt(3 / 5)), 0, (math.sqrt(3 / 5))]
            for eta in self.eta:
                for ksi in self.ksi:
                    self.localPoints.append((ksi, eta))
        elif amount_of_node == 4:
            self.ksi = [-(math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))),
                        -(math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))),
                        (math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))),
                        (math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5))))]
            self.eta = [-(math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))),
                        -(math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))),
                        (math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))),
                        (math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5))))]
            for eta in self.eta:
                for ksi in self.ksi:
                    self.localPoints.append((ksi, eta))

    def calculate_dN1_dKsi(self):
        dN1_dKsi = []
        for point in self.localPoints:
            dN1_dKsi.append(-(1 - point[1]) / 4)
        return dN1_dKsi

    def calculate_dN2_dKsi(self):
        dN2_dKsi = []
        for point in self.localPoints:
            dN2_dKsi.append((1 - point[1]) / 4)
        return dN2_dKsi

    def calculate_dN3_dKsi(self):
        dN3_dKsi = []
        for point in self.localPoints:
            dN3_dKsi.append((1 + point[1]) / 4)
        return dN3_dKsi

    def calculate_dN4_dKsi(self):
        dN4_dKsi = []
        for point in self.localPoints:
            dN4_dKsi.append(-(1 + point[1]) / 4)
        return dN4_dKsi

    def calculate_dN1_dEta(self):
        dN1_dEta = []
        for point in self.localPoints:
            dN1_dEta.append(-(1 - point[0]) / 4)
        return dN1_dEta

    def calculate_dN2_dEta(self):
        dN2_dEta = []
        for point in self.localPoints:
            dN2_dEta.append(-(1 + point[0]) / 4)
        return dN2_dEta

    def calculate_dN3_dEta(self):
        dN3_dEta = []
        for point in self.localPoints:
            dN3_dEta.append((1 + point[0]) / 4)
        return dN3_dEta

    def calculate_dN4_dEta(self):
        dN4_dEta = []
        for point in self.localPoints:
            dN4_dEta.append((1 - point[0]) / 4)
        return dN4_dEta

    def calculate_N1(self):
        dN1 = []
        for point in self.localPoints:
            dN1.append(((1 - point[0]) * (1 - point[1])) / 4)
        # tmp = dN1[2]
        # dN1[2] = dN1[3]
        # dN1[3] = tmp
        return dN1

    def calculate_N2(self):
        dN2 = []
        for point in self.localPoints:
            dN2.append(((1 - point[0]) * (1 + point[1])) / 4)
        # tmp = dN2[2]
        # dN2[2] = dN2[3]
        # dN2[3] = tmp
        return dN2

    def calculate_N3(self):
        dN3 = []
        for point in self.localPoints:
            dN3.append(((1 + point[0]) * (1 + point[1])) / 4)
        # tmp = dN3[2]
        # dN3[2] = dN3[3]
        # dN3[3] = tmp
        return dN3

    def calculate_N4(self):
        dN4 = []
        for point in self.localPoints:
            dN4.append(((1 + point[0]) * (1 - point[1])) / 4)
        # tmp = dN4[2]
        # dN4[2] = dN4[3]
        # dN4[3] = tmp
        return dN4

# test = Element4Node(2)
# test2 = Element4Node(3)
# test3 = Element4Node(4)
#
# print(len(test3.localPoints))
# for point in test3.localPoints:
#     print(point)
# print(test3.localPoints)
# print("--------------------")
# print(test3.calculate_dN1_dEta())
# print(test3.calculate_dN2_dEta())
# print(test3.calculate_dN3_dEta())
# print(test3.calculate_dN4_dEta())
# print(test3.calculate_dN1_dKsi())
# print(test3.calculate_dN2_dKsi())
# print(test3.calculate_dN3_dKsi())
# print(test3.calculate_dN4_dKsi())
#
