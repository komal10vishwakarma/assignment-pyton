import tkinter as tk
from time import strftime

def time():
    string=strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000,time)
def application_run():
    root=tk.Tk()
    root.title("Digital Clock")
    global label
    label=tk.Label(root,
                   font=('times new roman',50,'bold'),
                   background='black',
                   foreground='white'
                   )
    label.pack(anchor='center')
    time()
    root.mainloop()