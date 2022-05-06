from tkinter import *
from tkinter import ttk
from database import Database
from tkinter import messagebox

db = Database('Empolyee.db')
app = Tk()
app.title('Empolyee Management System')
app.geometry('1350x515+0+20')
app .resizable(FALSE, FALSE)
app.iconbitmap('E:\\Employee\\employee.ico')
app.config(bg='#7F8C8D')


nme = StringVar()
eml = StringVar()
phon = StringVar()
age = StringVar()
job = StringVar()
grnd = StringVar()


# frame for entries======
fentry = Frame(app, bg='#BFC9CA', width=360, height=515)
fentry.place(x=0, y=0)
title1 = Label(fentry, text='Company Name', font=(
    'tajawal', 20, 'bold'), bg="#BFC9CA", fg="#2C3E50")
title1.place(x=20, y=5)
# head====================


def hide():
    app.geometry('360x515')


def show():
    app.geometry('1350x515+0+20')


btn1 = Button(fentry, text='SHOW', bg="#2C3E50",
              fg="#BFC9CA", font=(
                  'tajawal', 10, 'bold'), activebackground='#ABB2B9', width=7, height=1, activeforeground='#2C3E50', cursor='hand2', bd=1, relief=SOLID, command=show)
btn1.place(x=300, y=10)
btn2 = Button(fentry, text='HIDE', bg="#2C3E50", fg="#BFC9CA", font=(
    'tajawal', 10, 'bold'), activebackground='#ABB2B9', width=5, height=1, activeforeground='#2C3E50', cursor='hand2', bd=1, relief=SOLID, command=hide)
btn2.place(x=250, y=10)


# fuctions====================

def getdata(event):
    markedrow = tablehead.focus()
    information = tablehead.item(markedrow)
    global rows
    rows = information['values']
    nme.set(rows[1])
    eml.set(rows[2])
    age.set(rows[3])
    phon.set(rows[4])
    grnd.set(rows[6])
    job.set(rows[7])
    txtadd.delete(1.0, END)
    txtadd.insert(END, rows[5])


def displayall():
    tablehead.delete(*tablehead.get_children())
    for row in Database.display(db):
        tablehead.insert("", END, values=row)


def clr():
    nme.set("")
    eml.set("")
    age.set("")
    phon.set("")
    grnd.set("")
    job.set("")
    txtadd.delete(1.0, END)


def add_details():
    if entname.get() == " " or entem.get() == " " or entage.get() == "" or entjob.get() == "" or entph.get() == "" or combgen.get() == "" or txtadd.get(1.0, END) == "":
        messagebox.showerror("ALERT ERROR !", "Plase Make Sure For Your Data")
        return
    db.insert(
        entname.get(),
        entem.get(),
        entage.get(),
        entph.get(),
        txtadd.get(1.0, END),
        combgen.get(),
        entjob.get()
    )
    messagebox.showinfo('Done', 'Add New Data')
    displayall()
    clr()


def dele():
    db.remove(rows[0])
    clr()
    displayall()


def update_details():
    if entname.get() == " " or entem.get() == " " or entage.get() == "" or entjob.get() == "" or entph.get() == "" or combgen.get() == "" or txtadd.get(1.0, END) == "":
        messagebox.showerror("ALERT ERROR !", "Plase Make Sure For Your Data")
        return
    db.update(rows[0],
              entname.get(),
              entem.get(),
              entage.get(),
              entph.get(),
              txtadd.get(1.0, END),
              combgen.get(),
              entjob.get()
              )
    messagebox.showinfo('Done', 'Update New Data')
    displayall()
    clr()


# body=====================
# for name
labl1 = Label(fentry, text='Name', font=(
    'tajawal', 14, 'bold'), fg='#283747', bg="#BFC9CA")
labl1.place(x=20, y=70)
entname = Entry(fentry, width=20, font=(
    'tajawal', 12), textvariable=nme)
entname.place(x=90, y=75)
# for email
labl2 = Label(fentry, text='Email', font=(
    'tajawal', 14, 'bold'), fg='#283747', bg="#BFC9CA")
