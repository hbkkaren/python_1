from tkinter import *


def insert_data():
    print("insert_data called")

def read_data():
    print("read_data called")

def update_data():
    print("update_data called")

def delete_data():
    print("delete_data called")
    

root = Tk()

root.geometry("500x500")
root.title("CRUD app")

l_id = Label(root, text = "ID",font = ("Arial, 15"))
l_id.place(x = 50 , y = 50)
l_fname = Label(root, text = "FULL NAME",font = ("Arial, 15"))
l_fname.place(x = 50 , y = 110)

l_lname = Label(root, text = "LAST NAME",font = ("Arial, 15"))
l_lname.place(x = 50 , y = 170)

l_email = Label(root, text = "EMAIL",font = ("Arial, 15"))
l_email.place(x = 50 , y = 230)


l_mobile = Label(root, text = "MOBILE NO.",font = ("Arial, 15"))
l_mobile.place(x = 50 , y = 290)


e_id = Entry(root)
e_id.place(x = 200, y = 50)

e_fname = Entry(root)
e_fname.place(x = 200, y = 110)

e_lname = Entry(root)
e_lname.place(x = 200, y = 170)


e_email = Entry(root)
e_email.place(x = 200, y = 230)


e_mobile = Entry(root)
e_mobile.place(x = 200, y = 290)



insert = Button(text = "INSERT",font =("Arial 15"),bg = "Black", fg = "white", command = insert_data)
insert.place(x = 20 , y= 400)

read = Button(text = "READ",font =("Arial  15"),bg = "Black", fg = "white", command = read_data)
read.place(x = 110 , y= 400)

update = Button(text = "UPDATE",font =("Arial  15"),bg = "Black", fg = "white",command = update_data)
update.place(x =200 , y= 400)

delete = Button(text = "DELETE",font =("Arial  15"),bg = "Black", fg = "white",command = delete_data)
delete.place(x = 309 , y= 400)

