from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk

root = Tk()
style = Style(theme="flatly")

frame = ttk.Frame(root, padding="20 20 20 20")
frame.pack(fill='both', expand=True)

scrollbar = ttk.Scrollbar(frame, orient=VERTICAL)
text = Text(frame, yscrollcommand=scrollbar.set)

for i in range(100):
    text.insert(END, f"line {i}\n")

scrollbar.config(command=text.yview)
text.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()