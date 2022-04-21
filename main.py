import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

dots = []
xi = []
ni = []
pi = []


def drawEmperical():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    fig.suptitle('График эмперической функции')
    h = pi[0]
    plt.plot([xi[0] - 0.5, xi[0]], [0, 0])
    for i in range(len(xi) - 1):
        plt.plot([xi[i], xi[i + 1]], [h, h])
        h += pi[i + 1]
    plt.plot([xi[len(xi) - 1], xi[len(xi) - 1] + 1], [1, 1])
    plt.grid()
    plt.show()


def drawPoligon():
    h = (dots[len(dots) - 1] - dots[0]) / (1 + (math.log(len(dots)) / math.log(2)))
    m = math.ceil(1 + math.log(len(dots)) / math.log(2))
    x = dots[0] - h / 2
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('pi')
    x1 = []
    y1 = []
    fig.suptitle('Полигон частот')
    for i in range(m):
        c = 0
        for k in dots:
            if (k >= x and k < (x + h)):
                c += 1
        x1.append(x + h / 2)
        y1.append(c / len(dots))
        x += h
    plt.plot(x1, y1, '--o')
    plt.show()


def drawHistogram():
    h = (dots[len(dots) - 1] - dots[0]) / (1 + (math.log(len(dots)) / math.log(2)))
    m = math.ceil(1 + math.log(len(dots)) / math.log(2))
    x = dots[0] - h / 2
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('pi')

    fig.suptitle('Гистограмма частот')
    for i in range(m):
        c = 0
        for k in dots:
            if (k >= x and k < (x + h)):
                c += 1
        plt.plot([x, x + h], [c / len(dots) / h, c / len(dots) / h])
        plt.fill_between([x, x + h], [c / len(dots) / h, c / len(dots) / h])
        # print(x, x + h)
        x += h
    plt.show()


def matDespOtkl():
    k = list(set(dots))
    k.sort()
    for i in k:
        count = 0
        xi.append(i)
        for j in dots:
            if j == i:
                count += 1
        ni.append(count)
        pi.append(count / len(dots))
    expectedValue = 0
    for i in range(len(xi)):
        expectedValue += xi[i] * pi[i]
    print("Оценка математического ожидания:")
    print("%.2f" % expectedValue)
    dispersia = 0
    for i in range(len(xi)):
        dispersia += pow(xi[i] - expectedValue, 2) * ni[i]
    dispersia = dispersia * (1 / len(dots))
    print("Дисперсия:")
    print("%.2f" % dispersia)
    print("Среднеквадратичное отклонение:")
    print("%.2f" % math.sqrt(dispersia))
    print("Выборка:")
    for i in range(len(xi)):
        print(xi[i], " ", ni[i], " ", pi[i])


def main():
    f = open('input.txt')
    for i in f:
        dots.append(float(i))
    dots.sort()
    print("Вариационный ряд:")
    print(dots)
    print("Экстремальные значения:")
    print("Min = {0}\nMax = {1}".format(dots[0], dots[len(dots) - 1]))
    print("Размах выборки:")
    print(abs(dots[0]) + abs(dots[len(dots) - 1]))
    matDespOtkl()
    h = pi[0]
    print("Эмперическая функция:")
    print("0 если -∞ < x <= {0}".format(xi[0]))
    for i in range(len(xi) - 1):
        print("%.2f" % h + " если {0} < x <= {1}".format(xi[i], xi[i + 1]))
        h += pi[i + 1]
    print("1 если {0} <x <= ∞".format(xi[len(xi) - 1]))
    drawEmperical()
    drawPoligon()
    drawHistogram()


main()
