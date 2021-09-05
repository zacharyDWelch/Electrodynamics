from tkinter import *
import math as m

"""
*************** Things to think about *************************

At some point get the circle to be randomly be placed in the grid.

TODO: 

"""

class Drawing:

    def __init__(self):
        self.master = Tk()
        self.master.title("Drawing of Circle and Charge Points")
        self.master.minsize(300,300)
        self.master.maxsize(1000,1000)


        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 800

        self.my_canvas = Canvas(self.master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
        self.my_canvas.pack()

        self.resetChargePoints = Button(self.master, text="Re-Set", command=self.testButton)
        self.resetChargePoints.pack(pady=20)

        # Drawing on the window
        self.creatGrid()
        #self.addText()
        self.drawCircle() # Main circle
        self.drawChargePoints() # Small red circles for charge points
        self.drawTestPoint() # Small blue circle for test point

        # main loop to keep window open.
        self.master.mainloop()


    def testButton(self):
        print("Button clicked")

    def creatGrid(self):
        """
        Draws the axis lines (fixed location)
        """
        # Create Line             (x1, y1, x2, y2)
        self.my_canvas.create_line(10, 10, 10, 800, fill="black", arrow=FIRST) # Y-Axis
        self.my_canvas.create_line(10, 800, 900, 800, fill="black", arrow=LAST) # X-Axis

        x_axisText = Label(self.master, text="x")
        x_axisText.place(x=900, y=800)

        y_axisText = Label(self.master, text="y")
        y_axisText.place(x=15, y=5)


    def addText(self):
     """
     Adds any needed text to window
     """

    def setCircleCoords(self, point):
        x1, y1 = 50, 650
        x2, y2 = 150, 750

        if(point == 'x1'):
            return x1

        if(point == 'y1'):
            return y1

        if(point == 'x2'):
            return x2

        if(point == 'y2'):
            return y2

    def drawCircle(self):
        """
        Draws circle is in a fixed location.
        # oval (x1, y1, x2, y2)
        # x1, y1 : Top left of oval
        # x1, y2 : Bottom right of oval
        """
        self.my_canvas.create_oval(
            self.setCircleCoords('x1'),
            self.setCircleCoords('y1'),
            self.setCircleCoords('x2'),
            self.setCircleCoords('y2'))

    def getChargePoints(self, xPos, yPos):
        """
        Gets the charge points from CircleProblem

        :See CircleProblem:
        :param xPos: X coordnate of charge point
        :param yPos: Y coordnate of charge point
        :return: The location of each charge point
        """
        x = xPos
        y = yPos

        def checkChargePoints(xPos,yPos):
            """
            Check to see if the charge points are on the circle, by taking
            points form setCircleCoords() and comparing them to the points
            set up already.

            To check if points are on circle
                set up loop to go through points to check if they are on
                the circle or not.

            Equation for circle: (x-h)^2 + (y-k)^2 = r^2

            tkinter makes a square at the top left of the coordinates
            and constructs a circle inside the square.

            :return:
            x,y points: if the points are on the circle
            print don look good: if points are not on the circle
            """

            check = False

            x = xPos # x coordinate
            y = yPos # y coordinate
            h = 1/2 * x # center x coordinate
            k = 1/2 * y # center y coordinate
            r = m.sqrt((x-h)**2 + (y-k)**2)


            if(x == 0):
                check = True

            return check

        if(checkChargePoints(xPos, yPos) == True):
            print("Check Pass")
            return x , y
        else:
            print("Check Fail")

    def drawChargePoints(self):
        """
        Draws the Charge Point at coordinates from getChargePoints
        Points drawn are small filled ovals

        ToDo: set points based on getChargePoint()

        :return: Draws points at the location of the Charge Points

        """

        # points to draw
        x1,y1 = 100, 100
        x2,y2 = x1 + 5 , y1 + 5

        # Test points for charge
        self.my_canvas.create_oval(x1,y1,x2,y2, fill="red")
        self.my_canvas.create_oval(47, 700, 52, 705, fill="red") # Take x1, y1 (spot on circle)
                                                                 # and add 5 to it for x2,y2.


    def getTestPoint(self):
        """
        Gets the Test points from the CircleProblem class

        :return: Test point
        """

    def drawTestPoint(self):
        """
        Draws the test point given coordinates from getTestPoint
        Points are small ovals

        :return: Draws small oval for test point.
        """
        self.my_canvas.create_oval(300, 300, 305, 305, fill="blue")

display = Drawing() # display whats on the screen (main loop)
