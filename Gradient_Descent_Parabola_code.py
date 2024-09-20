"""
Gradient Descent on a Parabola

The code takes the slope/derivative (dy/dx = 2x) of the equation of the parabola (y = x^2) and uses the derivative to move down the parabola to find the minimum. 
The slope of the parabola depends on the value of x. We use this slope to step down to the parabola's minimum.
The step is created by multiplying the learning rate (which makes sure the step is not too large) and the derivative.

In an equation, when you subtract the slope from x, the answer (the new x) will have a lower y-value than the previous x.
"""


import matplotlib.pyplot as plt
import numpy as np

lr = .05 # Learning Rate - 
x = -3 # Starting Value - the value it starts going down from

xvalues = np.array([x])
for i in range(100):
  x = x - (lr)*(2)*(x) # finds the next x value that is has a lower y-value to keep moving down. 
  #print(i, x)
  xvalues = np.append(xvalues, x) # stores all x-values so that we can see it going down in a graph

yvalues = xvalues**2
#print(yvalues)

plt.scatter(xvalues, yvalues, c = "red", s = 20, label = "Steps Taken During Gradient Descent")

#xoriginalcurve = np.arange(-3.5, 3.6, .1)# Here, you give the step size, and Python finds out how many points. It does not include the last number (here it will be 3.5).
xoriginalcurve = np.linspace(-3.5, 3.5, 100)# this is the opposite of arange because you give it the number of points and it finds the size of the steps.
yoriginalcurve = xoriginalcurve**2
plt.plot(xoriginalcurve, yoriginalcurve, label = "Original Curve")
plt.legend()
plt.grid()
