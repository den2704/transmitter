import math

input_file = 'input.txt'
my_output = 'my_output.txt'
coords = []
measure = []

result_system1 = []
result_system2 = []
result_system3 = []

with open(input_file) as file:
    key = 0
    for line in file:
        if key == 0:
            coords.append(line.replace('\n', '').split(','))
            key += 1
        else:
            measure.append(line.replace('\n', '').split(','))

for i in range(len(coords[0])):
    coords[0][i] = float(coords[0][i])

for r in range(len(measure)):
    for c in range(len(measure[r])):
        measure[r][c] = float(measure[r][c])
print('Положение статичных приемников:')
print(coords)
print('Данные измерений:')
print(measure)
print('Количество измерений:')
print(len(measure))

# статичные радиоприемники - координаты
x1 = coords[0][0]
y1 = coords[0][1]
x2 = coords[0][2]
y2 = coords[0][3]
x3 = coords[0][4]
y3 = coords[0][5]


def system1(d1_f, d2_f, d3_f):  # решение системы из двух уравнений - третье для проверки
    global x1, x2, x3, y1, y2, y3
    global x_min, x_max, y_min, y_max
    # (x-x1)**2 + (y-y1)**2 = (d1*10**6)**2
    # (x-x2)**2 + (y-y2)**2 = (d2*10**6)**2
    # (x-x3)**2 + (y-y3)**2 = (d3*10**6)**2

    # x**2 + y**2 - 2*x1*x - 2*y1*y = (d1*10**6)**2 - x1**2 - y1**2
    # x**2 + y**2 - 2*x2*x - 2*y2*y = (d2*10**6)**2 - x2**2 - y2**2
    # x**2 + y**2 - 2*x3*x - 2*y3*y = (d3*10**6)**2 - x3**2 - y3**2

    # вычитаем из первого второе
    # - 2*x1*x - 2*y1*y + 2*x2*x + 2*y2*y = (d1*10**6)**2 - x1**2 - y1**2 - (d2*10**6)**2 + x2**2 + y2**2
    num = (d1_f*10**6)**2 - x1**2 - y1**2 - (d2_f*10**6)**2 + x2**2 + y2**2
    # 2*(-x1+x2)*x + 2*(-y1+y2)*y = num
    # x = ((num - 2*(-y1+y2)*y) / 2*(-x1+x2)) = a - b*y
    a = num / (2*(x2-x1))
    b = (y2 - y1) / (x2 - x1)

    # подставляем в первое x**2 + y**2 - 2*x1*x - 2*y1*y = (d1*10**6)**2 - x1**2 - y1**2
    num1 = (d1_f*10**6)**2 - x1**2 - y1**2

    # (a - b*y)**2 + y**2 - 2*x1*(a - b*y) - 2*y1*y = num1
    # a**2 - 2*a*b*y + b**2*y**2 + y**2 - 2*x1*a + 2*x1*b*y - 2*y1*y = num1
    # (b**2+1)*y**2 + (-2*a*b+2*x1*b-2*y1)*y + (a**2 - 2*x1*a - num1) = 0
    l = b**2 + 1
    m = -2*a*b + 2*x1*b - 2*y1
    n = a**2 - 2*x1*a - num1
    D = m**2 - 4*l*n

    if D >= 0:
        y_1 = (math.sqrt(D) - m) / (2*l)
        y_2 = (-math.sqrt(D) - m) / (2*l)
        x_1 = (num - 2 * (-y1 + y2) * y_1) / (2 * (-x1 + x2))
        x_2 = (num - 2 * (-y1 + y2) * y_2) / (2 * (-x1 + x2))

        # проверяем - укладывается ли d3 в диапазон 10%?
        # (x-x3)**2 + (y-y3)**2 = (d3*10**6)**2

        left1 = ((x_1 - x3)**2 + (y_1 - y3)**2)
        # right1 = ((d3_f*10**6)**2)

        d3_f_v = math.sqrt(left1) / 10**6
        if math.fabs(d3_f_v - d3_f) < 0.1*d3_f:
            # print('x_1', x_1, 'y_1', y_1)
            x_list.append(x_1)
            y_list.append(y_1)

        left2 = ((x_2 - x3) ** 2 + (y_2 - y3) ** 2)
        # right2 = ((d3_f * 10 ** 6) ** 2)

        d3_f_v = math.sqrt(left2) / 10**6
        if math.fabs(d3_f_v - d3_f) < 0.1*d3_f:
            # print('x_2', x_2, 'y_2', y_2)
            x_list.append(x_2)
            y_list.append(y_2)


