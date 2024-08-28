from tkinter import *
window = Tk()
window.title("Mile to km converter!")
window.config(padx=20, pady=20)

def button_clicked():
    num_miles = float(miles.get())
    num_km = round(num_miles * 1.609, 2)
    km.config(text=f"{num_km}")


label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="Km")
label2.grid(column=2, row=1)
label3 = Label(text="is equal to")
label3.grid(column=0, row=1)

miles = Entry(width=10)
miles.grid(column=1, row=0)
km = Label(text=0)
km.grid(column=1, row=1)

calc = Button(text="Calculate", command=button_clicked)
calc.grid(column=1, row=2)

window.mainloop()


