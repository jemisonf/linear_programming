from pulp import *


def max_deviation(points):
    n = len(points)
    xs = map(lambda point: point[0], points)
    ys = map(lambda point: point[1], points)

    prob = LpProblem('Maximum deviation', LpMinimize)
    a = LpVariable('a')
    b = LpVariable('b')
    e = LpVariable('e')

    prob += e

    for i in range(0, n):
        prob += e >= a*xs[i] + b - ys[i]
        prob += e >= -a*xs[i] - b + ys[i]

    prob.writeLP('max_deviation.lp')
    prob.solve()

    print 'Status: ' + LpStatus[prob.status]
    print 'a: ' + str(value(a))
    print 'b: ' + str(value(b))
    print 'e: ' + str(value(e))

if __name__ == '__main__':
    test_data = [(1, 3), (2, 5), (3, 7), (5, 11), (7, 14), (8, 15), (10, 19)]
    max_deviation(test_data)
