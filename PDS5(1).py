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
f4a = Frame(f1, width=1350, height=330,bg='black')
f4a.pack(side=TOP)
f1a = Frame(f1, width=1350, height=370,bg='black')
f1a.pack(side=TOP)
f2a = Frame(f1, width=1350, height=330,bg='black')
f2a.pack(side=BOTTOM)

lblInfo=Label(Tops,fg='white',font=('Times New Roman',60,'bold'),text ="Pizza Management System",anchor='w')
lblInfo.configure(background="black") 
lblInfo.grid(row=0,column=0)

PaymentRef=StringVar()
CustomerName=StringVar()
MobileNumber=StringVar()
Pan=StringVar()
Medium=StringVar()
Large=StringVar()
TotalCost=StringVar()
Status=StringVar()

lblRef = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Order ID',justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=PaymentRef,justify='left')
txtRef.grid(row=0,column=1)

from tkinter import messagebox

def iExit():
	qExit = messagebox.askyesno("Billing system","Do you want to exit the system?")
	if qExit > 0:
		root.destroy()
		return

def Reset():
	PaymentRef.set("")

def show():
    c =con.execute("select * from order1")
    lblCust = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Customer Name',justify='left')
    lblCust.grid(row=1,column=0)
    txtCust=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=CustomerName,justify='left')
    txtCust.grid(row=1,column=1)

    lblCustMob = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Customer Mobile Number',justify='left')
    lblCustMob.grid(row=2,column=0)
    txtCustMob=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=MobileNumber,justify='left')
    txtCustMob.grid(row=2,column=1)

    lblPan = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Pan-Sized',justify='left')
    lblPan.grid(row=3,column=0)
    txtPan=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Pan,justify='left')
    txtPan.grid(row=3,column=1)

    lblMedium = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Medium-Sized',justify='left')
    lblMedium.grid(row=4,column=0)
    txtMedium=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Medium,justify='left')
    txtMedium.grid(row=4,column=1)

    lblLarge = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Large-Sized',justify='left')
    lblLarge.grid(row=5,column=0)
    txtLarge=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Large,justify='left')
    txtLarge.grid(row=5,column=1)

    lblTotalCost = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Total Cost',anchor='w')
    lblTotalCost.grid(row=6,column=0)
    txtTotalCost = Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=TotalCost,justify='left')
    txtTotalCost.grid(row=6,column=1)

    lblStatus = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Status',anchor='w')
    lblStatus.grid(row=7,column=0)
    txtStatus = Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Status,justify='left')
    txtStatus.grid(row=7,column=1)

    for i in c:
            if i[2]==PaymentRef.get():
                    CustomerName.set(i[0])
                    MobileNumber.set(i[1])
                    Pan.set(i[5])
                    Medium.set(i[6])
                    Large.set(i[7])
                    TotalCost.set(i[8])
                    x=random.randstr("Not Started","Making","On the Way","Delivered")
                    Status.set(x)
            else:
                    CustomerName.set("Not Found")
                    MobileNumber.set("Not Found")
                    Pan.set("Not Found")
                    Medium.set("Not Found")
                    Large.set("Not Found")
                    TotalCost.set("Not Found")
                    Status.set("Not Found")
    con.commit()

btnTrack=Button(f2a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Track Order',command=show).grid(row=0,column=0)

btnReset=Button(f2a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Reset',command=Reset).grid(row=0,column=1)

btnExit=Button(f2a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Exit',command=iExit).grid(row=0,column=2)

root.mainloop()
