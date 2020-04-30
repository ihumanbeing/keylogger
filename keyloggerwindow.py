#CREATED BY @anactualhuman_
#please for the love of all that is good dont use this to actually steal passwords
#just use it as a funny prank or some shit


from tkinter import *


root = Tk()
root.title("Keylogger")
root.resizable(0,0)
root.geometry("130x100")
root.configure(bg="#171717")
esca = IntVar()

def begin():
    root.destroy()
    import keyloggertask
    #execfile('keyloggertask.py')



var = StringVar(root, "Simple Keylogger\nby @anactualhuman_\nESC To cancel operation")
title = Label(root, bd=0, fg="white", bg="#0a0a0a", textvariable = str(var), relief = FLAT).grid(row=0, column=0)

#escapebtn = Checkbutton(root, bd=1, padx=30, pady=30, text="Esc to cancel operation", variable=esca).grid(row=2,column=2,columnspan=1)
runbtn = Button(root, bd=0, fg="white", bg="#0a0a0a", pady=10, padx=10, text="Run", command=begin).grid(row=2,column=0)


root.mainloop()