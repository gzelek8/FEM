import math


def calculate_function(x, y):
    output = -5 * (x * x * y) + 2 * (x * y * y) + 10
    return output


def calculate_integral_2_node():
    weight = 1
    f1 = calculate_function(-0.577, -0.577)
    f2 = calculate_function(0.577, -0.577)
    f3 = calculate_function(-0.577, 0.577)
    f4 = calculate_function(0.577, 0.577)
    output = f1 * weight * weight + f2 * weight * weight + f3 * weight * weight + f4 * weight * weight
    return output


def calculate_integral_3_node():
    weight1 = 5 / 9
    weight2 = 8 / 9
    weight3 = 5 / 9
    f1 = calculate_function(-0.777, -0.77)
    f2 = calculate_function(0, -0.77)
    f3 = calculate_function(0.77, -0.77)
    f4 = calculate_function(-0.77, 0)
    f5 = calculate_function(0, 0)
    f6 = calculate_function(0.77, 0)
    f7 = calculate_function(-0.77, 0.77)
    f8 = calculate_function(0, 0.77)
    f9 = calculate_function(0.77, 0.77)
    output = f1 * weight1 * weight1\
             + f2 * weight2 * weight1\
             + f3 * weight3 * weight1\
             + f4 * weight1 * weight2\
             + f5 * weight2 * weight2\
             + f6 * weight3 * weight2\
             + f7 * weight1 * weight3\
             + f8 * weight2 * weight3\
             + f9 * weight3 * weight3
    return output


def calculate_integral_4_node():
    w1 = (18 - math.sqrt(30)) / 36
    w2 = (18 + math.sqrt(30)) / 36
    weight1 = w2
    weight2 = w1
    weight3 = w1
    weight4 = w2
    f1 = calculate_function(-0.8611363115940526, -0.8611363115940526)
    f2 = calculate_function(-0.3399810435848563, -0.8611363115940526)
    f3 = calculate_function(0.3399810435848563, -0.8611363115940526)
    f4 = calculate_function(0.8611363115940526, -0.8611363115940526)
    f5 = calculate_function(-0.8611363115940526, -0.3399810435848563)
    f6 = calculate_function(-0.3399810435848563, -0.3399810435848563)
    f7 = calculate_function(0.3399810435848563, -0.3399810435848563)
    f8 = calculate_function(0.8611363115940526, -0.3399810435848563)
    f9 = calculate_function(-0.8611363115940526, 0.3399810435848563)
    f10 = calculate_function(-0.3399810435848563, 0.3399810435848563)
    f11 = calculate_function(0.3399810435848563, 0.3399810435848563)
    f12 = calculate_function(0.8611363115940526, 0.3399810435848563)
    f13 = calculate_function(-0.8611363115940526, 0.8611363115940526)
    f14 = calculate_function(-0.3399810435848563, 0.8611363115940526)
    f15 = calculate_function(0.3399810435848563, 0.8611363115940526)
    f16 = calculate_function(0.8611363115940526, 0.8611363115940526)
    output = f1 * weight1 * weight1\
             + f2 * weight2 * weight1\
             + f3 * weight3 * weight1\
             + f4 * weight4 * weight1\
             + f5 * weight1 * weight2\
             + f6 * weight2 * weight2\
             + f7 * weight3 * weight2\
             + f8 * weight4 * weight2\
             + f9 * weight1 * weight3\
             + f10 * weight2 * weight3\
             + f11 * weight3 * weight3\
             + f12 * weight4 * weight3\
             + f13 * weight1 * weight4\
             + f14 * weight2 * weight4\
             + f15 * weight3 * weight4\
             + f16 * weight4 * weight4
    return output


print(calculate_integral_2_node())
print(calculate_integral_3_node())
print(calculate_integral_4_node())
