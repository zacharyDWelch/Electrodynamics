import numpy as np
import random as rnd
import math as m
import tkinter
import Drawing

# Set up circle
# Set up random for points
# Set up random 5 points
# Set up a test point
# Set up vectors for rand point to test point
# Calculate the field at given points, and test point.


"""
*************** Things to think about *************************

How is the drawing system going to work?
    - Should another class be made just for the drawing.
    
Should there be one set of coordinates, and not worry about converting from one to another?
    - Moreover what coordinate system would be best for this task?
    - Should another function be made to convert from one to another?

Should a class be set up to make and set the random points?
    - Doing it this way would make it just a point and click, 
      as well as not needing to read the data in an output console 
    - Construct each point as an object. 

ToDo:

Get the main logic working.
Setup a function to get the coordinates of the drawn circle



"""


class CircleProblem:

    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos

    def coordinatesToVector(self, x,y):
        """
        Sets up the coordinates random points on circle.

        :param x: Set of the x coordinate
        :param y: Set of the y coordinate
        :return:

        """
        return None


    def getCircleCoords(self):
        """
        Get Coordinates from the circle in drawing.

        """
        a = m.sqrt((x * x) + (y * y))

        return None

    def setRandomPoints(self):
        """
        Set up points on the circle.

        :return:
        Coordinates < x,y >
        Place points on circle
        """

        return None

    def getRandPoints(self):
        """
        Get the coordinates for the 5 points on the circle
        """

        return None

    def setTestPoint(self):
        """
        Set up the test point

        either by click, or have randomly set up
        """
        return None

    def getTestPoint(self):
        """
        Get the test point
        """
        return None

    def CoolombsLaw(self, q, Q, r):
        """
        :param q: Charge 1
        :param Q: Charge 2
        :param r: Distance between 1 and 2


        Global: Epsolon

        :return:
        forceTotal: The total force of all charges
        """
        forceTotal = 0
        force = []

        Ep = 8.81
        k = 1 / (4 * m.pi * Ep)

        for charge in range(0, 5):
            force.append(k * (q * Q) / r**2)

        for forces in force:
            force[forces] += forceTotal

        return forceTotal

    def translateToVector(self):
        """
        Take the random points, and turn them into vectors to the test charge.


        :return:
        5 random Points translated to vector points.
        """
