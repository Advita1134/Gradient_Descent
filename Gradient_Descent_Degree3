"""
Gradient Descent on an equation with the highest power(degree) of 3.

This code finds the derivative (dy/dx) to go down the original curve.
The equation of the curve was x^3-4x making the derivative 3x^2 - 4.
We subtracted the point's slope (multiplied by the learning rate so that it would not be too much) from the x-value of the starting point to create an x closer to the local minimum.
Then, this process is repeated 100 times to make the x have a lower y-value each time (to be closer to the minimum).

"""

import matplotlib.pyplot as plt
import numpy as np

## Gradient Descent ##
x = -1 # starting x-value to step down from
x_gd_values= [x] # the list of x-values, so that the points showing the steps down the curve can be graphed
lr = .005 # learning rate (makes sure that the steps are not too big)

for a in range(100):
  x = x - lr * (3*(x)**2 - 4) # finding the new x using the previous x-value, learning rate, and derivative
  x_gd_values.append(x) # appending the new x into list to be able to make a graph of the points
  #print(a, x2)

x_gd_values = np.array(x_gd_values) # converting into NumPy array to be able to easily find the y-values without a for loop to go through every single x-value and find the y.
y_gd_values = x_gd_values**3 - 4*x_gd_values # calculating the y-values using the x-values used for gradient descent.
plt.scatter(x_gd_values, y_gd_values) # graphing the points to show how they get lower on the curve.

## Original Curve ##
xcurve = np.linspace(-5, 5, 100) # gives 100 points evenly spaced between -5 and 5
ycurve = xcurve**3-4*xcurve # equation (x^3 - 4x)
plt.plot(xcurve, ycurve) # plotting the x and y values based on the equation of the original curve.



