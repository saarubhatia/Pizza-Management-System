from tkinter import*
import random
import time
import datetime
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.configure(background="black")
root.title("Pizza Management System")

def Order():
    global root
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
    f2a.pack(side=LEFT)
    f3a = Frame(f1, width=1350, height=330,bg='black')
    f3a.pack(side=RIGHT)

    lblInfo=Label(Tops,fg='white',font=('Times New Roman',60,'bold'),text ="Pizza Management System",anchor='w')
    lblInfo.configure(background="black") 
    lblInfo.grid(row=0,column=0)

    CustomerName=StringVar()
    MobileNumber=StringVar()

    lblCust = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Customer Name',justify='left')
    lblCust.grid(row=0,column=0)
    txtCust=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=CustomerName,justify='left')
    txtCust.grid(row=0,column=1)

    lblCustMob = Label(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Customer Mobile Number',justify='left')
    lblCustMob.grid(row=1,column=0)
    txtCustMob=Entry(f4a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=MobileNumber,justify='left')
    txtCustMob.grid(row=1,column=1)

    PaymentRef=StringVar()
    Pan=StringVar()
    Medium=StringVar()
    Large=StringVar()

    Pan.set(0)
    Medium.set(0)
    Large.set(0)

    lblRef = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Order ID',justify='left')
    lblRef.grid(row=0,column=0)
    txtRef=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=PaymentRef,justify='left')
    txtRef.grid(row=0,column=1)

    lblPan = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Pan-Sized',justify='left')
    lblPan.grid(row=1,column=0)
    txtPan=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Pan,justify='left')
    txtPan.grid(row=1,column=1)

    lblMedium = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Medium-Sized',justify='left')
    lblMedium.grid(row=2,column=0)
    txtMedium=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Medium,justify='left')
    txtMedium.grid(row=2,column=1)

    lblLarge = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Large-Sized',justify='left')
    lblLarge.grid(row=3,column=0)
    txtLarge=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Large,justify='left')
    txtLarge.grid(row=3,column=1)

    TimeofOrder=StringVar()
    perPan=StringVar()
    perMedium=StringVar()
    perLarge=StringVar()

    TimeofOrder.set(time.strftime("%H:%M:%S"))
    perPan.set(199)
    perMedium.set(299)
    perLarge.set(399)

    lblTimeofOrder = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Order Time',anchor='w')
    lblTimeofOrder.grid(row=0,column=2)
    txtTimeofOrder=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=TimeofOrder,justify='left')
    txtTimeofOrder.grid(row=0,column=3)

    lblperPan = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Cost/Pizza',anchor='w')
    lblperPan.grid(row=1,column=2)
    txtperPan=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=perPan,justify='left')
    txtperPan.grid(row=1,column=3)


    lblperMedium = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Cost/Pizza',anchor='w')
    lblperMedium.grid(row=2,column=2)
    txtperMedium=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=perMedium,justify='left')
    txtperMedium.grid(row=2,column=3)

    lblperLarge = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Cost/Pizza',anchor='w')
    lblperLarge.grid(row=3,column=2)
    txtperLarge=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=perLarge,justify='left')
    txtperLarge.grid(row=3,column=3)

    DateofOrder=StringVar()
    CostofPan=StringVar()
    CostofMedium=StringVar()
    CostofLarge=StringVar()

    DateofOrder.set(time.strftime("%d/%m/%y"))

    lblDateofOrder = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Order Date',anchor='w')
    lblDateofOrder.grid(row=0,column=4)
    txtDateofOrder=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=DateofOrder,justify='left')
    txtDateofOrder.grid(row=0,column=5)

    lblCostofPan = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Total(Pan-Sized)',anchor='w')
    lblCostofPan.grid(row=1,column=4)
    txtCostofPan=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=CostofPan,justify='left')
    txtCostofPan.grid(row=1,column=5)


    lblCostofMedium = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Total(Medium-Sized)',anchor='w')
    lblCostofMedium.grid(row=2,column=4)
    txtCostofMedium=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=CostofMedium,justify='left')
    txtCostofMedium.grid(row=2,column=5)

    lblCostofLarge = Label(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Total(Large-Sized)',anchor='w')
    lblCostofLarge.grid(row=3,column=4)
    txtCostofLarge=Entry(f1a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=CostofLarge,justify='left')
    txtCostofLarge.grid(row=3,column=5)

    PaidTax=StringVar()
    SubTotal=StringVar()
    TotalCost=StringVar()

    lblPaidTax = Label(f2a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Tax',anchor='w')
    lblPaidTax.grid(row=1,column=0)
    txtPaidTax = Entry(f2a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=PaidTax,justify='left')
    txtPaidTax.grid(row=1,column=1)

    lblSubTotal = Label(f2a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Sub Total',anchor='w')
    lblSubTotal.grid(row=0,column=0)
    txtSubTotal = Entry(f2a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=SubTotal,justify='left')
    txtSubTotal.grid(row=0,column=1)

    lblTotalCost = Label(f2a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Total Cost',anchor='w')
    lblTotalCost.grid(row=2,column=0)
    txtTotalCost = Entry(f2a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=TotalCost,justify='left')
    txtTotalCost.grid(row=2,column=1)

    def CostOfOrder():
        Pan1 = float(Pan.get())
        Medium1 = float(Medium.get())
        Large1 = float(Large.get())
        PanperPrice = float(perPan.get())
        MediumperPrice = float(perMedium.get())
        LargeperPrice = float(perLarge.get())
	
        PanCost = "Rs " + str("%.2f"%((Pan1*PanperPrice)))
        CostofPan.set(PanCost)
	
        MediumCost = "Rs " + str("%.2f"%((Medium1*MediumperPrice)))
        CostofMedium.set(MediumCost)
	
        LargeCost = "Rs " + str("%.2f"%((Large1*LargeperPrice)))
        CostofLarge.set(LargeCost)
	
        ToC = "Rs " + str("%.2f"%((Pan1*PanperPrice)+(Medium1*MediumperPrice)+(Large1*LargeperPrice)))
        SubTotal.set(ToC)
	
        Tax = "Rs " + str("%.2f"%((Pan1*PanperPrice)+(Medium1*MediumperPrice)+(Large1*LargeperPrice)*0.18))
        PaidTax.set(Tax)
	
        TaxPay = ((Pan1*PanperPrice)+(Medium1*MediumperPrice)+(Large1*LargeperPrice))*0.18
        Cost = ((Pan1*PanperPrice)+(Medium1*MediumperPrice)+(Large1*LargeperPrice))
        CostofItems = "Rs " + str("%.2f"%(TaxPay+Cost))
        TotalCost.set(CostofItems)
	
        x=random.randint(10034,699812)
        randomRef=str(x)
        PaymentRef.set("BILL"+randomRef)

        name=CustomerName.get()
        mob=MobileNumber.get()
        oid=PaymentRef.get()
        dt=DateofOrder.get()
        tm=TimeofOrder.get()
        pn=Pan.get()
        md=Medium.get()
        lr=Large.get()
        ct=TotalCost.get()
        #con.execute("create table order1(CustomerName varchar(50), MobileNumber varchar(10),OrderID varchar(50),DateOfOrder varchar(50),TimeOfOrder varchar(50),PanPizza varchar(10),MediumPizza varchar(10),LargePizza varchar(10),TotalCost varchar(20));")
        con.execute("insert into order1(CustomerName,MobileNumber,OrderID,DateOfOrder,TimeOfOrder,PanPizza,MediumPizza,LargePizza,TotalCost)values(?,?,?,?,?,?,?,?,?)",(name,mob,oid,dt,tm,pn,md,lr,ct))
        con.commit()

    
    btnTotal=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Total Cost', command = CostOfOrder).grid(row=0,column=0)

    btnReset=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Reset',command=Reset).grid(row=0,column=1)

    btnExit=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Exit',command=lambda :iExit(root)).grid(row=0,column=2)

    root.mainloop()

def iExit(root):
      qExit = messagebox.askyesno("Pizza Management System","Do you want to exit the system?")
      if qExit>0:
          root.destroy()
          return

def Reset():
	PaymentRef.set("")
	Pan.set(0)
	Medium.set(0)
	Large.set(0)
	PaidTax.set("")
	SubTotal.set("")
	TotalCost.set("")
	CostofPan.set("")
	CostofMedium.set("")
	CostofLarge.set("")
	CustomerName.set("")
	MobileNumber.set("")

def trackorder():
  root = Tk()
  root.geometry("1350x750+0+0")
  root.configure(background="black")
  root.title("Pizza Management System")
  con=sqlite3.connect("OrderPizza.db")

  Tops = Frame(root, width=1350, height=100)
  Tops.pack(side=TOP)
  f2 = Frame(root, width=1350, height=700,bg='black')
  f2.pack(side=TOP)
  f42a = Frame(f2, width=1350, height=330,bg='black')
  f42a.pack(side=TOP)
  f22a = Frame(f2, width=1350, height=330,bg='black')
  f22a.pack(side=BOTTOM)

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

  lblRef = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Order ID',justify='left')
  lblRef.grid(row=0,column=0)
  txtRef=Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=PaymentRef,justify='left')
  txtRef.grid(row=0,column=1)

  btnTrack=Button(f22a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Track Order',command=lambda: showa(PaymentRef))
  btnTrack.grid(row=0,column=0)
  btnReset=Button(f22a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Reset',command=Reseta)
  btnReset.grid(row=0,column=1)
  btnExit=Button(f22a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Exit',command=lambda:iExita(root))
  btnExit.grid(row=0,column=2)
  
  root.mainloop()


def iExita(root):
    qExit = messagebox.askyesno("Cancel/Track Order","Do you want to exit this page?")
    if qExit>0:
        root.destroy()
        return

def Reseta():
	PaymentRef.set("")

def showa(a):
    root = Tk()
    root.geometry("1350x750+0+0")
    root.configure(background="black")
    root.title("Pizza Management System")
    con=sqlite3.connect("OrderPizza.db")

    c =con.execute("select * from order1")

    CustomerName=StringVar()
    MobileNumber=StringVar()
    Pan=StringVar()
    Medium=StringVar()
    Large=StringVar()
    TotalCost=StringVar()
    Status=StringVar()

    Tops = Frame(root, width=1350, height=100)
    Tops.pack(side=TOP)
    f2 = Frame(root, width=1350, height=700,bg='black')
    f2.pack(side=TOP)
    f42a = Frame(f2, width=1350, height=330,bg='black')
    f42a.pack(side=TOP)
    f22a = Frame(f2, width=1350, height=330,bg='black')
    f22a.pack(side=BOTTOM)
    
    lblInfo=Label(Tops,fg='white',font=('Times New Roman',60,'bold'),text ="Pizza Management System",anchor='w')
    lblInfo.configure(background="black") 
    lblInfo.grid(row=0,column=0)
    
    lblCust = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Customer Name',justify='left')
    lblCust.grid(row=1,column=0)
    txtCust=Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=CustomerName,justify='left')
    txtCust.grid(row=1,column=1)

    lblCustMob = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Customer Mobile Number',justify='left')
    lblCustMob.grid(row=2,column=0)
    txtCustMob=Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=MobileNumber,justify='left')
    txtCustMob.grid(row=2,column=1)

    lblPan = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Pan-Sized',justify='left')
    lblPan.grid(row=3,column=0)
    txtPan=Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Pan,justify='left')
    txtPan.grid(row=3,column=1)

    lblMedium = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Medium-Sized',justify='left')
    lblMedium.grid(row=4,column=0)
    txtMedium=Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Medium,justify='left')
    txtMedium.grid(row=4,column=1)

    lblLarge = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Large-Sized',justify='left')
    lblLarge.grid(row=5,column=0)
    txtLarge=Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Large,justify='left')
    txtLarge.grid(row=5,column=1)

    lblTotalCost = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Total Cost',anchor='w')
    lblTotalCost.grid(row=6,column=0)
    txtTotalCost = Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=TotalCost,justify='left')
    txtTotalCost.grid(row=6,column=1)

    lblStatus = Label(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),text='Status',anchor='w')
    lblStatus.grid(row=7,column=0)
    txtStatus = Entry(f42a,fg='white',bg='black',font=('Times New Roman',16,'bold'),textvariable=Status,justify='left')
    txtStatus.grid(row=7,column=1)

    for i in c:
            if i[2]==a:
                    CustomerName.set(i[0])
                    MobileNumber.set(i[1])
                    Pan.set(i[5])
                    Medium.set(i[6])
                    Large.set(i[7])
                    TotalCost.set(i[8])
                    Status.set("Delivered")
                    x=sample("Making","On the Way","Delivered")
                    
            else:
                    CustomerName.set("Not Found")
                    MobileNumber.set("Not Found")
                    Pan.set("Not Found")
                    Medium.set("Not Found")
                    Large.set("Not Found")
                    TotalCost.set("Not Found")
                    Status.set("Not Found")

    btnReset=Button(f22a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Reset',command=trackorder)
    btnReset.grid(row=0,column=1)
    btnExit=Button(f22a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Exit',command=lambda:iExita(root))
    btnExit.grid(row=0,column=2)

    con.commit()

def cancelorder():
    root = Tk()
    root.geometry("1350x750+0+0")
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

    btnCancel=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Cancel Order',command=lambda :Cancel(PaymentRef)).grid(row=0,column=0)

    btnReset=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Reset',command=Resetb).grid(row=0,column=1)

    btnExit=Button(f3a,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='Exit',command=lambda:iExita(root)).grid(row=0,column=2)

    root.mainloop()

def Resetb():
    PaymentRef.set("")
    CustomerName.set("")

def Cancel(a):
    con=sqlite3.connect("OrderPizza.db")
    c =con.execute("select * from order1")
    
    b=0
    for i in c:
            if i[2]==a:
                b=1
                a=messagebox.askyesno("Pizza Delivery System","Do you want to cancel this order?")
                if a>0:
                    con.execute("delete from order1 where OrderID='"+str(i[2])+"'")
                    messagebox.showinfo("Pizza Delivery System","The chosen order is deleted")
                    break
    if b==0:
            messagebox.showinfo("Pizza Delivery System","The OrderID does not exist")

def begin():
    global root
    con=sqlite3.connect("OrderPizza.db")

    Tops = Frame(root, width=1350, height=100)
    Tops.pack(side=TOP)
    f1 = Frame(root, width=1350, height=700,bg='black')
    f1.pack(side=TOP)

    lblInfo=Label(Tops,fg='white',font=('Times New Roman',60,'bold'),text ="Pizza Management System",anchor='w')
    lblInfo.configure(background="black") 
    lblInfo.grid(row=0,column=0)

    btnOrder=Button(f1,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='ORDER NEW PIZZA',command=Order)
    btnOrder.grid(row=0,column=0)
    btnCOrder=Button(f1,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='CANCEL ORDER',command=cancelorder)
    btnCOrder.grid(row=1,column=0)
    btnTOrder=Button(f1,padx=16,pady=16,fg='white',bg='black',font=('Times New Roman',16,'bold'),width=15,text='TRACK ORDER',command=trackorder)
    btnTOrder.grid(row=2,column=0)

    root.mainloop()

begin()
