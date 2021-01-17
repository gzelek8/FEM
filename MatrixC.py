import GlobalData as gd
import Element4node as weight

weights_3_points = weight.Element4Node.weight_3_p
weights_4_points = weight.Element4Node.weight_4_p


class MatrixC:
    def __init__(self, jacobian, amount_of_nodes):
        self.matrixC = []
        self.global_matrixC = [[0 for el in range(amount_of_nodes)] for el in range(amount_of_nodes)]
        self.j = jacobian
        self.matrixCp1 = []
        self.matrixCp2 = []
        self.matrixCp3 = []
        self.matrixCp4 = []
        if len(self.j.dN_dKsi[0]) > 4:
            self.matrixCp5 = []
            self.matrixCp6 = []
            self.matrixCp7 = []
            self.matrixCp8 = []
            self.matrixCp9 = []
            if len(self.j.dN_dKsi[0]) > 9:
                self.matrixCp10 = []
                self.matrixCp11 = []
                self.matrixCp12 = []
                self.matrixCp13 = []
                self.matrixCp14 = []
                self.matrixCp15 = []
                self.matrixCp16 = []

    def calculate_matrixCp1(self, n, det):
        vector = []
        for el in n:
            vector.append(el[0])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append(
                        el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[0] *
                        weights_3_points[0])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[0] *
                                weights_4_points[0])
            self.matrixCp1.append(temp)

    def calculate_matrixCp2(self, n, det):
        vector = []
        for el in n:
            vector.append(el[1])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append(
                        el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[1] *
                        weights_3_points[0])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[1] *
                                weights_4_points[0])
            self.matrixCp2.append(temp)

    def calculate_matrixCp3(self, n, det):
        vector = []
        for el in n:
            vector.append(el[2])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append(
                        el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[2] *
                        weights_3_points[0])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[2] *
                                weights_4_points[0])
            self.matrixCp3.append(temp)

    def calculate_matrixCp4(self, n, det):
        vector = []
        for el in n:
            vector.append(el[3])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[0] *
                                weights_3_points[1])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[3] *
                                weights_4_points[0])
            self.matrixCp4.append(temp)

    def calculate_matrixCp5(self, n, det):
        vector = []
        for el in n:
            vector.append(el[4])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[1] *
                                weights_3_points[1])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[0] *
                                weights_4_points[1])
            self.matrixCp5.append(temp)

    def calculate_matrixCp6(self, n, det):
        vector = []
        for el in n:
            vector.append(el[5])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[2] *
                                weights_3_points[1])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[1] *
                                weights_4_points[1])
            self.matrixCp6.append(temp)

    def calculate_matrixCp7(self, n, det):
        vector = []
        for el in n:
            vector.append(el[6])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[0] *
                                weights_3_points[2])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[2] *
                                weights_4_points[1])
            self.matrixCp7.append(temp)

    def calculate_matrixCp8(self, n, det):
        vector = []
        for el in n:
            vector.append(el[7])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[1] *
                                weights_3_points[2])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[3] *
                                weights_4_points[1])
            self.matrixCp8.append(temp)

    def calculate_matrixCp9(self, n, det):
        vector = []
        for el in n:
            vector.append(el[8])
        for el1 in vector:
            temp = []
            for el2 in vector:
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_3_points[2] *
                                weights_3_points[2])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[0] *
                                weights_4_points[2])
            self.matrixCp9.append(temp)

    def calculate_matrixCp10(self, n, det):
        vector = []
        for el in n:
            vector.append(el[9])
        for el1 in vector:
            temp = []
            for el2 in vector:
                temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[1] *
                            weights_4_points[2])
            self.matrixCp10.append(temp)

    def calculate_matrixCp11(self, n, det):
        vector = []
        for el in n:
            vector.append(el[10])
        for el1 in vector:
            temp = []
            for el2 in vector:
                temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[2] *
                            weights_4_points[2])
            self.matrixCp11.append(temp)

    def calculate_matrixCp12(self, n, det):
        vector = []
        for el in n:
            vector.append(el[11])
        for el1 in vector:
            temp = []
            for el2 in vector:
                temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[3] *
                            weights_4_points[2])
            self.matrixCp12.append(temp)

    def calculate_matrixCp13(self, n, det):
        vector = []
        for el in n:
            vector.append(el[12])
        for el1 in vector:
            temp = []
            for el2 in vector:
                temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[0] *
                            weights_4_points[3])
            self.matrixCp13.append(temp)

    def calculate_matrixCp14(self, n, det):
        vector = []
        for el in n:
            vector.append(el[13])
        for el1 in vector:
            temp = []
            for el2 in vector:
                temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[1] *
                            weights_4_points[3])
            self.matrixCp14.append(temp)

    def calculate_matrixCp15(self, n, det):
        vector = []
        for el in n:
            vector.append(el[14])
        for el1 in vector:
            temp = []
            for el2 in vector:
                temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[2] *
                            weights_4_points[3])
            self.matrixCp15.append(temp)

    def calculate_matrixCp16(self, n, det):
        vector = []
        for el in n:
            vector.append(el[15])
        for el1 in vector:
            temp = []
            for el2 in vector:
                temp.append(el1 * el2 * gd.GlobalData.ro * gd.GlobalData.c * det[0] * weights_4_points[3] *
                            weights_4_points[3])
            self.matrixCp16.append(temp)

    def calculate_matrixC(self, n, det):
        self.calculate_matrixCp1(n, det)
        self.calculate_matrixCp2(n, det)
        self.calculate_matrixCp3(n, det)
        self.calculate_matrixCp4(n, det)
        if len(self.j.dN_dKsi[0]) > 4:
            self.calculate_matrixCp5(n, det)
            self.calculate_matrixCp6(n, det)
            self.calculate_matrixCp7(n, det)
            self.calculate_matrixCp8(n, det)
            self.calculate_matrixCp9(n, det)
            if len(self.j.dN_dKsi[0]) > 9:
                self.calculate_matrixCp10(n, det)
                self.calculate_matrixCp11(n, det)
                self.calculate_matrixCp12(n, det)
                self.calculate_matrixCp13(n, det)
                self.calculate_matrixCp14(n, det)
                self.calculate_matrixCp15(n, det)
                self.calculate_matrixCp16(n, det)

        for count, el1 in enumerate(self.matrixCp1):
            temp = []
            if len(self.j.dN_dKsi[0]) == 4:
                for i, el2 in enumerate(self.matrixCp1):
                    temp.append((self.matrixCp1[count][i] + self.matrixCp2[count][i]
                                 + self.matrixCp3[count][i] + self.matrixCp4[count][i]))
            elif len(self.j.dN_dKsi[0]) == 9:
                for i, el2 in enumerate(self.matrixCp1):
                    temp.append((self.matrixCp1[count][i] + self.matrixCp2[count][i]
                                 + self.matrixCp3[count][i] + self.matrixCp4[count][i]
                                 + self.matrixCp5[count][i] + self.matrixCp6[count][i]
                                 + self.matrixCp7[count][i] + self.matrixCp8[count][i]
                                 + self.matrixCp9[count][i]))
            elif len(self.j.dN_dKsi[0]) == 16:
                for i, el2 in enumerate(self.matrixCp1):
                    temp.append((self.matrixCp1[count][i] + self.matrixCp2[count][i]
                                 + self.matrixCp3[count][i] + self.matrixCp4[count][i]
                                 + self.matrixCp5[count][i] + self.matrixCp6[count][i]
                                 + self.matrixCp7[count][i] + self.matrixCp8[count][i]
                                 + self.matrixCp9[count][i] + self.matrixCp10[count][i]
                                 + self.matrixCp11[count][i] + self.matrixCp12[count][i]
                                 + self.matrixCp13[count][i] + self.matrixCp14[count][i]
                                 + self.matrixCp15[count][i] + self.matrixCp16[count][i]))
            self.matrixC.append(temp)
        self.matrixCp1 = []
        self.matrixCp2 = []
        self.matrixCp3 = []
        self.matrixCp4 = []

    def fill_in_global_matrixC(self, elements):
        shift = 0
        for element in elements:
            for i in range(len(element.id)):
                for j in range(len(element.id)):
                    self.global_matrixC[element.id[i] - 1][element.id[j] - 1] += self.matrixC[i + shift][j]
            shift += 4

    def print_global_matrixC(self):
        for el in self.global_matrixC:
            print(el)
