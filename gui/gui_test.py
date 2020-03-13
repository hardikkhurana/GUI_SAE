from tkinter import *
import math
import random
root = Tk()  # creating window
root.resizable(height=None, width=None)
root.config(background="black")
global c
c=Canvas(root,height=900,width=1500,bg="black")
print (1)
c.pack()
class Update:
    def main(self):
        self.bat_calc=random.randint(150,650)
        self.rect = c.create_rectangle(120, self.bat_calc, 170, 650, fill'"white")                           
        c.after(100,self.main)
    
print (1)
U=Update()
U.main()
mainloop()
