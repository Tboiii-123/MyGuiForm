from tkinter import*
import os
from tkinter import messagebox
import re
import sqlite3

def donothing():
    print("ok i won't")

def file1():
    z=open('mbox.txt')
    for n in z:
        print(n)

def open1():
    
    x=r'C:\Users\HP\Desktop\Python files' 
    new=x+"\\practice\\"
    if not os.path.exists(new):
        os.mkdir(new)
        
def location():
    print(os.getcwd())

def employee(b):
    data={
    'FID':b[0],
    'Firstname':b[1],
    'Lastanme':b[2],
    'Email':b[3],
    'DOB':b[4],
    'Mobile':b[5],
    'Password':b[6]
        }
    return data

def sqlite():
    conn=sqlite3.connect('Login_form.db')
    b=conn.cursor()

    #b.execute("""CREATE TABLE Form(
      #  FID integer,
     #   Firstname text,
    #    Lastname text,
    #    Email text,
    #    DOB text,
       # Phone_no number,
      #  Password text
      #  )""")
        

    # b.execute("""INSERT INTO Form 
    #         (Firstname,Lastname,Email,DOB,Phone_no,Password)
    #         VALUES('{}','{}','{}','{}','{}','{}')
    #         """.format(container.get(),container1.get(),container2.get(),container3.get(),container4.get(),container5.get()))
    # conn.commit()
    # conn.close()
    
    # messagebox.showinfo('','DATA ADDED TO THE DATABASE')
    
    # container.delete(0,END)
    # container1.delete(0,END)
    # container2.delete(0,END)
    # container3.delete(0,END)
    # container4.delete(0,END)
    # container5.delete(0,END)

    b.execute('SELECT Email AND Password from Form where FID>1')
    a =b.fetchall()
    for i in a:
        print(i)
        
    conn.commit()
    conn.close()

root=Tk()
root.title('My project')
menu=Menu(root)
root.geometry('600x600')
root.config(menu=menu)


subMenu=Menu(menu)

menu.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label='open',command=open1)
subMenu.add_command(label='mbox_file',command=file1)
subMenu.add_separator()
subMenu.add_command(label='Exist',command=quit)


editMenu=Menu(menu)
menu.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='redo',command=donothing)

Shellmenu=Menu(menu)
menu.add_cascade(label='Shell',menu=Shellmenu)
Shellmenu.add_command(label='location',command=location)

Debugmenu=Menu(menu)
menu.add_cascade(label='calculations',menu=Debugmenu)
Debugmenu.add_command(label='calculator')



optionmenu=Menu(menu)
menu.add_cascade(label='Options',menu=optionmenu)
optionmenu.add_command(label='Zoom height')

windowmenu=Menu(menu)
menu.add_cascade(label='Window',menu=windowmenu)
windowmenu.add_command(label='About')
windowmenu.add_separator()
windowmenu.add_command(label='Online')
windowmenu.add_command(label='Offline')

Title=Label(text='Your Personal Form',font=('Helvetica',30),bg='yellow')
Title.pack(side=TOP)



Fname=Label(root,text='First Name',font=('Helvetica',11))
Fname.place(x=150,y=70)
container=Entry(root,bd=3)
container.place(x=240,y=77)




Lname=Label(root,text='Last Name',font=('Helvetica',11))
Lname.place(x=440,y=70)
container1=Entry(root,bd=3)
container1.place(x=520,y=70)


Email=Label(root,text='Email',font=('Helvetica',11))
Email.place(x=160,y=130)
container2=Entry(root,bd=3,width=54)
container2.pack()
container2.place(x=240,y=130)





DOB=Label(root,text='DOB',font=('Helvetica',11))
DOB.place(x=150,y=190)
container3=Entry(root,bd=3,width=37)
container3.place(x=240,y=190)


Gender=Label(root,text='Gender',font=('Helvetica',11))
Gender.place(x=150,y=235)

Male=Radiobutton(root,text='Male',font=('Helvetica',11))
Male.place(x=240,y=235)


Female=Radiobutton(root,text='Female',font=('Helvetica',11))
Female.place(x=360,y=235)



Mobile=Label(root,text='Phone no',font=('Helvetica',11))
Mobile.place(x=150,y=290)
container4=Entry(root,bd=3)
container4.place(x=240,y=293)

Password=Label(text='Password',font=('Helvetica',11))
Password.place(x=150,y=350)
container5=Entry(root,bd=3)
container5.place(x=240,y=353)


Login=Button(root,text='SUBMIT',width=15,height=2,bg='green',command=sqlite,relief='raised')
Login.place(x=180,y=450)


button=Button(root,text="CANCEL",bg="RED",fg='white',width=15,height=2,cursor="target",command=quit)
button.place(x=380,y=450)

Reset=Button(root,text="RESET",bg="blue",width=15,height=2)
Reset.place(x=580,y=450)



status=Label(root,text='Forms preparing.....',bd=5,relief='raised')
status.pack(side=BOTTOM,fill=X)



Fname=container.get()
Lname=container1.get()
Email=container2.get()
DOB=container3.get()
Mobile=container4.get()
Password=container5.get()
root.mainloop()
