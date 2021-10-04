#Parker Hodgkins, MatPlot, Numpy, Scipy

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Gets inputs
print("What is x0? ")
x0 = float(input())

print("What is y0? ")
y0 = float(input())

print("What is h? ")
h = float(input())

#array to store points for later plotting
points_x = [x0]
points_y = [y0]

#dy/dx
def dy_dx(x, y):
    return -y + np.log(x)

#ODEINT METHOD
#def model(y, t):
 #   x = np.log(t)
  #  dydx = -y + x
   # return dydx


#t = np.linspace(0, 140)

#y = odeint(model, y0, t)

#plt.plot(t, y, "g:")
#ODEINT END

#solves all k values for RKF
def k1(xn, yn):
    return dy_dx(xn, yn)


def k2(xn, yn):
    return dy_dx(xn + h/2, yn + h * (k1(xn, yn) / 2))


def k3(xn, yn):
    return dy_dx(xn + h/2, yn + h * (k2(xn, yn) / 2))


def k4(xn, yn):
    return dy_dx(xn + h, yn + h * k3(xn, yn))


def runge_print(steps, xn, yn):
    if steps < 501:
        print("x", steps, ": ", round(xn + h, 4), ", y", steps, ": ", round(runge_solve(xn, yn), 4))
        steps2 = steps + 1
        yn2 = runge_solve(xn, yn)
        xn2 = xn + h
        points_x.append(xn2)
        points_y.append(yn2)
        runge_print(steps2, xn2, yn2)



def runge_solve(xn, yn):
    return yn + (1.0/6.0) * h * (k1(xn, yn) + 2 * k2(xn, yn) + 2 * k3(xn, yn) + k4(xn, yn))


runge_print(1, x0, y0)

plt.plot(points_x, points_y, "r-")
plt.xlabel("Time")
plt.ylabel("f(x)")

plt.show()
