from tkinter import *
import tkinter.messagebox
redg =Tk()
redg.title("Employee Registration Form")
redg.geometry('700x400')
redg.configure(background = "white")

label1=Label(redg ,text= "Employee Registration Form ", font=("bold", 30)).grid(row =0, column=2)
Firstname = Label(redg ,text = "First Name",width=20,font=("bold", 20)).grid(row = 1,column = 1)
LastName = Label(redg ,text = "Last Name",width=20,font=("bold", 20)).grid(row = 2,column = 1)
Address = Label(redg ,text = "Address",width=20,font=("bold", 20)).grid(row = 3,column = 1)
City = Label(redg ,text = "City",width=20,font=("bold", 20)).grid(row = 4,column = 1)
State= Label(redg ,text = "state",width=20,font=("bold", 20)).grid(row = 5,column = 1)
Country = Label(redg ,text = "Country",width=20,font=("bold", 20)).grid(row = 7,column = 1)
postal = Label(redg ,text = "Postal /zip Code",width=20,font=("bold", 20)).grid(row = 6,column = 1)
list1 = ['Pakistan','India','UK','Nepal','North America'];
c=StringVar()
droplist=OptionMenu(redg,c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.grid(row = 7,column = 2)
Mobile = Label(redg ,text = "Contact Number",width=20,font=("bold", 20)).grid(row = 8,column = 1)
Email = Label(redg ,text = "Email Id",width=20,font=("bold", 20)).grid(row = 9,column = 1)
Gender =Label(redg ,text = "Gender",width=20,font=("bold", 20)).grid(row = 10,column = 1)
var = IntVar()
Radiobutton(redg, text="Male",padx = 30, variable=var, value=1).grid(row = 10,column = 2)
Radiobutton(redg, text="Female",padx = 20, variable=var, value=2).grid(row = 10,column = 3)
Choose =Label(redg ,text = "Date Of Birth",width=20,font=("bold", 20)).grid(row = 11,column = 1)
label_12 = Label(redg, text="Programming",width=20,font=("bold", 20))
label_12.grid(row = 12,column = 1)
var1 = IntVar()
Checkbutton(redg, text="java", variable=var1).grid(row = 12,column = 2)
var2 = IntVar()
Checkbutton(redg, text="python", variable=var2).grid(row = 12,column = 3)


Firstname1 = Entry(redg).grid(row = 1,column = 2)
Lastna = Entry(redg).grid(row = 2,column = 2)
Adderss1=Entry(redg).grid(row = 3,column = 2)
city1=Entry(redg).grid(row = 4,column = 2)
state1=Entry(redg).grid(row = 5,column = 2)
postal1=Entry(redg).grid(row = 6,column = 2)
Email1 = Entry(redg).grid(row = 9,column = 2)
Mobile1 = Entry(redg).grid(row = 8,column = 2)
choose1 = Entry(redg).grid(row = 11,column = 2)


def onClick():
    tkinter.messagebox.showinfo("Congratulation", "Your Details Submitted  Successfully !")



Button(redg, text="Submit", command=onClick,width=20,bg='red',fg='white').grid(row = 14,column=2)
redg.mainloop()

