from tkinter import *
 
root = Tk()
 
e = Entry(root, width=15, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=1,padx=10,pady=10)
 
dollar = Label(root, font=("Courier", 44),text="$")
dollar.grid(row=0,column=0)
 
f = Label(root, width=15, borderwidth=15,font=("Courier", 44))
f.grid(row=1,column=1,padx=10,pady=10)
 
def button_click():
   
    value = int(e.get())
    e.delete(0,END)
    f.config(text="£"+str(value*0.8))
    
button_equal = Button(root,text="=",padx=100,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=1)
root.mainloop()