def system2(d1_f, d2_f, d3_f):  # решение системы из двух уравнений - второе для проверки
    global x1, x2, x3, y1, y2, y3
    global x_min, x_max, y_min, y_max
    # (x-x1)**2 + (y-y1)**2 = (d1*10**6)**2
    # (x-x2)**2 + (y-y2)**2 = (d2*10**6)**2
    # (x-x3)**2 + (y-y3)**2 = (d3*10**6)**2

    # x**2 + y**2 - 2*x1*x - 2*y1*y = (d1*10**6)**2 - x1**2 - y1**2
    # x**2 + y**2 - 2*x2*x - 2*y2*y = (d2*10**6)**2 - x2**2 - y2**2
    # x**2 + y**2 - 2*x3*x - 2*y3*y = (d3*10**6)**2 - x3**2 - y3**2

    # вычитаем из первого третье
    # - 2*x1*x - 2*y1*y + 2*x3*x + 2*y3*y = (d1*10**6)**2 - x1**2 - y1**2 - (d3*10**6)**2 + x3**2 + y3**2
    num = (d1_f*10**6)**2 - x1**2 - y1**2 - (d3_f*10**6)**2 + x3**2 + y3**2
    # 2*(-x1+x3)*x + 2*(-y1+y3)*y = num
    # x = ((num - 2*(-y1+y3)*y) / 2*(-x1+x3)) = a - b*y
    a = num / (2*(x3-x1))
    b = (y3 - y1) / (x3 - x1)

    # подставляем в первое x**2 + y**2 - 2*x1*x - 2*y1*y = (d1*10**6)**2 - x1**2 - y1**2
    num1 = (d1_f*10**6)**2 - x1**2 - y1**2

    # (a - b*y)**2 + y**2 - 2*x1*(a - b*y) - 2*y1*y = num1
    # a**2 - 2*a*b*y + b**2*y**2 + y**2 - 2*x1*a + 2*x1*b*y - 2*y1*y = num1
    # (b**2+1)*y**2 + (-2*a*b+2*x1*b-2*y1)*y + (a**2 - 2*x1*a - num1) = 0
    l = b**2 + 1
    m = -2*a*b + 2*x1*b - 2*y1
    n = a**2 - 2*x1*a - num1
    D = m**2 - 4*l*n

    if D >= 0:
        y_1 = (math.sqrt(D) - m) / (2*l)
        y_2 = (-math.sqrt(D) - m) / (2*l)
        x_1 = (num - 2 * (-y1 + y3) * y_1) / (2 * (-x1 + x3))
        x_2 = (num - 2 * (-y1 + y3) * y_2) / (2 * (-x1 + x3))

        # проверяем - укладывается ли d2 в диапазон 10%?
        # (x-x2)**2 + (y-y2)**2 = (d2*10**6)**2

        left2 = ((x_1 - x2)**2 + (y_1 - y2)**2)
        # right1 = ((d2_f*10**6)**2)

        d2_f_v = math.sqrt(left2) / 10**6
        if math.fabs(d2_f_v - d2_f) < 0.1*d2_f:
            # print('x_1', x_1, 'y_1', y_1)
            x_list.append(x_1)
            y_list.append(y_1)

        left2 = ((x_2 - x2) ** 2 + (y_2 - y2) ** 2)
        # right2 = ((d2_f * 10 ** 6) ** 2)

        d2_f_v = math.sqrt(left2) / 10**6
        if math.fabs(d2_f_v - d2_f) < 0.1*d2_f:
            # print('x_2', x_2, 'y_2', y_2)
            x_list.append(x_2)
            y_list.append(y_2)


