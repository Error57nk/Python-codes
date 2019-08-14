import tkinter as tk
import UI_database as df

def action():
    try:
        idn=int(e1.get())
        record=df.DB.fetch(idn)
        if record == []:
            name.set("Nil")
            bal.set("Nil")
            err.set("  NO RECORD FOUND !!")
        else:
            name.set(record[0][1])
            bal.set(record[0][2])
            err.initialize("")
    except Exception:
        err.set("INVALID INPUT TRY AGAIN")
    e1.delete(0, 'end')
        
        
        
    
    

win=tk.Tk()
win.title(" #^# Display Detail")
win.geometry("400x450")
 
name=tk.StringVar()
bal=tk.StringVar()
err=tk.StringVar()

#label

lab1=tk.Label(win, text="Enter ID :-", font="Times 20",bd=5)
e1=tk.Entry(win, text="Enter ID :-", font="Times 20", fg="blue",bd=5, width=15)
e1.focus()
#button
src=tk.Button(win, text="Search", font="Times 30", fg="orange",command=action,bd=5,bg='green')

info=tk.Label(win, text="Informations are :", font="Times 20", fg="green")
#Dynamic
n1=tk.Label(win, text="Name :-", font="Times 20")
n2=tk.Label(win, textvariable=name, font="Times 20")
b1=tk.Label(win, text="Balance :-", font="Times 20")
b2=tk.Label(win, textvariable=bal, font="Times 20")

exp=tk.Label(win, textvariable=err, font="Times 20", fg="red")
'''#grid
lab1.grid(row=0 ,column=0 )
e1.grid(row=0,column=1)

info.grid(row=1,column=0)

n1.grid(row=2,column=0)
n2.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
'''
lab1.place(x=0, y=10)
e1.place(x=130, y=10)
src.place(x=120, y=60)
info.place(x=100, y=180)
n1.place(x=40, y=220)
n2.place(x=130, y=220)
b1.place(x=40, y=270)
b2.place(x=160, y=270)
exp.place(x=20, y=340)
win.mainloop()
