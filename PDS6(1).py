from tkinter import*
import random
import time
import datetime
import sqlite3

root = Tk()
root.geometry("1350x650+0+0")
root.configure(background="black")
root.title("Pizza Management System")
con=sqlite3.connect("OrderPizza.db")

Tops = Frame(root, width=1350, height=100)
Tops.pack(side=TOP)
f1 = Frame(root, width=1350, height=700,bg='black')
f1.pack(side=TOP)
f1a = Frame(f1, width=1350, height=370,bg='black')
f1a.pack(side=TOP)
f3a = Frame(f1, width=1350, height=370,bg='black')
f3a.pack(side=BOTTOM)

lblInfo=Label(Tops,fg='white',font=('Times New Roman',60,'bold'),text ="Pizza Management System",anchor='w')
lblInfo.configure(background="black") 
lblInfo.grid(row=0,column=0)

CustomerName=StringVar()
PaymentRef=StringVar()

lblCust = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Customer Name',justify='left')
lblCust.grid(row=0,column=0)
txtCust=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=CustomerName,justify='left')
txtCust.grid(row=0,column=1)

lblRef = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Order ID',justify='left')
lblRef.grid(row=1,column=0)
txtRef=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=PaymentRef,justify='left')
txtRef.grid(row=1,column=1)

from tkinter import messagebox

def iExit():
	qExit = messagebox.askyesno("Billing system","Do you want to exit the system?")
	if qExit > 0:
		root.destroy()
		return

def Reset():
	PaymentRef.set("")
	CustomerName.set("")

def Cancel():
    c =con.execute("select * from order1")
    b=0
    for i in c:
            if i[2]==PaymentRef.get():
                b=1
                a=messagebox.askyesno("Pizza Delivery System","Do you want to cancel this order?")
                if a>0:
                    con.execute("delete from order1 where OrderID='"+str(i[2])+"'")
                    messagebox.showinfo("Pizza Delivery System","The chosen order is deleted")
                    break
    if b==0:
            messagebox.showinfo("Pizza Delivery System","The OrderID does not exist")

btnCancel=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Cancel Order',command=Cancel).grid(row=0,column=0)

btnReset=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Reset',command=Reset).grid(row=0,column=1)

btnExit=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Exit',command=iExit).grid(row=0,column=2)

root.mainloop()
