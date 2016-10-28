from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text='Click Me')
button.pack()

# print(button['text'])
# print(button.config())
# print(str(button))
# print(str(root))

button['text'] = 'Press Me'
button.config(text='Push Me')
root.mainloop()
