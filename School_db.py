from tkinter import *
import sqlite3
from tkinter import messagebox





root=Tk()
root.geometry('500x600')
def employee(b):
    data={
    'ID':b[0],
    
    'Name':b[1],
    'Age':b[2],
    'Email':b[3]
        }
    return data



def Add():
    a=sqlite3.connect('School_data.db')
    b=a.cursor()
    

    b.execute("""Create Table My_class(
        ID text,
        Name text,
        Age integer,
        Email text
                   )""")

   # b.execute("""INSERT INTO My_class
    #
     #           VALUES('{}','{}','{}')
      #      """.format(name_ent.get(),Age_ent.get,Email_ent.get()))

  #  b.execute("""DELETE FROM TABLE WHERE)


    a.commit()
    a.close()

    messagebox.showinfo('','DATA ADDED INTO DATA BASE')
    name_ent.delete(0,END)

    Age_ent.delete(0,END)
    Email_ent.delete(0,END)

    

def clear():
    name_ent.delete(0,END)
    Age_ent.delete(0,END)
    Email_ent.delete(0,END)
    


text=Label(root,text='My school form',font=('Helvetica',17))
text.pack()



name=Label(root,text=' Student Name :')
name.place(x=20,y=50)
name_ent=Entry(root)
name_ent.place(x=120,y=50)



Age=Label(root,text='Student Age :')
Age.place(x=20,y=100)
Age_ent=Entry(root)
Age_ent.place(x=120,y=100)


Email=Label(root,text='Stident Email :')
Email.place(x=20,y=150)

Email_ent=Entry(root)
Email_ent.place(x=120,y=150)



add=Button(root,text='ADD',width=30,bg='green',command=Add)
add.place(x=60,y=400)



cancel=Button(root,text='CANCEL',width=30,bg='RED',command=clear)
cancel.place(x=360,y=400)



root.mainloop()