import csv
from pulp import *
import math

DAY = 8
AVERAGE_TEMP = 7

def parse_data(filename):
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            data.append((int(row[DAY]), float(row[AVERAGE_TEMP])))
    return data

def local_temp_solver(data):
    n = len(data)
    days = map(lambda datum: datum[0], data)
    temps = map(lambda datum: datum[1], data)

    print(days)
    print(temps)

    prob = LpProblem('Local Temperature Change', LpMinimize)
    x1 = LpVariable('x1')
    x2 = LpVariable('x2')
    x3 = LpVariable('x3')
    x4 = LpVariable('x4')
    x5 = LpVariable('x5')
    x6 = LpVariable('x6')
    e = LpVariable('e')

    prob += e

    for i in range(n):
        prob += (e >= x1 + 
                      x2 * days[i] + 
                      x3 * math.cos((2 * math.pi * days[i])/365.25) + 
                      x4 * math.sin((2 * math.pi * days[i])/365.25) +
                      x5 * math.cos((2 * math.pi * days[i])/(365.25 * 10.7)) +
                      x6 * math.sin((2 * math.pi * days[i])/(365.25 * 10.7)) 
                      - temps[i] )
        prob += (e >= -1 * x1 - 
                      x2 * days[i] - 
                      x3 * math.cos((2 * math.pi * days[i])/365.25) - 
                      x4 * math.sin((2 * math.pi * days[i])/365.25) -
                      x5 * math.cos((2 * math.pi * days[i])/(365.25 * 10.7)) -
                      x6 * math.sin((2 * math.pi * days[i])/(365.25 * 10.7)) 
                      + temps[i] )
    prob.writeLP("local_temp.lp")
    prob.solve()

    print 'Status: ' + LpStatus[prob.status]
    print '\tx1: ' + str(value(x1))
    print '\tx2: ' + str(value(x2))
    print '\tx3: ' + str(value(x3))
    print '\tx4: ' + str(value(x4))
    print '\tx5: ' + str(value(x5))
    print '\tx5: ' + str(value(x5))
    

if __name__ == '__main__':
    test_data = parse_data('Corvallis.csv')
    local_temp_solver(test_data)



