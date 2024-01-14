from tkinter import *
from tkinter import messagebox
import random,tempfile
import os,tempfile,smtplib

def clear():
     bathsoapentry.delete(0,END)
     facecreamentry.delete(0,END)
     facewashentry.delete(0,END)
     harigelentry.delete(0,END)
     hairsprayentry.delete(0,END)
     bodylotionentry.delete(0,END)

     daalentry.delete(0,END)
     riceentry.delete(0,END)
     oilentry.delete(0,END)
     Wheatentry.delete(0,END)
     sugarentry.delete(0,END)
     teaentry.delete(0,END)


     cocacolaentry.delete(0,END)
     pepsientry.delete(0,END)
     mazzaentry.delete(0,END)
     Dewentry.delete(0,END)
     Spriteentry.delete(0,END)
     frootientry.delete(0,END)
     


     bathsoapentry.insert(0,0)
     facewashentry.insert(0,0)
     facecreamentry.insert(0,0)
     hairsprayentry.insert(0,0)
     harigelentry.insert(0,0)
     bodylotionentry.insert(0,0)

     daalentry.insert(0,0)
     Wheatentry.insert(0,0)
     riceentry.insert(0,0)
     oilentry.insert(0,0)
     sugarentry.insert(0,0)
     teaentry.insert(0,0)

     pepsientry.insert(0,0)
     cocacolaentry.insert(0,0)
     Spriteentry.insert(0,0)
     frootientry.insert(0,0)
     mazzaentry.insert(0,0)
     Dewentry.insert(0,0)

     cosmatictaxentry.delete(0,END)
     grocerytaxentry.delete(0,END)
     drinkstaxentry.delete(0,END)

     cosmaticpriceentry.delete(0,END)
     grocerypriceentry.delete(0,END)
     drinkspriceentry.delete(0,END)

     nameentry.delete(0,END)
     phoneentry.delete(0,END)
     billnoentry.delete(0,END)

     textarea.delete(1.0,END)

     




