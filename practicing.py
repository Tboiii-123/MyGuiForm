from tkinter import *

root=Tk()

def submit():
	message=entry.get()
	text.insert(END,'\n'+message)
	




root.geometry('500x300')
root.title('My practicing page')



text=Label(root,text='My practicing page',bg='red')

text.place(x=10,y=30)


text=Text(root,bg='green',fg='white',height=10,width=100)
text.place(x=10,y=80)


entry=Entry(root,width=40)

entry.place(x=30,y=280)

count=0
while count<3:
    btn=Button(root, text='click',width=70,command=submit)

    btn.place(x=30,y=300)
    count+=1
root.mainloop()
