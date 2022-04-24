
from ast import Try
from configparser import DuplicateSectionError
import tkinter as tk 



ventana = tk.Tk()


ventana.title("Employees Management")
def open1():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('700x400')
    win.configure()
    e3=tk.Label(win, text="Search for employees" ,bg="blue", fg="white", font='Helvetica 15 bold')
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    boton4= tk.Button(win, text= "Exit", command=win. destroy)
    boton4.pack(side=tk.TOP)

def open2():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('700x400')
    win.configure()
    e3=tk.Label(win, text="Add employees" ,bg="blue", fg="white", font='Helvetica 15 bold')
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    boton4= tk.Button(win, text= "Exit", command=win. BACK)
    boton4.pack(side=tk.TOP)


ventana.geometry('700x400')
etiquetal=tk.Label(ventana,text="Employees Managent", bg= "blue", fg= "white", font='Helvetica 15 bold')
etiquetal.pack(fill=tk.X)


boton1 = tk.Button(ventana,text= "Search for employees", command=open1)
boton1.place(x=20,y=50)



boton2 = tk.Button(ventana,text= "Add employees", command=open2)
boton2.place(x=280,y=50)

boton3 = tk.Button(ventana,text= "Delete employees")
boton3.place(x=580,y=50)



ventana.mainloop()






