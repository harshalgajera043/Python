# import tkinter
#
# window = tkinter.Tk()
# window.title('my first GUI program')
# window.minsize(width=500, height=300)
#
# # label
#
# label = tkinter.Label(text="I am a label", font=("Arial", 20, "bold"))
# label.pack()
#
#
#
# window.mainloop()

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