def system3(d1_f, d2_f, d3_f):  # решение системы из двух уравнений - второе для проверки
    global x1, x2, x3, y1, y2, y3
    global x_min, x_max, y_min, y_max
    # (x-x1)**2 + (y-y1)**2 = (d1*10**6)**2
    # (x-x2)**2 + (y-y2)**2 = (d2*10**6)**2
    # (x-x3)**2 + (y-y3)**2 = (d3*10**6)**2

    # x**2 + y**2 - 2*x1*x - 2*y1*y = (d1*10**6)**2 - x1**2 - y1**2
    # x**2 + y**2 - 2*x2*x - 2*y2*y = (d2*10**6)**2 - x2**2 - y2**2
    # x**2 + y**2 - 2*x3*x - 2*y3*y = (d3*10**6)**2 - x3**2 - y3**2

    # вычитаем из второго третье
    # - 2*x2*x - 2*y2*y + 2*x3*x + 2*y3*y = (d2*10**6)**2 - x2**2 - y2**2 - (d3*10**6)**2 + x3**2 + y3**2
    num = (d2_f * 10 ** 6) ** 2 - x2 ** 2 - y2 ** 2 - (d3_f * 10 ** 6) ** 2 + x3 ** 2 + y3 ** 2
    # 2*(-x2+x3)*x + 2*(-y2+y3)*y = num
    # x = ((num - 2*(-y2+y3)*y) / 2*(-x2+x3)) = a - b*y
    a = num / (2 * (x3 - x2))
    b = (y3 - y2) / (x3 - x2)

    # подставляем во второе x**2 + y**2 - 2*x2*x - 2*y2*y = (d2*10**6)**2 - x2**2 - y2**2
    num2 = (d2_f * 10 ** 6) ** 2 - x2 ** 2 - y2 ** 2

    # (a - b*y)**2 + y**2 - 2*x2*(a - b*y) - 2*y2*y = num2
    # a**2 - 2*a*b*y + b**2*y**2 + y**2 - 2*x2*a + 2*x2*b*y - 2*y2*y = num2
    # (b**2+1)*y**2 + (-2*a*b+2*x2*b-2*y2)*y + (a**2 - 2*x2*a - num2) = 0
    l = b ** 2 + 1
    m = -2 * a * b + 2 * x2 * b - 2 * y2
    n = a ** 2 - 2 * x2 * a - num2
    D = m ** 2 - 4 * l * n

    if D >= 0:
        y_1 = (math.sqrt(D) - m) / (2 * l)
        y_2 = (-math.sqrt(D) - m) / (2 * l)
        x_1 = (num - 2 * (-y2 + y3) * y_1) / (2 * (-x2 + x3))
        x_2 = (num - 2 * (-y2 + y3) * y_2) / (2 * (-x2 + x3))

        # проверяем - укладывается ли d1 в диапазон 10%?
        # (x-x1)**2 + (y-y1)**2 = (d1*10**6)**2

        left1 = ((x_1 - x1) ** 2 + (y_1 - y1) ** 2)
        # right1 = ((d1_f*10**6)**2)

        d1_f_v = math.sqrt(left1) / 10 ** 6
        if math.fabs(d1_f_v - d1_f) < 0.1 * d1_f:
            # print('x_1', x_1, 'y_1', y_1)
            x_list.append(x_1)
            y_list.append(y_1)

        left1 = ((x_2 - x1) ** 2 + (y_2 - y1) ** 2)
        # right2 = ((d2_f * 10 ** 6) ** 2)

        d1_f_v = math.sqrt(left1) / 10 ** 6
        if math.fabs(d1_f_v - d1_f) < 0.1 * d1_f:
            # print('x_2', x_2, 'y_2', y_2)
            x_list.append(x_2)
            y_list.append(y_2)


