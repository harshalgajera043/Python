from tkinter import *

display = Tk()
display.minsize(width=200, height=100)
display.title("Mile to Km Converter")
display.config(padx=10, pady=10)


def convert_mile_to_km():
    km_distance = float(distance_input.get()) * 1.609
    km_label.config(text=f"{round(km_distance,2)}")


distance_input = Entry(width=10)
# distance_input.insert(index=0, string="enter covered distance in miles")
mile_distance = distance_input.get()
# print(mile_distance)
distance_input.focus()
distance_input.grid(column=1, row=1)

miles_lable = Label(text="Miles")
miles_lable.grid(column=2, row=1)

# using button class to create a convert button which will convert mile to  km after press
convert = Button(command=convert_mile_to_km)
convert.config(text="Calculate")
convert.grid(column=1, row=3)

# display km distance label  below convert button
km_label = Label(text="0")
km_label.grid(column=1, row=2)

k_lable = Label(text="Km")
k_lable.grid(column=2, row=2)

# display texts
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=2)


display.mainloop()