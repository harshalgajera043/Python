import tkinter

window = tkinter.Tk()
window.title('my first GUI program')
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# label
label = tkinter.Label(text="I am a label", font=("Arial", 20, "bold"))
# label["text"] = "I am Harshal"
label.config(text="Write texts")
label.grid(column=3, row=2)
label.config(pady=10, padx=10)


def button_clicked():
    label.config(text=input.get())


def button_clicked_1():
    label.config(text=f"Hello {input.get()}")


# Button
my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(column=0, row=0)
my_button.config(pady=10, padx=10)

New_button = tkinter.Button(text="press me", command=button_clicked_1)
New_button.grid(column=2, row=0)
New_button.config(pady=10, padx=10)


# input
input = tkinter.Entry(width=30)
input.insert(index=0, string="enter text here")
input.focus()
print(input.get())
input.grid(column=1, row=1)
# input.config(pady=10, padx=10)

# # Text
# text = tkinter.Text(height=5, width=25)
# # put cursor in box
# text.focus()
# text.insert(0, "enter the multi_line comment here.")
# print(text.get("1.0", 0))
# text.pack()


# spinbox
# def get_spinbox():
#     print(spinbox.get())
#
#
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=get_spinbox)
# spinbox.pack()
#
#
# # Scale
# def get_scale(value):
#     print(value)
#
#
# scale = tkinter.Scale(from_=0, to=10, width=10, length=50, command=get_scale)
# # value = scale.get()
# scale.pack()
#
#
# # checkbox
# def get_checkbutton():
#     print(checked_state.get())
#
#
# checked_state = tkinter.IntVar()
# checkbox_1 = tkinter.Checkbutton(text="Harshal",variable=checked_state,command=get_checkbutton)
# checkbox_1.pack()
# checkbox_2 = tkinter.Checkbutton(text="Pooja", variable=checked_state,command=get_checkbutton)
# checkbox_2.pack()
# checkbox_3 = tkinter.Checkbutton(text="Komal", variable=checked_state,command=get_checkbutton)
# checkbox_3.pack()
#
# # radio button
# def radio_button_on():
#     print(radio_on.get())
#
# radio_on = tkinter.IntVar()
# radio_button_1 = tkinter.Radiobutton(text="harshal", value=1, variable=radio_on, command=radio_button_on)
# radio_button_1.pack()
# radio_button_2 = tkinter.Radiobutton(text="pooja", value=2, variable=radio_on, command=radio_button_on)
# radio_button_2.pack()
#
#
# # listbox
# def get_box(event):
#     print(box.get(box.curselection()))
#
#
# box = tkinter.Listbox(height=4)
# fruits= ["apple", "barries", "banana", "walnuts"]
# for fruit in fruits:
#     box.insert(fruits.index(fruit), fruit)
# box.bind("<<ListboxSelect>>", get_box)
# box.pack()






# manu
# radio_button = tkinter.Radiobutton(text="harshal", value="harshal")
# radio_button.pack()





window.mainloop()

# functions with default values
# advanced python arguments
# def my_function(a=1, b=3, c=5):
#     d = a + b + c
#     return d
#
#
# print(my_function(a=12))

# def foo(a, b=6, c=4):
#     print(a, b, c)
# foo(1)

# # Unlimited number of arguments
# # Unlimited positional arguments
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return(total)
#
# print(add(1,2,3,4,5,6,7,8,9,10))

# def sum(a=1, b=3, **kwargs):
#     sum = a + b
#     for n in kwargs:
#         sum += n
#     return sum
# print(sum(1,2,3))
#
# def calculate(**kwargs):
#     print(kwargs["add"])
#
# calculate(add=5, sum=4)

# class MyCar:
#
#     def __init__(self, **kwargs):
#         self.move = kwargs.get("move")
#         self.mode = kwargs.get("mode")
#         self.speed = kwargs.get("speed")
#         self.time = kwargs.get("time")
#
#     def distance(self):
#         distance_cover = self.time * self.speed
#         return distance_cover
#
#
# car = MyCar(speed=40, time=40)
# print(car.distance())



