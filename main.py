from tkinter import *
window=Tk()
window.title("Temperature convertor")
window.minsize(300,200)
window.config(padx=10,pady=10)

l=Label(text="Celsius",font=("Arial",10,"bold"))
l.grid(row=30,column=30)

e=Entry(width=10)
e.grid(row=30,column=10)

l1=Label(text="is equal to",font=("Arial",10,"bold"))
l1.grid(row=35,column=0)

def convert():

    if e.get():
        c=int(e.get())
        f=str((c*9/5)+32)
        t.insert(index=5, string=f)
        e.delete(0,"end")
    else:
        f=int(t.get())
        c=str((f-32)*5/9)
        e.insert(index=5,string=c)
        t.delete(0,"end")



t=Entry(width=10)
t.grid(row=35,column=10)


b=Button(text="Convert", command=convert)
b.grid(row=40, column=10)


window.mainloop()