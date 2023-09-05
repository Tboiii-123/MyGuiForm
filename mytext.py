
"""
def Login():
    Fname=container.get()
    Lname=container1.get()
    Email=container2.get()
    DOB=container3.get()
    Mobile=container4.get()
    Password=container5.get()
    #formated string
    F='lawal'
    L='hussein'
    E='lawalhussein775@gmail.com'
    D='july,7,2007'
    M='09035014430'
    P='python'
    if Fname=='' and Lname=='' and Email=='' and  DOB=='' and Mobile=='' and Password=='':
        messagebox.showinfo('','FILL YOUR FORM PLEASE.......')
                
    elif Fname==f'{F}' and Lname==f'{L}' and Email==f'{E}' and DOB==f'{D}'  and Mobile==f'{M}'and Password==f'{P}':
        messagebox.showinfo('','LOGIN SUCCESSFUL')
       
    else:
        messagebox.showerror('','INCORRECT DETAILS')
def reset():
    container.delete(0,END)
    container1.delete(0,END)
    container2.delete(0,END)
    container3.delete(0,END)
    container4.delete(0,END)
    container5.delete(0,END)

"""
