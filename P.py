def fil_in_global_p(elements, amount_of_nodes):
    global_p = [0 for el in range(amount_of_nodes)]
    for el in elements:
        for count, el2 in enumerate(el.P):
            global_p[el.id[count] - 1] = global_p[el.id[count] - 1] + el2
    return global_p
