from tkinter import *
from tkinter import ttk
import bf_interpreter

root = Tk()
# main window setup
root.geometry("560x560")
root.minsize(height=560, width=560)
root.title("BrainFuck IDE")
# scrollbar setup
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
# text box setup
text_info = Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

scrollbar.config(command=text_info.yview)

root.mainloop()
