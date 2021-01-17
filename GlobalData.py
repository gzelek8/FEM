class GlobalData:
    H = 0.1
    W = 0.1
    nH = 31
    nW = 31
    simulation_step = 50
    simulation_time = 10000
    simulation_iteration = simulation_time/simulation_step
    k = 25
    c = 700
    ro = 7800
    alfa = 300.0
    talfa = 1200
    amount_integral_point = 2
    nN = nH * nW
    nE = (nH - 1) * (nW - 1)
    var = [H, W, nH, nW]
    initial_temperature = 100
