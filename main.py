import numpy as np

import FEM_GRID as fg
import GlobalData as gd
import BC as BC
import Element4node as el4node
import JacobianMatrix as Jacobian
import MatrixH as MatrixH
import MatrixC as MatrixC
import P as P


def calculate_matrixH():
    global i, arg_jacobian, arg_det
    if len(j1.jacobian) == 81:
        for i in range(0, len(jacobian), 9):
            arg_jacobian = [jacobian[i], jacobian[i + 1], jacobian[i + 2], jacobian[i + 3]]
            arg_det = [det[i], det[i + 1], det[i + 2], det[i + 3]]
            h1.calculate_matrixH(arg_jacobian, arg_det)
    elif len(j1.jacobian) == 144:
        for i in range(0, len(jacobian), 16):
            arg_jacobian = [jacobian[i], jacobian[i + 1], jacobian[i + 2], jacobian[i + 3]]
            arg_det = [det[i], det[i + 1], det[i + 2], det[i + 3]]
            h1.calculate_matrixH(arg_jacobian, arg_det)
    else:
        for i in range(0, len(jacobian), 4):
            arg_jacobian = [jacobian[i], jacobian[i + 1], jacobian[i + 2], jacobian[i + 3]]
            arg_det = [det[i], det[i + 1], det[i + 2], det[i + 3]]
            h1.calculate_matrixH(arg_jacobian, arg_det)


def calculate_matrixC():
    global i, arg_jacobian, arg_det
    if len(j1.jacobian) == 81:
        for i in range(0, len(jacobian), 9):
            arg_jacobian = [jacobian[i], jacobian[i + 1], jacobian[i + 2], jacobian[i + 3]]
            arg_det = [det[i], det[i + 1], det[i + 2], det[i + 3]]
            mc.calculate_matrixC(j1.N, arg_det)
    elif len(j1.jacobian) == 144:
        for i in range(0, len(jacobian), 16):
            arg_jacobian = [jacobian[i], jacobian[i + 1], jacobian[i + 2], jacobian[i + 3]]
            arg_det = [det[i], det[i + 1], det[i + 2], det[i + 3]]
            mc.calculate_matrixC(j1.N, arg_det)
    else:
        for i in range(0, len(jacobian), 4):
            arg_jacobian = [jacobian[i], jacobian[i + 1], jacobian[i + 2], jacobian[i + 3]]
            arg_det = [det[i], det[i + 1], det[i + 2], det[i + 3]]
            mc.calculate_matrixC(j1.N, arg_det)


def Create_All():
    global g1, j1, h1, mc
    g1 = fg.FEM_GRID()
    el4n = el4node.Element4Node(gd.GlobalData.amount_integral_point)
    j1 = Jacobian.JacobianMatrix(el4n)
    h1 = MatrixH.MatrixH(j1, len(g1.node))
    mc = MatrixC.MatrixC(j1, len(g1.node))


t0 = [gd.GlobalData.initial_temperature for el in range(gd.GlobalData.nN)]

for iteration_num in range(int(gd.GlobalData.simulation_iteration)):
    Create_All()
    lista_el = []
    for count in range(1, gd.GlobalData.nE + 1):
        lista_el.append(g1.return_element(count))

    for el in lista_el:
        j1.fill_in_jacobian_matrix(el)

    j1.calculate_det()

    j1.invert_jacobian()

    jacobian = []
    for el in j1.jacobian:
        jacobian.append(el)

    det = []
    for el in j1.det:
        det.append(el)

    # print("------------------MATRIX L+BC------------------")
    BC.calculate_BC(g1, gd.GlobalData.amount_integral_point, gd.GlobalData.alfa, gd.GlobalData.talfa)

    # print("+++++++++++++++++MATRIX H++++++++++++++")
    calculate_matrixH()
    shift = 0
    for el in g1.element:
        el.HL.append(h1.matrixH[shift])
        el.HL.append(h1.matrixH[1 + shift])
        el.HL.append(h1.matrixH[2 + shift])
        el.HL.append(h1.matrixH[3 + shift])
        shift += 4
    for el in g1.element:
        for count, el2 in enumerate(el.HL):
            for i, el3 in enumerate(el.HL):
                if el.HBC:
                    el.HL[count][i] += el.HBC[count][i]
    h1.fill_in_global_matrixH(g1.element)
    # h1.print_global_matrixH()

    # print("---------------MATRIX C-------------")
    calculate_matrixC()
    mc.fill_in_global_matrixC(g1.element)
    # mc.print_global_matrixC()

    # for el in g1.element:
    #     el.HL = el.HL + el.HBC
    #
    # for el in g1.element:
    #     for el2 in el.HL:
    #         print(el2)
    #     print("----------------")
    # for el in g1.element:
    #     for el2 in el.HBC:
    #         print(el2)
    #     print("------")
    # for el in g1.element:
    #     print(el.P)
    #     print(el)

    vector_p = P.fil_in_global_p(g1.element, gd.GlobalData.nN)

    c = [[0 for el in range(gd.GlobalData.nN)] for el in range(gd.GlobalData.nN)]
    cp = mc.global_matrixC.copy()
    h = h1.global_matrixH
    for index1, el in enumerate(mc.global_matrixC):
        for index2, el2 in enumerate(el):
            c[index1][index2] = el2 / gd.GlobalData.simulation_step + h[index1][index2]
    p = [0 for el in range(gd.GlobalData.nN)]

    for index1, el in enumerate(cp):
        for index2, el2 in enumerate(el):
            p[index1] += t0[index2] * (el2 / gd.GlobalData.simulation_step)
    for index, el in enumerate(vector_p):
        p[index] += abs(vector_p[index])
    # print("--------------------")
    # for el in c:
    #    print(el)
    # print("-----------------")
    # print(p)
    t0 = list(np.linalg.solve(c, p))
    print(f"I:{iteration_num} tmin:{min(t0)} tmax:{max(t0)}")
    # print(f"Max T: {max(t0)}")
    # print(f"Max T: {min(t0)}")
