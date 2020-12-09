from tkinter import *
 
root = Tk()
root.title("Prime number checker")
 
title1 = Label(root, width=25, borderwidth=5,text="Prime number checker",font=("Courier", 44))
title1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 
numberEntry = Entry(root, width=25, borderwidth=5,font=("Courier", 44))
numberEntry.grid(row=1,column=1,columnspan=1,padx=10,pady=10)
 
answer = Label(root, width=25, borderwidth=5,font=("Courier", 44))
answer.grid(row=2,column=1,columnspan=1,padx=10,pady=10)
 
answer2 = Label(root, width=25, borderwidth=5,font=("Courier", 44))
answer2.grid(row=3,column=1,columnspan=1,padx=10,pady=10)
 
def button_click(): 
    num =  int(numberEntry.get()) 
    for i in range(2,num):
        if (num % i) == 0:
           answer.config(text=str(num)+" is not prime")
           answer2.config(text=str(str(i)+" times "+str(num//i)+" is "+str(num)))
           break
        else:
            answer.config(text=str(num)+" is prime")
 
 
button_equal = Button(root,text="CHECK",padx=20,pady=20,command=lambda: button_click(), bg="Red")
button_equal.grid(row=4,column=0,columnspan=3)
  
root.mainloop()
