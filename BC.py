import math


def calculate_BC(g1, amount_integral_point, alfa, talfa):
    # L = g1.node[4].x - g1.node[0].x
    # 2 points schema
    local_points = []
    weights = []
    if amount_integral_point == 2:
        weights = [1, 1]

        local_points.append((-(1 / math.sqrt(3)), -1))
        local_points.append(((1 / math.sqrt(3)), -1))

        local_points.append((1, -(1 / math.sqrt(3))))
        local_points.append((1, (1 / math.sqrt(3))))

        local_points.append(((1 / math.sqrt(3)), 1))
        local_points.append((-(1 / math.sqrt(3)), 1))

        local_points.append((-1, (1 / math.sqrt(3))))
        local_points.append((-1, -(1 / math.sqrt(3))))
    elif amount_integral_point == 3:
        weights = [5 / 9, 8 / 9, 5 / 9]

        local_points.append(-(math.sqrt(3 / 5)), -1)
        local_points.append(0, -1)
        local_points.append((math.sqrt(3 / 5)), -1)

        local_points.append(1, -(math.sqrt(3 / 5)))
        local_points.append(1, 0)
        local_points.append(1, (math.sqrt(3 / 5)))

        local_points.append((math.sqrt(3 / 5)), 1)
        local_points.append(0, 1)
        local_points.append(-(math.sqrt(3 / 5)), 1)

        local_points.append(-1, (math.sqrt(3 / 5)))
        local_points.append(-1, 0)
        local_points.append(-1, -(math.sqrt(3 / 5)))

    elif amount_integral_point == 4:
        weights = [(18 - math.sqrt(30)) / 36, (18 + math.sqrt(30)) / 36, (18 + math.sqrt(30)) / 36,
                   (18 - math.sqrt(30)) / 36]
        local_points.append(-(math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))), -1)
        local_points.append(-(math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))), -1)
        local_points.append((math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))), -1)
        local_points.append((math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))), -1)

        local_points.append(1, -(math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))))
        local_points.append(1, -(math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))))
        local_points.append(1, (math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))))
        local_points.append(1, (math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))))

        local_points.append((math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))), 1)
        local_points.append((math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))), 1)
        local_points.append(-(math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))), 1)
        local_points.append(-(math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))), 1)

        local_points.append(-1, (math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))))
        local_points.append(-1, (math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))))
        local_points.append(-1, -(math.sqrt(3 / 7 - 2 / 7 * (math.sqrt(6 / 5)))))
        local_points.append(-1, -(math.sqrt(3 / 7 + 2 / 7 * (math.sqrt(6 / 5)))))

    for el in g1.element:
        for count, node in enumerate(el.id):
            if count + 1 < len(el.id):
                if g1.node[node - 1].BC and g1.node[(el.id[count + 1]) - 1].BC:
                    L = math.sqrt((pow(g1.node[(el.id[count + 1]) - 1].x - g1.node[node - 1].x, 2)) + (
                        pow(g1.node[(el.id[count + 1]) - 1].y - g1.node[node - 1].y, 2)))
                    vector = []
                    local_matrix = []
                    first_point = []
                    second_point = []
                    if count == 0:
                        N1 = ((1 - local_points[0][0]) * (1 - local_points[0][1])) / 4
                        N4 = ((1 - local_points[0][0]) * (1 + local_points[0][1])) / 4
                        N3 = ((1 + local_points[0][0]) * (1 + local_points[0][1])) / 4
                        N2 = ((1 + local_points[0][0]) * (1 - local_points[0][1])) / 4
                        vector = [N1, N2, N3, N4]
                        for el1 in vector:
                            temp = []
                            for el2 in vector:
                                temp.append(el1 * el2)
                            local_matrix.append(temp)
                        first_point.append(local_matrix)

                        N1 = ((1 - local_points[1][0]) * (1 - local_points[1][1])) / 4
                        N4 = ((1 - local_points[1][0]) * (1 + local_points[1][1])) / 4
                        N3 = ((1 + local_points[1][0]) * (1 + local_points[1][1])) / 4
                        N2 = ((1 + local_points[1][0]) * (1 - local_points[1][1])) / 4
                        vector = [N1, N2, N3, N4]
                        local_matrix = []
                        for el1 in vector:
                            temp = []
                            for el2 in vector:
                                temp.append(el1 * el2)
                            local_matrix.append(temp)
                        second_point.append(local_matrix)

                        for counter, el1 in enumerate(first_point[0]):
                            temp = []
                            for i, el2 in enumerate(first_point[0]):
                                temp.append((first_point[0][counter][i] * weights[0] + second_point[0][counter][i] *
                                             weights[1]) * alfa * L / 2)
                            el.HBC.append(temp)
                        # dół
                        N1 = ((1 - local_points[0][0]) * (1 - local_points[0][1])) / 4
                        N4 = ((1 - local_points[0][0]) * (1 + local_points[0][1])) / 4
                        N3 = ((1 + local_points[0][0]) * (1 + local_points[0][1])) / 4
                        N2 = ((1 + local_points[0][0]) * (1 - local_points[0][1])) / 4
                        vector_1pc = [N1, N2, N3, N4]

                        N1 = ((1 - local_points[1][0]) * (1 - local_points[1][1])) / 4
                        N4 = ((1 - local_points[1][0]) * (1 + local_points[1][1])) / 4
                        N3 = ((1 + local_points[1][0]) * (1 + local_points[1][1])) / 4
                        N2 = ((1 + local_points[1][0]) * (1 - local_points[1][1])) / 4
                        vector_2pc = [N1, N2, N3, N4]

                        for counter_1pc, el1pc in enumerate(vector_1pc):
                            el.P.append((vector_1pc[counter_1pc] * weights[0] + vector_2pc[counter_1pc] *
                                         weights[1]) * (-alfa) * talfa * L / 2)

                    elif count == 1:
                        N1 = ((1 - local_points[2][0]) * (1 - local_points[2][1])) / 4
                        N4 = ((1 - local_points[2][0]) * (1 + local_points[2][1])) / 4
                        N3 = ((1 + local_points[2][0]) * (1 + local_points[2][1])) / 4
                        N2 = ((1 + local_points[2][0]) * (1 - local_points[2][1])) / 4
                        vector = [N1, N2, N3, N4]
                        for el1 in vector:
                            temp = []
                            for el2 in vector:
                                temp.append(el1 * el2)
                            local_matrix.append(temp)
                        first_point.append(local_matrix)

                        N1 = ((1 - local_points[3][0]) * (1 - local_points[3][1])) / 4
                        N4 = ((1 - local_points[3][0]) * (1 + local_points[3][1])) / 4
                        N3 = ((1 + local_points[3][0]) * (1 + local_points[3][1])) / 4
                        N2 = ((1 + local_points[3][0]) * (1 - local_points[3][1])) / 4
                        vector = [N1, N2, N3, N4]
                        local_matrix = []
                        for el1 in vector:
                            temp = []
                            for el2 in vector:
                                temp.append(el1 * el2)
                            local_matrix.append(temp)
                        second_point.append(local_matrix)
                        for counter, el1 in enumerate(first_point[0]):
                            temp = []
                            for i, el2 in enumerate(first_point[0]):
                                temp.append((first_point[0][counter][i] * weights[0] + second_point[0][counter][i] *
                                             weights[1]) * alfa * (L / 2.0))
                            if len(el.HBC) < 4:
                                el.HBC.append(temp)
                            else:
                                for counter2, el_H in enumerate(el.HBC):
                                    el.HBC[counter][counter2] = temp[counter2] + el.HBC[counter][counter2]

                        # prawo
                        N1 = ((1 - local_points[2][0]) * (1 - local_points[2][1])) / 4
                        N4 = ((1 - local_points[2][0]) * (1 + local_points[2][1])) / 4
                        N3 = ((1 + local_points[2][0]) * (1 + local_points[2][1])) / 4
                        N2 = ((1 + local_points[2][0]) * (1 - local_points[2][1])) / 4
                        vector_1pc = [N1, N2, N3, N4]

                        N1 = ((1 - local_points[3][0]) * (1 - local_points[3][1])) / 4
                        N4 = ((1 - local_points[3][0]) * (1 + local_points[3][1])) / 4
                        N3 = ((1 + local_points[3][0]) * (1 + local_points[3][1])) / 4
                        N2 = ((1 + local_points[3][0]) * (1 - local_points[3][1])) / 4
                        vector_2pc = [N1, N2, N3, N4]

                        for counter_1pc, el1pc in enumerate(vector_1pc):
                            if len(el.P) < 4:
                                el.P.append((vector_1pc[counter_1pc] * weights[0] + vector_2pc[counter_1pc] *
                                             weights[1]) * (-alfa) * talfa * L / 2)
                            else:
                                el.P[counter_1pc] = ((vector_1pc[counter_1pc] * weights[0] + vector_2pc[counter_1pc] *
                                                      weights[1]) * (-alfa) * talfa * L / 2) + el.P[counter_1pc]

                    elif count == 2:
                        N1 = ((1 - local_points[4][0]) * (1 - local_points[4][1])) / 4
                        N4 = ((1 - local_points[4][0]) * (1 + local_points[4][1])) / 4
                        N3 = ((1 + local_points[4][0]) * (1 + local_points[4][1])) / 4
                        N2 = ((1 + local_points[4][0]) * (1 - local_points[4][1])) / 4
                        vector = [N1, N2, N3, N4]
                        for el1 in vector:
                            temp = []
                            for el2 in vector:
                                temp.append(el1 * el2)
                            local_matrix.append(temp)
                        first_point.append(local_matrix)

                        N1 = ((1 - local_points[5][0]) * (1 - local_points[5][1])) / 4
                        N4 = ((1 - local_points[5][0]) * (1 + local_points[5][1])) / 4
                        N3 = ((1 + local_points[5][0]) * (1 + local_points[5][1])) / 4
                        N2 = ((1 + local_points[5][0]) * (1 - local_points[5][1])) / 4
                        vector = [N1, N2, N3, N4]
                        local_matrix = []
                        for el1 in vector:
                            temp = []
                            for el2 in vector:
                                temp.append(el1 * el2)
                            local_matrix.append(temp)
                        second_point.append(local_matrix)
                        for counter, el1 in enumerate(first_point[0]):
                            temp = []
                            for i, el2 in enumerate(first_point[0]):
                                temp.append(
                                    (first_point[0][counter][i] * weights[0] + second_point[0][counter][i] * weights[
                                        1]) * alfa * (L / 2.0))
                            if len(el.HBC) < 4:
                                el.HBC.append(temp)
                            else:
                                for counter2, el_H in enumerate(el.HBC):
                                    el.HBC[counter][counter2] = temp[counter2] + el.HBC[counter][counter2]
                        # góra
                        N1 = ((1 - local_points[4][0]) * (1 - local_points[4][1])) / 4
                        N4 = ((1 - local_points[4][0]) * (1 + local_points[4][1])) / 4
                        N3 = ((1 + local_points[4][0]) * (1 + local_points[4][1])) / 4
                        N2 = ((1 + local_points[4][0]) * (1 - local_points[4][1])) / 4
                        vector_1pc = [N1, N2, N3, N4]

                        N1 = ((1 - local_points[5][0]) * (1 - local_points[5][1])) / 4
                        N4 = ((1 - local_points[5][0]) * (1 + local_points[5][1])) / 4
                        N3 = ((1 + local_points[5][0]) * (1 + local_points[5][1])) / 4
                        N2 = ((1 + local_points[5][0]) * (1 - local_points[5][1])) / 4
                        vector_2pc = [N1, N2, N3, N4]

                        for counter_1pc, el1pc in enumerate(vector_1pc):
                            if len(el.P) < 4:
                                el.P.append((vector_1pc[counter_1pc] * weights[0] + vector_2pc[counter_1pc] *
                                             weights[1]) * (-alfa) * talfa * L / 2)
                            else:
                                el.P[counter_1pc] = ((vector_1pc[counter_1pc] * weights[0] + vector_2pc[counter_1pc] *
                                                      weights[1]) * (-alfa) * talfa * L / 2) + el.P[counter_1pc]

            elif g1.node[node - 1].BC and g1.node[(el.id[0]) - 1].BC:

                L = math.sqrt((pow(g1.node[node - 1].x - g1.node[(el.id[0]) - 1].x, 2)) + (
                    pow(g1.node[node - 1].y - g1.node[(el.id[0]) - 1].y, 2)))
                vector = []
                local_matrix = []
                first_point = []
                second_point = []
                N1 = ((1 - local_points[6][0]) * (1 - local_points[6][1])) / 4
                N4 = ((1 - local_points[6][0]) * (1 + local_points[6][1])) / 4
                N3 = ((1 + local_points[6][0]) * (1 + local_points[6][1])) / 4
                N2 = ((1 + local_points[6][0]) * (1 - local_points[6][1])) / 4
                vector = [N1, N2, N3, N4]
                for el1 in vector:
                    temp = []
                    for el2 in vector:
                        temp.append(el1 * el2)
                    local_matrix.append(temp)
                first_point.append(local_matrix)

                N1 = ((1 - local_points[7][0]) * (1 - local_points[7][1])) / 4
                N4 = ((1 - local_points[7][0]) * (1 + local_points[7][1])) / 4
                N3 = ((1 + local_points[7][0]) * (1 + local_points[7][1])) / 4
                N2 = ((1 + local_points[7][0]) * (1 - local_points[7][1])) / 4
                vector = [N1, N2, N3, N4]
                local_matrix = []
                for el1 in vector:
                    temp = []
                    for el2 in vector:
                        temp.append(el1 * el2)
                    local_matrix.append(temp)
                second_point.append(local_matrix)
                for counter, el1 in enumerate(first_point[0]):
                    temp = []
                    for i, el2 in enumerate(first_point[0]):
                        temp.append(
                            (first_point[0][counter][i] * weights[0] + second_point[0][counter][i] * weights[
                                1]) * alfa * (L / 2.0))
                    if len(el.HBC) < 4:
                        el.HBC.append(temp)
                    else:
                        for counter2, el_H in enumerate(el.HBC):
                            el.HBC[counter][counter2] = temp[counter2] + el.HBC[counter][counter2]
                # lewo
                N1 = ((1 - local_points[6][0]) * (1 - local_points[6][1])) / 4
                N4 = ((1 - local_points[6][0]) * (1 + local_points[6][1])) / 4
                N3 = ((1 + local_points[6][0]) * (1 + local_points[6][1])) / 4
                N2 = ((1 + local_points[6][0]) * (1 - local_points[6][1])) / 4
                vector_1pc = [N1, N2, N3, N4]

                N1 = ((1 - local_points[7][0]) * (1 - local_points[7][1])) / 4
                N4 = ((1 - local_points[7][0]) * (1 + local_points[7][1])) / 4
                N3 = ((1 + local_points[7][0]) * (1 + local_points[7][1])) / 4
                N2 = ((1 + local_points[7][0]) * (1 - local_points[7][1])) / 4
                vector_2pc = [N1, N2, N3, N4]

                for counter_1pc, el1pc in enumerate(vector_1pc):
                    if len(el.P) < 4:
                        el.P.append((vector_1pc[counter_1pc] * weights[0] + vector_2pc[counter_1pc] *
                                     weights[1]) * (-alfa) * talfa * L / 2)
                    else:
                        el.P[counter_1pc] = ((vector_1pc[counter_1pc] * weights[0] + vector_2pc[counter_1pc] * weights[
                            1]) * (-alfa) * talfa * L / 2) + el.P[counter_1pc]
