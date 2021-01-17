import GlobalData as gd
import Element4node as weight

kt = gd.GlobalData.k
weights_3_points = weight.Element4Node.weight_3_p
weights_4_points = weight.Element4Node.weight_4_p


class MatrixH:
    def __init__(self, jacobian, amount_of_nodes):
        self.matrixH = []
        self.global_matrixH = [[0 for el in range(amount_of_nodes)] for el in range(amount_of_nodes)]
        self.j = jacobian
        self.matrixHp1 = []
        self.matrixHp2 = []
        self.matrixHp3 = []
        self.matrixHp4 = []
        if len(self.j.dN_dKsi[0]) > 4:
            self.matrixHp5 = []
            self.matrixHp6 = []
            self.matrixHp7 = []
            self.matrixHp8 = []
            self.matrixHp9 = []
            if len(self.j.dN_dKsi[0]) > 9:
                self.matrixHp10 = []
                self.matrixHp11 = []
                self.matrixHp12 = []
                self.matrixHp13 = []
                self.matrixHp14 = []
                self.matrixHp15 = []
                self.matrixHp16 = []

    def calculate_matrixHp1(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append((1 / det[count]) * (
                    el[0] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][0]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[0] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][0]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[0] *
                                weights_3_points[0])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[0] *
                                weights_4_points[0])
            self.matrixHp1.append(temp)

    def calculate_matrixHp2(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[1] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][1]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[1] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][1]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[1] *
                                weights_3_points[0])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[1] *
                                weights_4_points[0])
            self.matrixHp2.append(temp)

    def calculate_matrixHp3(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[2] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][2]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[2] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][2]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[2] *
                                weights_3_points[0])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[2] *
                                weights_4_points[0])
            self.matrixHp3.append(temp)

    def calculate_matrixHp4(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[3] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][3]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[3] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][3]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 4:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count])
                elif len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[0] *
                                weights_3_points[1])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[3] *
                                weights_4_points[0])
            self.matrixHp4.append(temp)

    def calculate_matrixHp5(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[4] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][4]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[4] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][4]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[1] *
                                weights_3_points[1])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[0] *
                                weights_4_points[1])
            self.matrixHp5.append(temp)

    def calculate_matrixHp6(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[5] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][5]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[5] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][5]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[2] *
                                weights_3_points[1])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[1] *
                                weights_4_points[1])
            self.matrixHp6.append(temp)

    def calculate_matrixHp7(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[6] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][6]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[6] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][6]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[0] *
                                weights_3_points[2])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[2] *
                                weights_4_points[1])
            self.matrixHp7.append(temp)

    def calculate_matrixHp8(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[7] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][7]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[7] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][7]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[1] *
                                weights_3_points[2])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[3] *
                                weights_4_points[1])
            self.matrixHp8.append(temp)

    def calculate_matrixHp9(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[8] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][8]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[8] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][8]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                if len(self.j.dN_dKsi[0]) == 9:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_3_points[2] *
                                weights_3_points[2])
                elif len(self.j.dN_dKsi[0]) == 16:
                    temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[0] *
                                weights_4_points[2])
            self.matrixHp9.append(temp)

    def calculate_matrixHp10(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[9] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][9]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[9] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][9]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[1] *
                            weights_4_points[2])
            self.matrixHp10.append(temp)

    def calculate_matrixHp11(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[10] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][10]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[10] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][10]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[2] *
                            weights_4_points[2])
            self.matrixHp11.append(temp)

    def calculate_matrixHp12(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[11] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][11]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[11] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][11]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[3] *
                            weights_4_points[2])
            self.matrixHp12.append(temp)

    def calculate_matrixHp13(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[12] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][12]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[12] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][12]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[0] *
                            weights_4_points[3])
            self.matrixHp13.append(temp)

    def calculate_matrixHp14(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[13] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][13]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[13] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][13]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[1] *
                            weights_4_points[3])
            self.matrixHp14.append(temp)

    def calculate_matrixHp15(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[14] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][14]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[14] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][14]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[2] *
                            weights_4_points[3])
            self.matrixHp15.append(temp)

    def calculate_matrixHp16(self, jacobian, det):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[15] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][15]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[15] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][15]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[3] *
                            weights_4_points[3])
            self.matrixHp16.append(temp)

    def calculate_matrixHp(self, jacobian, det , num):
        vectorDx = []
        vectorDy = []
        matrixHdx = []
        matrixHdy = []
        for count, el in enumerate(self.j.dN_dKsi):
            vectorDx.append(1 / det[count] * (
                    el[num] * jacobian[count][3] + jacobian[count][1] * self.j.dN_dKsi[count][num]))
        for count, el in enumerate(self.j.dN_dEta):
            vectorDy.append(1 / det[count] * (
                    el[num] * jacobian[count][2] + jacobian[count][0] * self.j.dN_dEta[count][num]))
        for el1 in vectorDx:
            temp = []
            for el2 in vectorDx:
                temp.append(el1 * el2)
            matrixHdx.append(temp)
        for el1 in vectorDy:
            temp = []
            for el2 in vectorDy:
                temp.append(el1 * el2)
            matrixHdy.append(temp)
        for count, el1 in enumerate(matrixHdx):
            temp = []
            for i, el2 in enumerate(matrixHdx):
                temp.append((matrixHdx[count][i] + matrixHdy[count][i]) * kt * det[count] * weights_4_points[3] *
                            weights_4_points[3])
            self.matrixHp[num].append(temp)

    def calculate_matrixH(self, jacobian, det):
        self.calculate_matrixHp1(jacobian, det)
        self.calculate_matrixHp2(jacobian, det)
        self.calculate_matrixHp3(jacobian, det)
        self.calculate_matrixHp4(jacobian, det)
        if len(self.j.dN_dKsi[0]) > 4:
            self.calculate_matrixHp5(jacobian, det)
            self.calculate_matrixHp6(jacobian, det)
            self.calculate_matrixHp7(jacobian, det)
            self.calculate_matrixHp8(jacobian, det)
            self.calculate_matrixHp9(jacobian, det)
            if len(self.j.dN_dKsi[0]) > 9:
                self.calculate_matrixHp10(jacobian, det)
                self.calculate_matrixHp11(jacobian, det)
                self.calculate_matrixHp12(jacobian, det)
                self.calculate_matrixHp13(jacobian, det)
                self.calculate_matrixHp14(jacobian, det)
                self.calculate_matrixHp15(jacobian, det)
                self.calculate_matrixHp16(jacobian, det)

        for count, el1 in enumerate(self.matrixHp1):
            temp = []
            if len(self.j.dN_dKsi[0]) == 4:
                for i, el2 in enumerate(self.matrixHp1):
                    temp.append((self.matrixHp1[count][i] + self.matrixHp2[count][i]
                                 + self.matrixHp3[count][i] + self.matrixHp4[count][i]))
            elif len(self.j.dN_dKsi[0]) == 9:
                for i, el2 in enumerate(self.matrixHp1):
                    temp.append((self.matrixHp1[count][i] + self.matrixHp2[count][i]
                                 + self.matrixHp3[count][i] + self.matrixHp4[count][i]
                                 + self.matrixHp5[count][i] + self.matrixHp6[count][i]
                                 + self.matrixHp7[count][i] + self.matrixHp8[count][i]
                                 + self.matrixHp9[count][i]))
            elif len(self.j.dN_dKsi[0]) == 16:
                for i, el2 in enumerate(self.matrixHp1):
                    temp.append((self.matrixHp1[count][i] + self.matrixHp2[count][i]
                                 + self.matrixHp3[count][i] + self.matrixHp4[count][i]
                                 + self.matrixHp5[count][i] + self.matrixHp6[count][i]
                                 + self.matrixHp7[count][i] + self.matrixHp8[count][i]
                                 + self.matrixHp9[count][i] + self.matrixHp10[count][i]
                                 + self.matrixHp11[count][i] + self.matrixHp12[count][i]
                                 + self.matrixHp13[count][i] + self.matrixHp14[count][i]
                                 + self.matrixHp15[count][i] + self.matrixHp16[count][i]))
            self.matrixH.append(temp)
        self.matrixHp1 = []
        self.matrixHp2 = []
        self.matrixHp3 = []
        self.matrixHp4 = []

    def print_matrixH(self):
        print("-----Matrix H----------")
        for count, el in enumerate(self.matrixH):
            if ((count + 1) % 4) == 0:
                print(el)
                print("-----------------")
            else:
                print(el)

    def fill_in_global_matrixH(self, elements):
        shift = 0
        for element in elements:
            for i in range(len(element.id)):
                for j in range(len(element.id)):
                    self.global_matrixH[element.id[i] - 1][element.id[j] - 1] += element.HL[i][j]
            shift += 4

    def print_global_matrixH(self):
        for el in self.global_matrixH:
            print(el)

# j = jacobian.JacobianMatrix()
# j.fill_in_jacobian_matrix(jacobian.data.global_points)
# j.calculate_det()
# j.invert_jacobian()
# matrixH = MatrixH()
# matrixH.calculate_matrixHp1()
# matrixH.calculate_matrixHp2()
# matrixH.calculate_matrixHp3()
# matrixH.calculate_matrixHp4()
# matrixH.calculate_matrixH()
# matrixH.print_matrixH()
#
# print("1")
# print(matrixH.matrixHp1)
# print("2")
# print(matrixH.matrixHp2)
# print("3")
# print(matrixH.matrixHp3)
# print("4")
# print(matrixH.matrixHp4)