def answer1(d1, d2, d3):
    global x_min, x_max, y_min, y_max
    # print(d1, d2, d3)
    d1_min = d1 - 0.05*d1/2
    d1_max = d1 + 0.05*d1/2
    d2_min = d2 - 0.05*d2/2
    d2_max = d2 + 0.05*d2/2
    d3_min = d3 - 0.05*d3/2
    d3_max = d3 + 0.05*d3/2
    d1_v = d1_min
    d2_v = d2_min
    d3_v = d3_min
    accuracy = 0.0000001
    while d1_v < d1_max:
        while d2_v < d2_max:
            while d3_v < d3_max:
                # print(d1_v, d2_v, d3_v)
                system1(d1_v, d2_v, d3_v)
                d3_v += accuracy * d3
            d2_v += accuracy * d1
        d1_v += accuracy * d1
    if len(x_list) !=0:
        # print(len(x_list))
        x_av = sum(x_list)
        x_av = x_av / len(x_list)
    if len(y_list) != 0:
        # print(len(y_list))
        y_av = sum(y_list)
        y_av = y_av / len(y_list)
    # print('x_av', x_av, 'y_av', y_av)
    if len(x_list) !=0 and len(y_list) != 0:
        result_system1.append([x_av, y_av])


def answer2(d1, d2, d3):
    global x_min, x_max, y_min, y_max
    # print(d1, d2, d3)
    d1_min = d1 - 0.05*d1/2
    d1_max = d1 + 0.05*d1/2
    d2_min = d2 - 0.05*d2/2
    d2_max = d2 + 0.05*d2/2
    d3_min = d3 - 0.05*d3/2
    d3_max = d3 + 0.05*d3/2
    d1_v = d1_min
    d2_v = d2_min
    d3_v = d3_min
    accuracy = 0.0000001
    while d1_v < d1_max:
        while d2_v < d2_max:
            while d3_v < d3_max:
                # print(d1_v, d2_v, d3_v)
                system2(d1_v, d2_v, d3_v)
                d3_v += accuracy * d3
            d2_v += accuracy * d1
        d1_v += accuracy * d1
    if len(x_list) !=0:
        # print(len(x_list))
        x_av = sum(x_list)
        x_av = x_av / len(x_list)
    if len(y_list) != 0:
        # print(len(y_list))
        y_av = sum(y_list)
        y_av = y_av / len(y_list)
    # print('x_av', x_av, 'y_av', y_av)
    if len(x_list) !=0 and len(y_list) != 0:
        result_system2.append([x_av, y_av])


def answer3(d1, d2, d3):
    global x_min, x_max, y_min, y_max
    # print(d1, d2, d3)
    d1_min = d1 - 0.05*d1/2
    d1_max = d1 + 0.05*d1/2
    d2_min = d2 - 0.05*d2/2
    d2_max = d2 + 0.05*d2/2
    d3_min = d3 - 0.05*d3/2
    d3_max = d3 + 0.05*d3/2
    d1_v = d1_min
    d2_v = d2_min
    d3_v = d3_min
    accuracy = 0.0000001
    while d1_v < d1_max:
        while d2_v < d2_max:
            while d3_v < d3_max:
                # print(d1_v, d2_v, d3_v)
                system3(d1_v, d2_v, d3_v)
                d3_v += accuracy * d3
            d2_v += accuracy * d1
        d1_v += accuracy * d1
    if len(x_list) !=0:
        # print(len(x_list))
        x_av = sum(x_list)
        x_av = x_av / len(x_list)
    if len(y_list) != 0:
        # print(len(y_list))
        y_av = sum(y_list)
        y_av = y_av / len(y_list)
    # print('x_av', x_av, 'y_av', y_av)
    if len(x_list) !=0 and len(y_list) != 0:
        result_system3.append([x_av, y_av])


for n in range(len(measure)):
    x_list = []
    y_list = []
    d1 = measure[n][0]
    d2 = measure[n][1]
    d3 = measure[n][2]
    # print(d1, d2, d3)
    answer1(d1, d2, d3)
    answer2(d1, d2, d3)
    answer3(d1, d2, d3)

print('Результаты 1:')
print(result_system1)
print(len(result_system1))

print('Результаты 2:')
print(result_system2)
print(len(result_system2))

print('Результаты 3:')
print(result_system3)
print(len(result_system3))