def send_email():
    def send_gmail():
         try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderentry.get(),passwordentry.get())
            message=email_textarea.get(1.0,END)
            reciever_Address=receiverentry.get()
            ob.sendmail(senderentry.get(),reciever_Address,message)
            ob.quit()
            messagebox.showinfo('Success','Bill is Successfully Sent',parent=root1)
            root.destroy()
         except:
              messagebox.showerror('Error','Something went wrong, Please try again')

         
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        senderframe=LabelFrame(root1,text='SENDER',font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        senderframe.grid(row=0,column=0,padx=40,pady=20)

        senderlabel=Label(senderframe,text="Sender's Email",font=('arial',12,'bold'),bd=6,bg='gray20',fg='white')
        senderlabel.grid(row=0,column=0,padx=10,pady=8)

        senderentry=Entry(senderframe,font=('arial',12,'bold'),bd=2,width=23,relief=RIDGE)
        senderentry.grid(row=0,column=1,padx=10,pady=8)


        passwordlabel=Label(senderframe,text="Password",font=('arial',12,'bold'),bd=6,bg='gray20',fg='white')
        passwordlabel.grid(row=1,column=0,padx=10,pady=8)

        passwordentry=Entry(senderframe,font=('arial',12,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordentry.grid(row=1,column=1,padx=10,pady=8)


        recipientframe=LabelFrame(root1,text='RECIPIENT',font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        recipientframe.grid(row=1,column=0,padx=40,pady=20)

        receiverlabel=Label(recipientframe,text="Email Address",font=('arial',12,'bold'),bd=6,bg='gray20',fg='white')
        receiverlabel.grid(row=0,column=0,padx=10,pady=8)

        receiverentry=Entry(recipientframe,font=('arial',12,'bold'),bd=2,width=23,relief=RIDGE)
        receiverentry.grid(row=0,column=1,padx=10,pady=8)

        messagelabel=Label(recipientframe,text="Message",font=('arial',12,'bold'),bd=6,bg='gray20',fg='white')
        messagelabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientframe,font=('arial',12,'bold'),bd=2,relief=SUNKEN,
                            width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


        sendbutton=Button(root1,text='SEND',font=('arial',14,'bold'),width=15,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)

        root.mainloop()
        
      



def print_bill():
      if textarea.get(1.0,END)=='\n':
            messagebox.showerror('Error','Bill is Empty')
      else:
            file=tempfile.mktemp('.txt')
            open(file,'w').write(textarea.get(1.0,END))
            os.startfile(file,'print')
            


def search_bill():
      for i in os.listdir('bills/'):
          if i.split('.')[0]==billnoentry.get():
              f=open(f'bills/{i}','r')
              textarea.delete(1.0,END)
              for data in f:
                    textarea.insert(END,data)
              f.close()
              break
      else:
            messagebox.showerror('Error','Invalid bill number')




def save_bill():
    result=messagebox.askyesno('Confirm','Do you want to save bill ?')
    if result:
        bill_content=textarea.get(1.0,END)
        billnumber = random.randint(500, 1000)
        
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'{billnumber} is saves Successfully')
       



billnumber = random.randint(500, 1000)


def bill_area():
        if nameentry.get()=='' or phoneentry.get() == '':
            messagebox.showerror('Error', 'Custumer Details are Required')
        elif cosmaticpriceentry.get() == '' and grocerypriceentry.get() == '' and drinkspriceentry.get() == '':
            messagebox.showerror('Error', 'No Product are Selected')
        elif cosmaticpriceentry.get() == '0 Rs' and grocerypriceentry.get() == '0 Rs' and drinkspriceentry.get() == '0 Rs':
            messagebox.showerror('Error', 'No Product are Selected')
        else:
            textarea.delete(1.0, END)

            textarea.insert(END, "\t\t\t**Welcome Custumer**")
            textarea.insert(END, f"\nBill number:{billnumber}\n")
            textarea.insert(END, f"\nCustumer Name:{nameentry.get()}\n")
            textarea.insert(END, f"\nCustumer Phone number:{phoneentry.get()}\n")
            textarea.insert(END, "\n==========================================================")
            textarea.insert(END, "Product\t\t\tQuantity\t\t\tPrice")
            textarea.insert(END, "\n==========================================================")
            if bathsoapentry.get() != "0":
                  textarea.insert(
                        END, f"\nBath Soap\t\t\t{bathsoapentry.get()}\t\t\t{soapprice} Rs"
                  )
            if hairsprayentry.get() != "0":
                  textarea.insert(
                        END, f"\nHair spray\t\t\t{hairsprayentry.get()}\t\t\t{hairsprayprice} Rs"
                  )
            if harigelentry.get() != "0":
                  textarea.insert(
                        END, f"\nHair Gel\t\t\t{harigelentry.get()}\t\t\t{hairgelprice} Rs"
                  )
            if facecreamentry.get() != "0":
                  textarea.insert(
                        END, f"\nFace ceram\t\t\t{facecreamentry.get()}\t\t\t{facecreamprice} Rs"
                  )
            if facewashentry.get() != "0":
                  textarea.insert(
                        END, f"\nFace wash\t\t\t{facewashentry.get()}\t\t\t{facewashprice} Rs"
                  )
            if bodylotionentry.get() != "0":
                  textarea.insert(
                        END, f"\nBody lotion\t\t\t{bodylotionentry.get()}\t\t\t{bodylotionprice} Rs"
                  )

            # this are for grocery

            if riceentry.get() != "0":
                  textarea.insert(END, f"\nRice\t\t\t{riceentry.get()}\t\t\t{riceprice} Rs")
            if daalentry.get() != "0":
                  textarea.insert(END, f"\nDal\t\t\t{daalentry.get()}\t\t\t{dalprice} Rs")
            if oilentry.get() != "0":
                  textarea.insert(END, f"\nOil\t\t\t{oilentry.get()}\t\t\t{oilprice} Rs")
            if sugarentry.get() != "0":
                  textarea.insert(END, f"\nSugar\t\t\t{sugarentry.get()}\t\t\t{sugarprice} Rs")
            if Wheatentry.get() != "0":
                  textarea.insert(END, f"\nWheat\t\t\t{Wheatentry.get()}\t\t\t{wheatprice} Rs")
            if teaentry.get() != "0":
                  textarea.insert(END, f"\nTea\t\t\t{teaentry.get()}\t\t\t{teaprice} Rs")

            # this is the section of colddrink section
            if mazzaentry.get() != "0":
                  textarea.insert(END, f"\nMazza\t\t\t{mazzaentry.get()}\t\t\t{mazaprice} Rs")
            if pepsientry.get() != "0":
                  textarea.insert(END, f"\nPepsi\t\t\t{pepsientry.get()}\t\t\t{pepsiprice} Rs")
            if Spriteentry.get() != "0":
                  textarea.insert(END, f"\nSprite\t\t\t{Spriteentry.get()}\t\t\t{spriteprice} Rs")
            if Dewentry.get() != "0":
                  textarea.insert(END, f"\nDew\t\t\t{Dewentry.get()}\t\t\t{Deweprice} Rs")
            if cocacolaentry.get() != "0":
                  textarea.insert(
                        END, f"\nCoca Cola \t\t\t{cocacolaentry.get()}\t\t\t{cococolaprice} Rs"
                  )
            if frootientry.get() != "0":
                  textarea.insert(END, f"\nFrooti\t\t\t{frootientry.get()}\t\t\t{frootiprice} Rs")

            textarea.insert(END, "\n----------------------------------------------------------")

            if cosmatictaxentry.get() != "0.0 Rs":
                  textarea.insert(END, f"\nCosmatic Tax\t\t\t\t{cosmatictaxentry.get()}")
            if grocerytaxentry.get() != "0.0 Rs":
                  textarea.insert(END, f"\nGrocery Tax\t\t\t\t{grocerytaxentry.get()}")
            if drinkstaxentry.get() != "0.0 Rs":
                  textarea.insert(END, f"\nCold Drink  Tax\t\t\t\t{drinkstaxentry.get()}")

            textarea.insert(END, f"\n\nToatal Bill\t\t\t\t{totalbill}")
            textarea.insert(END, "\n----------------------------------------------------------")

            save_bill()



# functionality part  aur calculation part of the functionility
def total():
    global soapprice, hairsprayprice, hairgelprice, facecreamprice, facewashprice, bodylotionprice, oilprice, sugarprice, teaprice, wheatprice, riceprice, dalprice, mazaprice, frootiprice, Deweprice, pepsiprice, spriteprice, cococolaprice, totalbill
    soapprice = int(bathsoapentry.get()) * 20
    facecreamprice = int(facecreamentry.get()) * 50
    facewashprice = int(facewashentry.get()) * 100
    hairsprayprice = int(hairsprayentry.get()) * 150
    hairgelprice = int(harigelentry.get()) * 80
    bodylotionprice = int(bodylotionentry.get()) * 60

    totalcosmaticprice = (
        soapprice
        + facecreamprice
        + facewashprice
        + hairsprayprice
        + hairgelprice
        + bodylotionprice
    )
    cosmaticpriceentry.delete(0, END)
    cosmaticpriceentry.insert(0, str(totalcosmaticprice) + "Rs")
    cosmatictax = totalcosmaticprice * 0.12
    cosmatictaxentry.delete(0, END)
    cosmatictaxentry.insert(0, str(cosmatictax) + "Rs")

    # grocery calculation
    riceprice = int(riceentry.get()) * 30
    dalprice = int(daalentry.get()) * 100
    oilprice = int(oilentry.get()) * 120
    sugarprice = int(sugarentry.get()) * 50
    teaprice = int(teaentry.get()) * 140
    wheatprice = int(Wheatentry.get()) * 80

    totalgroceyprice = (
        riceprice + dalprice + oilprice + sugarprice + teaprice + wheatprice
    )
    grocerypriceentry.delete(0, END)
    grocerypriceentry.insert(0, str(totalgroceyprice) + "Rs")
    grocerytax = totalgroceyprice * 0.10
    grocerytaxentry.delete(0, END)
    grocerytaxentry.insert(0, str(grocerytax) + "Rs")

    # colddrink price

    mazaprice = int(mazzaentry.get()) * 50
    frootiprice = int(frootientry.get()) * 20
    Deweprice = int(Dewentry.get()) * 30
    pepsiprice = int(pepsientry.get()) * 20
    spriteprice = int(Spriteentry.get()) * 45
    cococolaprice = int(cocacolaentry.get()) * 90

    tatoalcolddrinkprice = (
        mazaprice + frootiprice + Deweprice + pepsiprice + spriteprice + cococolaprice
    )
    drinkspriceentry.delete(0, END)
    drinkspriceentry.insert(0, str(tatoalcolddrinkprice) + "Rs")

    colddrinktax = tatoalcolddrinkprice * 0.08
    drinkstaxentry.delete(0, END)
    drinkstaxentry.insert(0, str(colddrinktax) + "Rs")

    totalbill = (
        totalcosmaticprice
        + totalgroceyprice
        + tatoalcolddrinkprice
        + cosmatictax
        + grocerytax
        + colddrinktax
    )


# GUI part
root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.iconbitmap("billing icon.ico")

heading_label = Label(
    root,
    text="Retail Billing System",
    font=("times new roman", 20, "bold"),
    bg="gray20",
    fg="gold",
    bd=12,
    relief=GROOVE,
)
heading_label.pack(fill=X)


custumer_details_frame = LabelFrame(
    root,
    text="Custumer details",
    font=("times new roman", 16, "bold"),
    fg="gold",
    bd=8,
    relief=GROOVE,
    bg="gray20",
)
custumer_details_frame.pack(fill=X, pady=2)


namelabel = Label(
    custumer_details_frame,
    text="Name",
    font=("times new roman", 16, "bold"),
    bg="gray20",
    fg="white",
)
namelabel.grid(row=0, column=0, padx=20)
nameentry = Entry(custumer_details_frame, font=("arial", 15), bd=7, width=18)
nameentry.grid(row=0, column=1, padx=8)


phonelabel = Label(
    custumer_details_frame,
    text="Phone Number",
    font=("times new roman", 16, "bold"),
    bg="gray20",
    fg="white",
)
phonelabel.grid(row=0, column=2, padx=20)
phoneentry = Entry(custumer_details_frame, font=("arial", 15), bd=7, width=18)
phoneentry.grid(row=0, column=3, padx=8)


billnumberlabel = Label(
    custumer_details_frame,
    text="Bill number",
    font=("times new roman", 16, "bold"),
    bg="gray20",
    fg="white",
)
billnumberlabel.grid(row=0, column=4, padx=20)
billnoentry = Entry(custumer_details_frame, font=("arial", 15), bd=7, width=18)
billnoentry.grid(row=0, column=5, padx=8)


searchbutton = Button(
    custumer_details_frame, text="SEARCH", font=("arial", 15, "bold"), bd=7
,command=search_bill)
searchbutton.grid(row=0, column=6, padx=20)


productframe = Frame(root)
productframe.pack(pady=2)

cosmaticframe = LabelFrame(
    productframe,
    text="Cosmatics",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    relief=GROOVE,
    bg="gray20",
)
cosmaticframe.grid(row=0, column=0)


bathsoaplabel = Label(
    cosmaticframe,
    text="Bath soap",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bathsoaplabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")
bathsoapentry = Entry(
    cosmaticframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
bathsoapentry.grid(row=0, column=1, pady=9, padx=6)
bathsoapentry.insert(0, 0)


facecreamlabel = Label(
    cosmaticframe,
    text="Face cream",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
facecreamlabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")
facecreamentry = Entry(
    cosmaticframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
facecreamentry.grid(row=1, column=1, pady=9, padx=10)
facecreamentry.insert(0, 0)

facewashlabel = Label(
    cosmaticframe,
    text="Face Wash",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
facewashlabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")
facewashentry = Entry(
    cosmaticframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
facewashentry.grid(row=2, column=1, pady=9, padx=10)
facewashentry.insert(0, 0)

hairspraylabel = Label(
    cosmaticframe,
    text="Hair spray",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
hairspraylabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")
hairsprayentry = Entry(
    cosmaticframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
hairsprayentry.grid(row=3, column=1, pady=9, padx=10)
hairsprayentry.insert(0, 0)

harigellabel = Label(
    cosmaticframe,
    text="Hair Gel",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
harigellabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")
harigelentry = Entry(
    cosmaticframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
harigelentry.grid(row=4, column=1, pady=9, padx=10)
harigelentry.insert(0, 0)

bodylotionlabel = Label(
    cosmaticframe,
    text="Body Lotion",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bodylotionlabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")
bodylotionentry = Entry(
    cosmaticframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
bodylotionentry.grid(row=5, column=1, pady=9, padx=10)
bodylotionentry.insert(0, 0)


groceryframe = LabelFrame(
    productframe,
    text="Grocery",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    relief=GROOVE,
    bg="gray20",
)
ricelabel = Label(
    groceryframe,
    text="Rice",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
groceryframe.grid(row=0, column=1)
riceentry = Entry(groceryframe, font=("times new roman", 15, "bold"), width=10, bd=5)
riceentry.insert(0, 0)


oillabel = Label(
    groceryframe,
    text="Oil",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
oilentry = Entry(groceryframe, font=("times new roman", 15, "bold"), width=10, bd=5)
ricelabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")
riceentry.grid(row=0, column=1, pady=9, padx=10)
oilentry.insert(0, 0)


daallabel = Label(
    groceryframe,
    text="Daal",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
oillabel.grid(row=1, column=0, pady=9, padx=6, sticky="w")
daalentry = Entry(groceryframe, font=("times new roman", 15, "bold"), width=10, bd=5)
oilentry.grid(row=1, column=1, pady=9, padx=10)
daalentry.insert(0, 0)

Wheatlabel = Label(
    groceryframe,
    text="Wheat",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
Wheatentry = Entry(groceryframe, font=("times new roman", 15, "bold"), width=10, bd=5)
daallabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")
daalentry.grid(row=2, column=1, pady=9, padx=10)
Wheatentry.insert(0, 0)


sugarlabel = Label(
    groceryframe,
    text="Sugar",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
sugarentry = Entry(groceryframe, font=("times new roman", 15, "bold"), width=10, bd=5)
Wheatlabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")
Wheatentry.grid(row=3, column=1, pady=9, padx=10)
sugarentry.insert(0, 0)


tealabel = Label(
    groceryframe,
    text="Tea",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
teaentry = Entry(groceryframe, font=("times new roman", 15, "bold"), width=10, bd=5)
sugarlabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")
sugarentry.grid(row=4, column=1, pady=9, padx=10)
teaentry.insert(0, 0)

tealabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")
colddrinkframe = LabelFrame(
    productframe,
    text="Cold Drink",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    relief=GROOVE,
    bg="gray20",
)
teaentry.grid(row=5, column=1, pady=9)


mazzalabel = Label(
    colddrinkframe,
    text="Maaza",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
colddrinkframe.grid(row=0, column=2)
mazzaentry = Entry(colddrinkframe, font=("times new roman", 15, "bold"), width=10, bd=5)
mazzaentry.insert(0, 0)


pepsilabel = Label(
    colddrinkframe,
    text="Pepsi",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
pepsientry = Entry(colddrinkframe, font=("times new roman", 15, "bold"), width=10, bd=5)
mazzalabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")
mazzaentry.grid(row=0, column=1, pady=9, padx=10)
pepsientry.insert(0, 0)


Spritelabel = Label(
    colddrinkframe,
    text="Sprite",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
Spriteentry = Entry(
    colddrinkframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
pepsilabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")
pepsientry.grid(row=1, column=1, pady=9, padx=10)
Spriteentry.insert(0, 0)


Dewlabel = Label(
    colddrinkframe,
    text="Dew",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
Dewentry = Entry(colddrinkframe, font=("times new roman", 15, "bold"), width=10, bd=5)
Spritelabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")
Spriteentry.grid(row=2, column=1, pady=9, padx=10)
Dewentry.insert(0, 0)


frootilabel = Label(
    colddrinkframe,
    text="frooti",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
frootientry = Entry(
    colddrinkframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
Dewlabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")
Dewentry.grid(row=3, column=1, pady=9, padx=10)
frootientry.insert(0, 0)


cocacolalabel = Label(
    colddrinkframe,
    text="Coca cola",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cocacolaentry = Entry(
    colddrinkframe, font=("times new roman", 15, "bold"), width=10, bd=5
)
frootilabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")
frootientry.grid(row=4, column=1, pady=9, padx=10)
cocacolaentry.insert(0, 0)

cocacolalabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")
cocacolaentry.grid(row=5, column=1, pady=9, padx=10)

# Billing section
billframe = Frame(productframe, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3)

billarealabel = Label(
    billframe,
    text="Bill Area",
    font=("times new roman", 13, "bold"),
    bd=7,
    relief=GROOVE,
)
billarealabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# text area
textarea = Text(billframe, height=18, width=58, yscrollcommand=scrollbar.set)
textarea.pack()

# it is scroll bar
scrollbar.config(command=textarea.yview)

# bill menu frame
billmenuframe = LabelFrame(
    root,
    text="Bill Menu",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    relief=GROOVE,
    bg="gray20",
)
billmenuframe.pack()

# it is somatic price
cosmaticpricelabel = Label(
    billmenuframe,
    text="Cosmetic Price",
    font=("times new roman", 13, "bold"),
    bg="gray20",
    fg="white",
)
cosmaticpricelabel.grid(row=0, column=0, pady=9, sticky="w")
# it is cosmatic entry
cosmaticpriceentry = Entry(
    billmenuframe, font=("times new roman", 13, "bold"), width=10, bd=5
)
cosmaticpriceentry.grid(row=0, column=1, pady=9, padx=10)

# It is grocery price
grocerypricelabel = Label(
    billmenuframe,
    text="Grocery Price",
    font=("times new roman", 13, "bold"),
    bg="gray20",
    fg="white",
)
grocerypricelabel.grid(row=1, column=0, pady=9, sticky="w")

# grocery Entry
grocerypriceentry = Entry(
    billmenuframe, font=("times new roman", 13, "bold"), width=10, bd=5
)
grocerypriceentry.grid(row=1, column=1, pady=9)

# drinks label
drinkspricelabel = Label(
    billmenuframe,
    text="Cold drink Price",
    font=("times new roman", 13, "bold"),
    bg="gray20",
    fg="white",
)
drinkspricelabel.grid(row=2, column=0, pady=9, sticky="w")

# drinks Entry
drinkspriceentry = Entry(
    billmenuframe, font=("times new roman", 13, "bold"), width=10, bd=5
)
drinkspriceentry.grid(row=2, column=1, pady=9, padx=10)

# It is tax area

# it is somatic price
cosmatictaxlabel = Label(
    billmenuframe,
    text="Cosmetic Tax",
    font=("times new roman", 13, "bold"),
    bg="gray20",
    fg="white",
)
cosmatictaxlabel.grid(row=0, column=2, pady=9, sticky="w")
# it is cosmatic entry
cosmatictaxentry = Entry(
    billmenuframe, font=("times new roman", 13, "bold"), width=10, bd=5
)
cosmatictaxentry.grid(row=0, column=3, pady=9, padx=10)

# It is grocery price
grocerytaxlabel = Label(
    billmenuframe,
    text="Grocery tax",
    font=("times new roman", 13, "bold"),
    bg="gray20",
    fg="white",
)
grocerytaxlabel.grid(row=1, column=2, pady=9, sticky="w")

# grocery Entry
grocerytaxentry = Entry(
    billmenuframe, font=("times new roman", 13, "bold"), width=10, bd=5
)
grocerytaxentry.grid(row=1, column=3, pady=9)

# drinks label
drinkstaxlabel = Label(
    billmenuframe,
    text="Cold drink Tax",
    font=("times new roman", 13, "bold"),
    bg="gray20",
    fg="white",
)
drinkstaxlabel.grid(row=2, column=2, pady=9, sticky="w")

# drinks Entry
drinkstaxentry = Entry(
    billmenuframe, font=("times new roman", 13, "bold"), width=10, bd=5
)
drinkstaxentry.grid(row=2, column=3, pady=9, padx=10)


buttonframe = Frame(billmenuframe, bd=8, relief=GROOVE)
buttonframe.grid(row=0, column=4, rowspan=8)

totalbutton = Button(
    buttonframe,
    text="Total",
    font=("arial", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=10,
    command=total,
)
totalbutton.grid(row=0, column=0, pady=20, padx=5)

billbutton = Button(
    buttonframe,
    text="Bill",
    font=("arial", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=10,
    command=bill_area,
)
billbutton.grid(row=0, column=1, pady=20, padx=5)

Emailbutton = Button(
    buttonframe,
    text="Email",
    font=("arial", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=10,command=send_email
)
Emailbutton.grid(row=0, column=2, pady=20, padx=5)

printbutton = Button(
    buttonframe,
    text="Print",
    font=("arial", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=10,command=print_bill
)
printbutton.grid(row=0, column=3, pady=20, padx=5)


clearbutton = Button(
    buttonframe,
    text="Clear",
    font=("arial", 15, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=10,command=clear
)
clearbutton.grid(row=0, column=4, pady=20, padx=5)


root.mainloop()
