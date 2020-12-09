#creates calendar
from tkinter import *
root = Tk()
#places O or X on square 
def button_click(number):   
    currentDoor = doors[int(number-1)]
    if currentDoor['text'] == "X": 
        currentDoor.config(text=str(number), bg = "Blue") 
    else:
        currentDoor.config(text="X", bg = "Red")
 
doors = []
for j in range(6,31,6):
    for i in range(1,7):
        number = j-6+i    
        doors.append(Button(root,text=str(number),padx=1,pady=1, width=5,height=2,font=("Courier", 20) ))
        doors[int(number-1)].config(command=lambda number=number: button_click(number))
        doors[int(number-1)].grid(row=int(j/6),column=i)
         
root.mainloop()