labl2.place(x=20, y=110)
entem = Entry(fentry, width=20, font=(
    'tajawal', 12), textvariable=eml)
entem.place(x=90, y=110)
# forgender
labl3 = Label(fentry, text='Gender', font=(
    'tajawal', 14, 'bold'), fg='#283747', bg="#BFC9CA")
labl3.place(x=20, y=150)
combgen = ttk.Combobox(fentry, textvariable=grnd, state='readonly', font=(
    'tajawal', 12), width=18)
combgen['values'] = ('Male', 'Famle')
combgen.place(x=90, y=150)
# for job
labl3 = Label(fentry, text='Job', font=(
    'tajawal', 14, 'bold'), fg='#283747', bg="#BFC9CA")
labl3.place(x=20, y=190)
entjob = Entry(fentry, width=20, font=(
    'tajawal', 12), textvariable=job)
entjob.place(x=90, y=190)

# for age
labl5 = Label(fentry, text='Age', font=(
    'tajawal', 14, 'bold'), fg='#283747', bg="#BFC9CA")
labl5.place(x=20, y=230)
entage = Entry(fentry, width=20, font=(
    'tajawal', 12), textvariable=age)
entage.place(x=90, y=230)
# for phone
labl6 = Label(fentry, text='Phone', font=(
    'tajawal', 14, 'bold'), fg='#283747', bg="#BFC9CA")
labl6.place(x=20, y=270)
entph = Entry(fentry, width=20, font=(
    'tajawal', 12), textvariable=phon)
entph.place(x=90, y=270)
# for address
labl4 = Label(fentry, text='Address', font=(
    'tajawal', 14, 'bold'), fg='#283747', bg="#BFC9CA")
labl4.place(x=20, y=300)
txtadd = Text(fentry, width=40, height=3, font=('tajawal', 10))
txtadd.place(x=20, y=330)

# frame for buttons ==========
fbtn = Frame(fentry, bg='#BFC9CA', width=340, height=100)
fbtn.place(x=10, y=400)
# add details
btnadd = Button(fbtn, text='Add Details', width=15, height=1, bg='#2E4053', font=('tajawal', 12, 'bold'), command=add_details
                )
btnadd.place(x=20, y=5)
# edit details
btnedit = Button(fbtn, text='Edit Details', width=15, height=1, bg='#2E4053', font=('tajawal', 12, 'bold'), command=update_details
                 )
btnedit.place(x=180, y=5)
# delete details
btndel = Button(fbtn, text='Delete Details', width=15, height=1, bg='#2E4053', font=('tajawal', 12, 'bold'), command=dele
                )
btndel.place(x=180, y=50)
# reset
btnres = Button(fbtn, text='Reset', width=15, height=1, bg='#2E4053', font=('tajawal', 12, 'bold'), command=clr
                )
btnres.place(x=20, y=50)

# frame for table
ftb = Frame(app, bg='#7F8C8D', width=990, height=615)
ftb.place(x=360, y=0)
# style for table heading
styletable = ttk.Style()
styletable.configure('styletable.Treeview', font=('tajawal', 14), rowheight=70)
styletable.configure('styletable.Treeview.Heading', font=('tajawal', 14))
# style for head
tablehead = ttk.Treeview(ftb, columns=(
    1, 2, 3, 4, 5, 6, 7, 8), style='styletable.Treeview')
tablehead.heading('1', text='Id')
tablehead.column('1', width=20)
tablehead.heading('2', text='Name')
tablehead.column('2', width=150)
tablehead.heading('3', text='Email')
tablehead.column('3', width=150)
tablehead.heading('4', text='Age')
tablehead.column('4', width=20)
tablehead.heading('5', text='Phone')
tablehead.column('5', width=110)
tablehead.heading('6', text='Address')
tablehead.column('6', width=150)
tablehead.heading('7', text='Gender')
tablehead.column('7', width=50)
tablehead.heading('8', text='job')
tablehead.column('8', width=40)
tablehead['show'] = 'headings'

tablehead.bind("<ButtonRelease-1>", getdata)
tablehead.place(x=0, y=0, width=990, height=615)


displayall()

app.mainloop()
