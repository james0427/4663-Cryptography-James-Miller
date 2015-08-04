###############################################
# Name: James Miller
# Class: CMPS 4663 Cryptography
# Date: 30 July 2015
# Program 3 - Elliptical Points
###############################################

import numpy as np
import matplotlib.pyplot as plt

class Elliptical:
    #"""
    #Initiates the object with the values that are passed into it
    #
    # Returns the object with the values assigned
    #"""
    def __init__(self,x1,x2,y1,y2,a,b):
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.y1 = float(y1)
        self.y2 = float(y2)
        self.a = float(a)
        self.b = float(b)

    #"""
    #Get slope Method:
    #
    #This method takes the values and plugs them into the slop formual
    #
    #@param   Takes the values of X1,X2,Y1,Y2
    #@returns The slope of the values y2-y1/x2-x1
    #"""
    def getslope(self,x1,x2,y1,y2):
        #if x1 != x2 and y1 != y2:
        m = ((y2-y1)/(x2-x1))
        return m
        #else:
            #m = ((3 * x1)**2) + 9/ 2 * y1

#"""
# GetPoints Method:
# This method calculates a given point on the elliptical curve
#
#@param   The slope, x1, x2, and y2
#@returns Returns the x value and the y value of a point on the elliptical curve
#"""
    def getPoints(self,m,x1,x2,y2):
        xr = pow(m,2) - x2 - x1
        yr = y2 + (m * xr) - (m * x2)
        return xr,yr

#"""
# Curve Method
# This method first finds the max values of the grid and then adds 1 to incrase the range
#      Afterwhich, it created the height and width to those values, it then draws the elliptical curve based on a b
#           Once the curve has been draw it assigns the values to it and plots them.
#               Finallt it draws our the display for us to see
#
#@param   X1,X2,Y1,Y2,X3,Y3,Slope,a,b
#@returns Displays the draw out graph with plots and curve
#"""

    def curve(self,x1,x2,y1,y2,xr,yr,m,a,b):
        listx = [abs(x1),abs(x2),abs(xr)]
        listy = [abs(y1),abs(y2),abs(yr)]

        h = max(listy) + 1
        w = max(listx) + 1

        an1 = plt.annotate("James Miller", xy=(-w+.5 , h-.5), xycoords="data",
            va="center", ha="center",
            bbox=dict(boxstyle="round", fc="w"))

        y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

        plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x  + b), [0])
        plt.contour(x.ravel(), y.ravel(), (y-y1) - m*(x-x1), [0],colors=('pink'))
        plt.grid()

        plt.plot(x1, y1,'ro')
        plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1-.5,y1-1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )

        plt.plot(x2, y2,'ro')
        plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2-.5,y2-1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )

        plt.plot(xr, yr,'ro')

        plt.annotate('x3,y3', xy=(xr, yr), xytext=(xr+1,yr-1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )
        plt.show()
