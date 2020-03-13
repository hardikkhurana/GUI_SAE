from tkinter import *
import math
import random

root = Tk()  # creating window
root.resizable(height=None, width=None)
root.config(background="black")

x1y1 = 200, 100, 800, 700
x2y2 = 220, 120, 780, 680
l1 = 0
l2 = 0
gap_angle = 223
gap_angle_1 = 180

global c

c = Canvas(root, height=900, width=1500, bg="black")

# speedometer
oval0 = c.create_oval(195, 95, 805, 705, fill="white", outline="")
oval1 = c.create_oval(200, 100, 800, 700, fill="black", outline="")
arc0 = c.create_arc(x1y1, start=315, extent=270, fill="black", outline="")
while l1 < 7:
    arc1 = c.create_arc(x1y1, start=gap_angle, extent=2, fill="white", outline="")
    l1 = l1 + 1
    gap_angle = gap_angle - 45

arc2 = c.create_arc(x2y2, start=313, extent=273, fill="black", outline="")  # fill colour back 0angle to 228degrees
# arc3 = c.create_arc(x2y2, start=310, extent=90, fill="gray26", outline="")  # fill colour back 315angle to 0degrees
oval3 = c.create_oval(485, 385, 515, 415, fill="white", outline="")

SPEED = c.create_text(680, 580, fill="white", font="arial 20", text=60)
SPEED1 = c.create_text(320, 580, fill="white", font="arial 20", text=0)
SPEED = c.create_text(505, 140, fill="white", font="arial 20", text=30)
SPEED = c.create_text(240, 395, fill="white", font="arial 20", text=10)
SPEED = c.create_text(760, 405, fill="white", font="arial 20", text=50)
SPEED = c.create_text(685, 220, fill="white", font="arial 20", text=40)
SPEED = c.create_text(320, 220, fill="white", font="arial 20", text=20)

# temp motor and battery
x3y3 = 850, 100, 1250, 500
x4y4 = 850, 400, 1250, 800
x5y5 = 845, 95, 1255, 500
x6y6 = 845, 395, 1255, 800
x7y7 = 870, 120, 1230, 480
x8y8 = 865, 420, 1230, 780

arc5 = c.create_arc(x5y5, start=359, extent=40, fill="white", outline="")
arc5_1 = c.create_arc(x5y5, start=38, extent=74, fill="white", outline="")
arc5_2 = c.create_arc(x5y5, start=74, extent=109, fill="white", outline="")

arc6 = c.create_arc(x6y6, start=359, extent=40, fill="white", outline="")
arc6_1 = c.create_arc(x6y6, start=38, extent=74, fill="white", outline="")
arc6_2 = c.create_arc(x6y6, start=74, extent=109, fill="white", outline="")

arc3 = c.create_arc(x3y3, start=0, extent=180, fill="black", outline="")
arc4 = c.create_arc(x4y4, start=0, extent=180, fill="black", outline="")

while l2 < 11:
    if l2 > 7:
        fill3 = "white"
    elif l2 > 5 and l2 < 8:
        fill3 = "white"
    else:
        fill3 = "white"
    arc7 = c.create_arc(x3y3, start=gap_angle_1, extent=2, fill=fill3, outline="")
    arc8 = c.create_arc(x4y4, start=gap_angle_1, extent=2, fill=fill3, outline="")
    l2 = l2 + 1
    gap_angle_1 = gap_angle_1 - 18

arc9 = c.create_arc(x7y7, start=0, extent=183, fill="black", outline="")
arc10 = c.create_arc(x8y8, start=0, extent=183, fill="black", outline="")

oval_battery = c.create_oval(1040, 290, 1060, 310, fill="white", outline="")
oval_motor = c.create_oval(1040, 590, 1060, 610, fill="white", outline="")

# battery percentage
rect3 = c.create_rectangle(115, 145, 175, 655, fill="white")
rect4 = c.create_rectangle(120, 150, 170, 650, fill="black")

# math bs and working needle
# speedometer
unit = c.create_text(500, 640, fill="white", font="Times 10 italic bold", text="km/h")
#name_battery = c.create_text(500, 640, fill="white", font="Times 10 italic bold", text="km/h")
#name-battery = c.create_text(500, 640, fill="white", font="Times 10 italic bold", text="km/h")


q=1
c.pack()
# fuck with math is a fuction which shows the speed
l = 200  # length of needle in pixels of spedd

global speed
global battery_percentage_real
global temp_value_battery
global temp_value_motor

speed = float()
battery_percentage_real = float()
temp_value_battery = float()
temp_value_motor = float()
class Update:
    def __init__(self):
        self.l_temp = 115
        self.l = 200  # length of needle in pixels of spedd

    def fuck_with_math(self):
        speed=random.randint(10, 50)
        print (speed)
        self.printspeed=speed
        self.angle_used = speed * 4.5
        self.angle_rad = math.radians(self.angle_used - 225)
        self.p = math.sin(self.angle_rad) * self.l
        self.b = math.cos(self.angle_rad) * self.l
        self.center_x = 500
        self.center_y = 400
        self.bc = self.b + self.center_x
        self.pc = self.p + self.center_y



    def fuck_with_battery_percentage(self):
        # define here bitch
        battery_percentage_real=random.randint(10,50)
        self.battery_percentage = 100 - battery_percentage_real
        self.bat_calc = ((500 / 100) * self.battery_percentage) + 150


    def fuck_with_battery_temp(self):
        temp_value_battery=random.randint(10, 50)
        self.angle_used_temp_battery = temp_value_battery * 1.8
        self.angle_used_temp_battery_radian = math.radians(self.angle_used_temp_battery - 180)
        self.p_battery = math.sin(self.angle_used_temp_battery_radian) * self.l_temp
        self.b_battery = math.cos(self.angle_used_temp_battery_radian) * self.l_temp
        self.center_x_battery = 1050
        self.center_y_battery = 300
        self.bc_battery = self.b_battery + self.center_x_battery
        self.pc_battery = self.p_battery + self.center_y_battery


    def fuck_with_motor_temp(self):
        temp_value_motor=random.randint(10, 50)
        self.angle_used_temp_motor = temp_value_motor * 1.8
        self.angle_used_temp_motor_radian = math.radians(self.angle_used_temp_motor - 180)
        self.p_battery = math.sin(self.angle_used_temp_motor_radian) * self.l_temp
        self.b_battery = math.cos(self.angle_used_temp_motor_radian) * self.l_temp
        self.center_x_motor = 1050
        self.center_y_motor = 600
        self.bc_motor = self.b_battery + self.center_x_motor
        self.pc_motor = self.p_battery + self.center_y_motor

    def creating_object(self):
        self.outputrectangle=self.c.create_rectangle(120, 150, 170, 650, fill="black")


    def updating(self):
        U.creating_object
        c.after(1000, self.updating)

U=Update()
U.updating()

mainloop()