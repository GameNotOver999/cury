from lib2to3.pytree import convert
from tkinter import *

from tkinter.colorchooser import askcolor
from PIL import Image
from PIL import EpsImagePlugin


import math
EpsImagePlugin.gs_windows_binary =  r"C:\Program Files\gs\gs9.53.3\bin\gswin64c"

class begin():
    window = Tk()
    window.config(bg="gray")
    width = 0
    height = 0

    def __init__(self):

        self.widthe = Entry(self.window, text="width", width=4)
        #self.widthe.pack()
        self.widthe.grid(row=0, column=1)

        self.widthl = Label(self.window, text="width")
        # self.widthe.pack()
        self.widthl.grid(row=0, column=0)

        self.heighte = Entry(self.window, text="height", width=4)
        #self.heighte.pack()
        self.heighte.grid(row=0, column=3)

        self.heightl = Label(self.window, text="height")
        # self.heighte.pack()
        self.heightl.grid(row=0, column=2)

        self.new = Button(self.window, text="newfile", command=self.newfile)
        self.new.grid(row=0, column=4)
        #new.pack()

        self.window.mainloop()

    def newfile(self):

        self.width = self.widthe.get()
        self.height = self.heighte.get()

        newf = main(self.height, self.width)





class main():


    def __init__(self, height, width):

        self.choises = ["pen", "square", "oval", "line", "polygon", "gum"]
        self.color = "black"

        self.namec = StringVar(begin.window)
        self.namec.set("pen")



        #self.pensize.pack()

        self.choosecolorb = Button(begin.window, text="choosecolor", command=self.choosecolor)
        self.choosecolorb.grid(row=0, column=5)
        #self.choosecolorb.pack()

        self.filenamw = Label(begin.window, text="name")
        self.filenamw.grid(row=0, column=6)
        # self.filenamw.pack()

        self.filenaml = Entry(begin.window, text="untitled", width=20)
        self.filenaml.grid(row=0, column=7)
        #self.filenamw.pack()


        self.render = Button(begin.window, text="render", command=self.saveimage)
        self.render.grid(row=0, column=8)
        #self.render.pack()

        self.pens = OptionMenu(begin.window, self.namec, *self.choises)

        self.pens.grid(row=0, column=9)

        self.pensize = Scale(begin.window, from_=1.0, to=100.0, orient=HORIZONTAL)
        self.pensize.grid(row=0, column=10)

        self.c = Canvas(begin.window, width=width, height=height, bg="white")
        self.c.grid(row=1, columnspan=14)

        #self.c.pack()
        self.setup()
        self.c.mainloop()
        self.penss()

    def saveimage(self):


        self.filename = self.filenaml.get()

        self.c.postscript(file=self.filename + ".eps", colormode='color')
        self.image_eps = self.filename + ".eps"
        self.im = Image.open(self.image_eps)
        self.fig = self.im.convert('RGBA')
        self.image_png = self.filename + ".png"
        self.fig.save(self.image_png)

    def choosecolor(self):

        self.color = askcolor(color=self.color)[1]


    # drawing
    def draw(self, event):
        self.penss()


        #self.thick = (20 - math.sqrt((self.oldx - event.x)**2 + (self.oldy - event.y)**2) / ((self.height + self.width) / 2) * 3) + self.pensize.get() - 10
        if self.pen == True:
            self.thick = self.pensize.get()

            self.c.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=self.thick,
                               capstyle=ROUND)
            self.oldx = event.x
            self.oldy = event.y
        elif self.squere == True:

            self.c.delete(self.presquer)
            self.presquer = self.c.create_rectangle(self.oldx, self.oldy, event.x, event.y, fill=self.color, outline=self.color)
        elif self.oval == True:
            self.c.delete(self.prescircle)
            self.prescircle = self.c.create_oval(self.oldx, self.oldy, event.x, event.y, fill=self.color,
                                                    outline=self.color)
        elif self.line == True:
            self.c.delete(self.preline)
            self.preline = self.c.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=self.thick,
                               capstyle=ROUND)
        elif self.polygon == True:
            self.c.delete(self.prepol)
            self.prepol = self.c.create_polygon(self.oldx, self.oldy,
                                                     event.x, event.y, self.oldx, event.y, fill=self.color, outline=self.color)







    def reset(self, event):

        self.oldx = event.x
        self.oldy = event.y

    def rforf(self, event):

        if self.squere == True:
            self.c.create_rectangle(self.oldx, self.oldy, event.x, event.y, fill=self.color, outline=self.color)

        elif self.oval == True:
            self.c.create_oval(self.oldx, self.oldy, event.x, event.y, fill=self.color, outline=self.color)

        elif self.line == True:
            self.c.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=self.thick,
                               capstyle=ROUND)

        elif self.polygon == True:
            self.c.create_polygon(self.oldx, self.oldy,
                                  event.x, event.y, self.oldx, event.y, fill=self.color, outline=self.color)






    def setup(self):
        self.c.bind("<Button-1>", self.reset)
        self.c.bind("<B1-Motion>", self.draw)
        self.c.bind("<ButtonRelease-1>", self.rforf)

        self.oldx = 0
        self.oldy = 0

        self.filename = "drawing"
        self.thick = 5
        self.squere = False
        self.oval = False
        self.pen = True
        self.line = False
        self.polygon = False

        self.presquer = self.c.create_rectangle(0, 0, 0, 0)
        self.prescircle = self.c.create_oval(0, 0, 0, 0)
        self.preline = self.c.create_line(0, 0, 0, 0, width=0)
        self.prepol = self.c.create_polygon(0, 0, 0, 0, 0, 0)

    def penss(self):

        if self.namec.get() == "pen":
            self.pen = True
            self.squere = False
            self.oval = False
            self.line = False
            self.polygon = False

        elif self.namec.get() == "square":
            self.squere = True
            print(self.squere)
            self.oval = False
            self.pen = False
            self.line = False
            self.polygon = False

        elif self.namec.get() == "oval":
            self.oval = True
            self.pen = False
            self.squere = False
            self.line = False
            self.polygon = False

        elif self.namec.get() == "line":
            self.oval = False
            self.pen = False
            self.squere = False
            self.line = True
            self.polygon = False

        elif self.namec.get() == "polygon":
            self.oval = False
            self.pen = False
            self.squere = False
            self.line = False
            self.polygon = True

        elif self.namec.get() == "gum":
            self.oval = False
            self.pen = True
            self.squere = False
            self.line = False
            self.polygon = False
            self.color = "white"




if __name__ == '__main__':
    begin()
