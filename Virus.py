from tkinter import*
from tkinter import messagebox
def click():
    while(True):
        messagebox.showwarning(title='WARNING!!!!!',message='You have a virus.')
window=Tk()
button=Button(window,text='Click me if you dare',command=click)
button.pack()
window.mainloop()
