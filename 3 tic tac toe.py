#creates naughts and crosses
from tkinter import *
root = Tk()
#places O or X on square 
def button_click(number):
    global move
    move = move + 1 
    currentDoor = doors[int(number-1)]
    if currentDoor['text'] == "-": #only play if square unused
        if move%2 == 0: #toggle between O & X move
            currentDoor.config(text="X", bg = "Red") #mark the square with move
        else:
            currentDoor.config(text="O", bg = "Green") #mark the square with move
        
        checkWin()
 
def checkWin():
    #column check
    for c in range (0,3):    
        check3(c,c+3,c+6)
     #row check
    for r in range (0,7,3):    
        check3(r,r+1,r+2)
    #diagonal check   
    check3(0,4,8)
    check3(2,4,6)
        
def check3(sq1,sq2,sq3):
    if doors[sq1]['text'] == doors[sq2]['text'] and doors[sq2]['text'] == doors[sq3]['text'] and doors[sq1]['text'] !="-":
        doors[sq1].config(bg="Blue",text="win!")
        doors[sq2].config(bg="Blue",text="win!")
        doors[sq3].config(bg="Blue",text="win!")
 
move = 0  
doors = []
for j in range(3,10,3):
    for i in range(1,4):
        number = j-3+i
        doors.append(Button(root,text="-",padx=1,pady=1, width=6,height=3,font=("Courier", 44) ))
        doors[int(number-1)].config(command=lambda number=number: button_click(number))
        doors[int(number-1)].grid(row=int(j/3),column=i,columnspan=1)
          
root.mainloop()
