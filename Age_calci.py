from tkinter import*
root = Tk()
def Clear(Day,Month,Year):
    Day.delete(0,END)
    Month.delete(0,END)
    Year.delete(0,END)
def Print_Age(year,month,date):
    Y = Label(root,text ="Your Age :",font = ('Times New Roman',25,'bold'),bg = "yellow",fg = "Blue")
    Y.place(x=1,y=380)
    Age = Label(root,text = "\t"+year+" Years "+month+(" Months " if(month!=str(1)) else " month ")
                +date+(" days" if(date!=str(1)) else " day"),font = ('Cambria',20,'bold'),bg = "yellow",fg = "black")
    Age.place(x=1,y=420)
def Calculate(b_date,b_month,b_year):
    #print(date.today())
    from datetime import date
    today = str(date.today())
    list_today = today.split("-")
    c_date = int(list_today[2])
    c_month = int(list_today[1])
    c_year = int(list_today[0])
    b_date = int(b_date.get())
    b_month = int(b_month.get())
    b_year = int(b_year.get())
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(b_date>c_date):
        c_month=c_month-1
        c_date=c_date+month[b_month-1]
    if(b_month>c_month):
        c_year=c_year-1
        c_month=c_month+12
    date = str(c_date-b_date)
    month = str(c_month-b_month)
    year = str(c_year-b_year)
    #print(year+" years "+month+" months "+date+" days")
    X = Label(root,text = "Today's date :",font = ('Cambria',20,'bold'),bg = "yellow",fg = "green")
    X.place(x=1,y=310)
    D = Label(root,text = today,font = ('Cambria',20,'bold'),
              anchor = CENTER,bg = "yellow",fg = "Black")
    D.place(x=135,y=340)
    Print_Age(year,month,date)
root.geometry("500x500")
root.title("Age-Calci")
root.configure(bg = "yellow")
new = Label(root,text = "Age Calculator",font = ('Times New Roman',50,'bold'),anchor = CENTER,bg = "blue",fg = "yellow",width = 20)
new.pack()
Birthdate = Label(root,text = "BirthDate :",font = ('Cambria',15,'bold'),bg = 'yellow')
Birthdate.place(x=50,y=100)
Birthmonth = Label(root,text = "BirthMonth :",font = ('Cambria',15,'bold'),bg = 'yellow')
Birthmonth.place(x=50,y=150)
Birthyear = Label(root,text = "BirthYear :",font = ('Cambria',15,'bold'),bg = 'yellow')
Birthyear.place(x=50,y=200)
Day = StringVar()
Month = StringVar()
Year = StringVar()
Birthdate_txt = Entry(root,textvariable = Day,font = ('Arial',12,'bold'),bg = "white",width = '20')
Birthdate_txt.place(x=180,y=105)
Birthday_txt = Entry(root,textvariable = Month,font = ('Arial',12,'bold'),width = '20')
Birthday_txt.place(x=180,y=155)
Birthyear_txt = Entry(root,textvariable = Year,font = ('Arial',12,'bold'),width = '20')
Birthyear_txt.place(x=180,y=205)
Cal = Button(root,text = "CALCULATE",command = lambda:Calculate(Birthdate_txt,Birthday_txt,Birthyear_txt),bg = 'light green',
             fg = 'black',font = ("Cambria",15,'bold'),anchor= CENTER,borderwidth = 5)
Cal.place(x = 300,y = 255)
Clr = Button(root,text = "CLEAR",command = lambda:Clear(Birthdate_txt,Birthday_txt,Birthyear_txt),bg = 'light blue',fg = 'black',
             font = ("Cambria",15,'bold'),anchor= CENTER,borderwidth = 5)
Clr.place(x = 20,y = 255)
root.mainloop()
