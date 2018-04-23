import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
from PIL import Image, ImageTk
import os
import random
#import rcCar #test this out with X11 forwarding

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

# stuff for the PRM graph
f = Figure(figsize = (5,5), dpi = 100)
a = f.add_subplot(111)


#stuff for the path graph
p = Figure(figsize = (5,5), dpi = 100)
b = p.add_subplot(111)

#arrays to use for graphing later
#speed arrays
motor1 = []
motor2 = []
#direction arrays
directM1 = []
directM2 = []

#gets data from the data.txt file to graph the speed info
def getData():
    #if os.path.isfile('data.txt'):
    pullData = open('data.txt')
    text = pullData.read()
    dataArr = text.split('\n')

    for line in dataArr:
        print("line", line)
        if(line != ''):#make sure its not the end of file
            m1,m2,dm1,dm2 = line.split(',')
            print(type(m1), m2, dm1, dm2)
        motor1.append(int(float(m1)))
        motor2.append(int(float(m2)))
        directM1.append(dm1)
        directM2.append(dm2)

    #else:
        #print("file is empty")

def rpmAnimate():
    getData()
    #graph of rpm for each wheels
    i = 0
    xList = []

    while i < len(motor1):
        xList.append(i)
        i+= 1

    a.clear()
    a.plot(xList, motor1)
    a.plot(xList, motor2)


def pathAnimate():
    #getData()
    i = 0
    #these keep track of the directions of the car to make graphing easier
    prevDirection = "east"
    direction = "east"

    #line graph of path
    xList = []
    yList = []
    '''
    directions for graphing:
        north: x, y+1           straight up
        northeast: x + 1, y + 1
        east: x + 1, y          going right
        southeast: x+1, y- 1
        south: x, y-1           straight down
        southwest: x-1, y-1
        west: x - 1, y          going left
        northwest: x - 1, y + 1
    '''

    while(i < len(motor1)):

        if(i == 0):#base case
            xList.append(5)
            yList.append(5)
            direction = "east"

        #print(xList[i])
        #print(yList[i])
        print("i : ", i)
        print("motor length: ", len(motor1))
        print("xList length: ", len(xList))
        print("motor1[i]", motor1[i])
        print("motor1[i]", motor2[i])
        #set conditions for changing directions
        if(motor1[i] == 0 or motor2[i] == 0):# motors are stopped. append current position
            xList.append(xList[i - 1])
            yList.append(yList[i - 1])

        if(directM1[i] == 'F' and directM2[i] == 'F'):#both motors go forwards
            #both speeds are equal: no change in direction
            if(motor1[i] == motor2[i]):
                if(prevDirection == "north"):
                    direction = "north"
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "northeast"):
                    direction = "northeast"
                    xList.append(xList[i - 1] + 1)
                    yList.append(yList[i - 1] + 1)

                if(prevDirection == "east"):
                    direction = "east"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1])

                if(prevDirection == "southeast"):
                    direction = "southeast"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "south"):
                    direction = "south"
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "southwest"):
                    direction = "southwest"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "west"):
                    direction = "west"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1])

                if(prevDirection == "northwest"):
                    direction = "northwest"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] + 1)

            #if speed of m1 > m2 : change direction clockwise
            if(motor1[i] > motor2[i]):
                if(prevDirection == "north"):
                    direction = "northeast"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "northeast"):
                    direction = "east"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1])

                if(prevDirection == "east"):
                    direction = "southeast"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "southeast"):
                    direction = "south"
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "south"):
                    direction = "southwest"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "southwest"):
                    direction = "west"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1])

                if(prevDirection == "west"):
                    direction = "northwest"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "northwest"):
                    direction = "north"
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] + 1)

            #if speed of m1 < m2 : change direction counterclockwise
            if(motor1[i] < motor2[i]):
                if(prevDirection == "north"):
                    direction = "northwest"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "northwest"):
                    direction = "west"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1])

                if(prevDirection == "west"):
                    direction = "southwest"
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "southwest"):
                    direction = "south"
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "south"):
                    direction = "southeast"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "southeast"):
                    direction = "east"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1])

                if(prevDirection == "east"):
                    direction = "northeast"
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "northeast"):
                    direction = "north"
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] + 1)

        if(directM1[i] == 'B' and directM2[i] == 'B'): # both motors go backwards;
            #need to graph the opposite direction
            #if both speeds are equal: no change in direction
            if(motor1[i] == motor2[i]):
                if(prevDirection == "north"):
                    direction = "north"
                    #move south
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "northeast"):
                    direction = "northeast"
                    #move southwest
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "east"):
                    direction = "east"
                    #move west
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1])

                if(prevDirection == "southeast"):
                    direction = "southeast"
                    #move northwest
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "south"):
                    direction = "south"
                    #move north
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "southwest"):
                    direction = "southwest"
                    #move northeast
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "west"):
                    direction = "west"
                    #east
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1])

                if(prevDirection == "northwest"):
                    direction = "northwest"
                    #move southeast
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] - 1)

            #if speed of m1 > m2 : change direction counterclockwise move oppostie of new direction
            if(motor1[i] > motor2[i]):
                if(prevDirection == "north"):
                    direction = "northwest"
                    #move southeast
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "northwest"):
                    direction = "west"
                    #east
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1])

                if(prevDirection == "west"):
                    direction = "southwest"
                    #move northeast
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "southwest"):
                    direction = "south"
                    #move north
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "south"):
                    direction = "southeast"
                    #move northwest
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "southeast"):
                    direction = "east"
                    #move west
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1])

                if(prevDirection == "east"):
                    direction = "northeast"
                    #move southwest
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "northeast"):
                    direction = "north"
                    #move south
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] - 1)

            #if speed of m1 < m2 : change direction clockwise; move in opposite of new direction
            if(motor1[i] < motor2[i]):

                if(prevDirection == "north"):
                    direction = "northeast"
                    #move southwest
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "northeast"):
                    direction = "east"
                    #move west
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1])

                if(prevDirection == "east"):
                    direction = "southeast"
                    #move northwest
                    xList.append(xList[i-1] - 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "southeast"):
                    direction = "south"
                    #move north
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "south"):
                    direction = "southwest"
                    #move northeast
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] + 1)

                if(prevDirection == "southwest"):
                    direction = "west"
                    #east
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1])

                if(prevDirection == "west"):
                    direction = "northwest"
                    #move southeast
                    xList.append(xList[i-1] + 1)
                    yList.append(yList[i-1] - 1)

                if(prevDirection == "northwest"):
                    direction = "north"
                    #move south
                    xList.append(xList[i-1])
                    yList.append(yList[i-1] - 1)

        if(directM1[i] == 'B' and directM2[i] == 'F'): # change counterclockwise but dont move
            # since this is a spin counterclockwise
            if(prevDirection == "north"):
                direction = "northwest"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "northwest"):
                direction = "west"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "west"):
                direction = "southwest"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "southwest"):
                direction = "south"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "south"):
                direction = "southeast"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "southeast"):
                direction = "east"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "east"):
                direction = "northeast"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "northeast"):
                direction = "north"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

        if(directM1[i] == 'F' and directM2[i] == 'B'): # change counterclockwise but dont move
            # since this is a spin clockwise
            if(prevDirection == "north"):
                direction = "northeast"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "northeast"):
                direction = "east"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "east"):
                direction = "southeast"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "southeast"):
                direction = "south"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "south"):
                direction = "southwest"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "southwest"):
                direction = "west"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "west"):
                direction = "northwest"
                xList.append(xList[i-1])
                yList.append(yList[i-1])

            if(prevDirection == "northwest"):
                direction = "north"
                xList.append(xList[i-1])
                yList.append(yList[i-1])
        #setup directions for next iteration
        prevDirection = direction
        i += 1

    b.clear()
    b.plot(xList, yList)


