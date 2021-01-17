import Element4node as El4node

el = El4node.Element4Node(2)


class JacobianMatrix:
    def __init__(self, el):
        self.dN_dKsi = [el.calculate_dN1_dKsi(), el.calculate_dN2_dKsi(), el.calculate_dN3_dKsi(),
                        el.calculate_dN4_dKsi()]
        self.dN_dEta = [el.calculate_dN1_dEta(), el.calculate_dN2_dEta(), el.calculate_dN3_dEta(),
                        el.calculate_dN4_dEta()]
        self.N = [el.calculate_N1(), el.calculate_N2(), el.calculate_N3(), el.calculate_N4()]
        self.jacobian = []
        self.inverse_jacobian = []
        self.det = []

    def fill_in_jacobian_matrix(self, actual_points):
        i = 0
        while i != len(self.dN_dKsi[0]):
            actual_jacobian = []
            value = 0
            for count, point in enumerate(actual_points):
                value += point[0] * self.dN_dKsi[count][i]
            actual_jacobian.append(value)
            value = 0
            for count, point in enumerate(actual_points):
                value += point[0] * self.dN_dEta[count][i]
            actual_jacobian.append(value)
            value = 0
            for count, point in enumerate(actual_points):
                value += point[1] * self.dN_dKsi[count][i]
            actual_jacobian.append(value)
            value = 0
            for count, point in enumerate(actual_points):
                value += point[1] * self.dN_dEta[count][i]
            actual_jacobian.append(value)
            i += 1
            self.jacobian.append(actual_jacobian)

    def invert_jacobian(self):
        for jacobian in self.jacobian:
            self.inverse_jacobian.append([jacobian[3], -jacobian[1], -jacobian[2], jacobian[0]])

    def calculate_det(self):
        for jacobian in self.jacobian:
            self.det.append(jacobian[0] * jacobian[3] - jacobian[1] * jacobian[2])

    def print_ksi_and_eta_matrix(self):
        print("-------dN/dKsi-------")
        for line in self.dN_dKsi:
            print(line)
        print("-------dN/dEta-------")
        for line in self.dN_dEta:
            print(line)

    def print_jacobian_matrix(self):
        print("-----Jacobian Matrix---------")
        if len(self.jacobian) == 36:
            print(self.jacobian[0], self.jacobian[1])
            print(self.jacobian[2], self.jacobian[3])
        elif len(self.jacobian) == 81:
            print(self.jacobian[0], self.jacobian[1], self.jacobian[2])
            print(self.jacobian[3], self.jacobian[4], self.jacobian[5])
            print(self.jacobian[6], self.jacobian[7], self.jacobian[8])
        elif len(self.jacobian) == 144:
            print(self.jacobian[0], self.jacobian[1], self.jacobian[2], self.jacobian[3])
            print(self.jacobian[4], self.jacobian[5], self.jacobian[6], self.jacobian[7])
            print(self.jacobian[8], self.jacobian[9], self.jacobian[10], self.jacobian[11])
            print(self.jacobian[12], self.jacobian[13], self.jacobian[14], self.jacobian[15])

    def print_inverse_jacobian_matrix(self):
        print("-----Invert Jacobian Matrix---------")
        if len(self.inverse_jacobian) == 36:
            print(self.inverse_jacobian[0], self.inverse_jacobian[1])
            print(self.inverse_jacobian[2], self.inverse_jacobian[3])
        elif len(self.inverse_jacobian) == 81:
            print(self.inverse_jacobian[0], self.inverse_jacobian[1], self.inverse_jacobian[2])
            print(self.inverse_jacobian[3], self.inverse_jacobian[4], self.inverse_jacobian[5])
            print(self.inverse_jacobian[6], self.inverse_jacobian[7], self.inverse_jacobian[8])
        elif len(self.jacobian) == 144:
            print(self.inverse_jacobian[0], self.inverse_jacobian[1], self.inverse_jacobian[2],
                  self.inverse_jacobian[3])
            print(self.inverse_jacobian[4], self.inverse_jacobian[5], self.inverse_jacobian[6],
                  self.inverse_jacobian[7])
            print(self.inverse_jacobian[8], self.inverse_jacobian[9], self.inverse_jacobian[10],
                  self.inverse_jacobian[11])
            print(self.inverse_jacobian[12], self.inverse_jacobian[13], self.inverse_jacobian[14],
                  self.inverse_jacobian[15])

# j = JacobianMatrix(el)
# for el in j.N:
#     print(el)
# j.fill_in_jacobian_matrix()
# j.calculate_det()
# j.invert_jacobian()
# j.print_ksi_and_eta_matrix()
# print("-------------------------")
# j.print_jacobian_matrix()
# print("--------------------")
# j.print_inverse_jacobian_matrix()
# print("-----Det J-------")
# print(j.det)
