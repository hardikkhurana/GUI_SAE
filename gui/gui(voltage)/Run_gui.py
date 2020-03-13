#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import random
import gaugelib


win = tk.Tk()
a5 = PhotoImage(file="logo.png")
a6 = PhotoImage(file="logo1.png")
win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("GUI_E_JATAYU")
win.geometry("800x400+0+0")
#win.resizable(width=True, height=True)
win.configure(bg="black")

g_value=0
x=0

def read_every_second():
    global x
#battery temp
    g1_value=3
    p1.set_value(int(g1_value))
#motor temp
    g2_value=10
    p2.set_value(int(g2_value))
#speed
    g3_value=50
    p3.set_value(int(g3_value))
#battery percentage
    g4_value=random.randint(0,100)
    p4.set_value(int(g4_value))
#voltage
    g5_value = random.randint(0, 100)
    p5.set_value(int(g5_value))
    x+=1
    if x>100:
#        graph1.draw_axes()
        x=0
    win.after(100, read_every_second)

p1 = gaugelib.DrawGauge2(
    win,
    max_value=100.0,
    min_value=0.0,
    size=200,
    bg_col='black',
    unit = "Battery Temp. °C",bg_sel = 2)
#p1.pack(side=LEFT)
#p1.place(x=5,y=5,width=50,height=50)
p2 = gaugelib.DrawGauge2(
    win,
    max_value=100.0,
    min_value= 0.0,
    size=200,
    bg_col='black',
    unit = "Motor Temp. °C",bg_sel = 2)
#p2.pack(side=RIGHT)

p3 = gaugelib.DrawGauge3(
    win,
    max_value=60.0,
    min_value= 0.0,
    size=400,
    bg_col='black',
    unit = "Speed km/h",bg_sel = 1)
#p3.pack()
p4 = gaugelib.DrawGauge3(
    win,
    max_value=100.0,
    min_value= 0.0,
    size=200,
    bg_col='black',
    unit = "Battery %",bg_sel = 2)
#p4.pack()

p5 = gaugelib.DrawGauge44(
    win,
    max_value=100.0,
    min_value= 0.0,
    size=200,
    bg_col='black',
    unit = "voltage",bg_sel = 2)
p5.pack(side=RIGHT)
l22 = Label(height=2,width=20,fg="white",bg="black", text="E-JATAYU")
#l22.pack(side=RIGHT and BOTTOM)
l23  = Label( image=a6)
#l23.pack(side=LEFT and BOTTOM)
read_every_second()

mainloop()