class Application(tk.Frame):

    #basic attributes of the car as well as export settings
    carName = 'Group_F9.csv'
    colorScheme = 'boring AF'
    exportPath = os.getcwd()
    exportName = carName

    #main method; initialize the main window
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.minsize(500, 600)
        self.grid()
        self.createWidgets()

    #set up the buttons
    def createWidgets(self):
        #buttons and button frame
        self.buttonFrame = tk.Frame(self, width = 200, height = 100, background = 'blue2')
        self.buttonFrame.grid(row = 0, column = 0, sticky = 'W')
        self.quitButton = tk.Button(self.buttonFrame, text='Quit',command=self.quit)
        self.settingsButton = tk.Button(self.buttonFrame, text = 'Controls', command = self.settingsWindow)

        self.quitButton.grid(row = 0, column = 0)
        self.settingsButton.grid(row = 0, column = 1)

        #images in frames. path and rpmGraph will be replaced with realtime graphs

        self.pathFrame = tk.Frame(self, width = 600, height = 300)
        self.pathFrame.grid(row = 1, column = 1, sticky = 'E')

        self.pathLabel = tk.Label(self.pathFrame, text = "Path Graph")
        self.pathLabel.pack(pady = 10, padx = 10)

        canvasP = FigureCanvasTkAgg(p, self.pathFrame)
        canvasP.show()
        canvasP.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2TkAgg(canvasP, self.pathFrame)
        toolbar.update()
        canvasP._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.rpmFrame = tk.Frame(self, width = 300, height = 300)
        self.rpmFrame.grid(row = 1, column = 0, sticky = 'W')


        self.rpmLabel = tk.Label(self.rpmFrame, text = "RPM Graph")
        self.rpmLabel.pack(pady = 10, padx = 10)
        canvas = FigureCanvasTkAgg(f, self.rpmFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2TkAgg(canvas, self.rpmFrame)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    #settings window to change carName and colorScheme
    def settingsWindow(self):
        newWindow = tk.Toplevel(self)
        newWindow.title('Controls')

        self.controlFrame = tk.Frame(newWindow, width = 600, height = 300)
        self.controlFrame.grid(row = 2, column = 0, sticky = 's')

        imagec = ImageTk.PhotoImage(Image.open('GUIControls.gif')) #resize
        self.controlImg = tk.Label(self.controlFrame, image = imagec)
        self.controlImg.photo = imagec
        self.controlImg.grid(row = 0, column = 0, rowspan = 10, columnspan = 10)



app = Application()
app.master.title('Cat\'s Conundrum')
anir = animation.FuncAnimation(f, rpmAnimate(), interval=1000)
anip = animation.FuncAnimation(p, pathAnimate(), interval=1000)
app.mainloop()
