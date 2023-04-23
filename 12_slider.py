from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x200")
root.title("Slider Widget")
def salary():
    messagebox.showinfo("salary", f"You monthly salary is {myslider.get()} dollars")

l1=Label(root, text="Enter your salary(in dollars)")
l1.pack()
myslider=Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=20) #tickinterval--> used to specify the interval
myslider.set(20) #used to set the initial value of the scale
myslider.pack()
Button(root, text="Save",pady=10, command=salary).pack()
root.mainloop()