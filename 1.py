import tkinter
import PIL
from tkinter import *
from PIL import *



root=Tk()
root.minsize(width=500,height=500)
root.maxsize(width=500,height=500)
root.config(bg="white")

#give coustom button image path in file
image1=PhotoImage(file="button.png")
button=Button(root,image=image1,bg="#ffffff",border=0,activebackground="white")
button.place(x=50,y=50)


root.mainloop()
