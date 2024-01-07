from tkinter import *


def mile_kilo_conversion():
    mile = mile_input.get()
    kilo = int(mile) * 1.609
    kilo_input.config(text=f"{kilo}")


window = Tk()
window.title("Mile to Km Convertor")
window.config(padx=30, pady=30)

# MILES INPUT
mile_input = Entry(width=5)
mile_input.grid(column=1, row=0)
mile_input.insert(END, string="0")

# MILES LABEL
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# is equal to
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# KILOMETER 
kilo_input = Label(text="0")
kilo_input.grid(column=1, row=1)

# KILO LABEL
kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

# Calculate button
cal_button = Button(text='Calculate', command=mile_kilo_conversion)
cal_button.grid(column=1, row=2)

window.mainloop()
