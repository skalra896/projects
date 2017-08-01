from random import randint
# prediction location

from math import sin, tan, sqrt

xvaliddi = float(raw_input())
ddi = float(raw_input())
tdis = int(raw_input())
ptdi = int(raw_input())
ttdi = ptdi - tdis
des = float(xvaliddi * ttdi)
y = float(des * sin(ddi))
x = float(y / tan(ddi))
print x, y

# region formation
xvalid = []
yvalid = []
n = randint(0, 10)
print "enter" + str(n) + "values"
for i in range(n):
    (a, b) = map(float, raw_input().split())

    if x and y:
        xvalid.append(a)
        yvalid.append(b)

sol = [0, 0]


# fitness function
def fun(a, b, x, y):
    z = float(sqrt((x - a) ** 2 + (y - b) ** 2))
    return z


# optimal result


r = randint(0, 501)
qmin = 20
qmax = 500
f = 999999
i = 0
v=364
best = []
best = sol
while (sol != [x, y] and i < n):

    q = qmin + (qmin - qmax) % r
    v= v + sqrt((sol[0] - best[0])**2 + (sol[1]-best[1])**2)* q

    sol[0] = sol[0] + v
    sol[1] = sol[1] + v
    a = sol[0]
    b = sol[1]
    fnew = fun(a, b, x, y)
    if (fnew <= f and (a == xvalid[i] or b == yvalid[i])):
        f = fnew
        best[0] = a
        best[1] = b
        i += 1
    else:
        i += 1
    print sol



