from tkinter import *
from phone_list  import *
import webbrowser


def whichSelected() :
	print("At %s of %d" % (select.curselection(), len(phonelist)))
	return int(select.curselection()[0])

def add():
	phonelist.append ([nameVar.get(), phoneVar.get()])
	setSelect()

def update() :
	phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
	setSelect()

def delete():
	del phonelist[whichSelected()]
	setSelect()

def load() :
	name, phone, address, email = phonelist[whichSelected()]
	nameVar.set(name)
	phoneVar.set(phone)
	addressVar.set(address)
	emailVar.set(email)
    
def callback():
 	webbrowser.open_new(r"https://www.google.com/maps/place")
 	setSelect()

def Email():
        mail = Tk()
        mail.title("Send Email")
        Label(mail, text="To: ").grid(row=0)
        Label(mail, text="Subject: ").grid(row=1)
        Label(mail, text="Compose: ").grid(row=2)
        mail_entry1 = Entry(mail)
        mail_entry2 = Entry(mail)
        mail_entry3 = Entry(mail)
        mail_entry1.grid(row=0, column=1)
        mail_entry2.grid(row=1, column=1)
        mail_entry3.grid(row=2, column=1)
        send_mail_button = Button(mail, text="Send",command=mail.destroy)
        send_mail_button.grid(row=3)


def makeWindow () :
	global nameVar, phoneVar, addressVar, emailVar, select, link
	win = Tk()


	frame1 = Frame(win)
	frame1.pack()

	Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
	nameVar = StringVar()
	name = Entry(frame1, textvariable=nameVar)
	name.grid(row=0, column=1, sticky=W)
    
	Label(frame1, text="Address").grid(row=1, column=0, sticky=W)
	addressVar = StringVar()
	address = Entry(frame1, textvariable=addressVar)
	address.grid(row=1, column=1, sticky=W)
	map_button = Button(frame1, text="Map", fg="green", command=callback, cursor="hand2").grid(row=1, column=10)
    
	Label(frame1, text="Phone").grid(row=3, column=0, sticky=W)
	phoneVar = StringVar()
	phone = Entry(frame1, textvariable=phoneVar)
	phone.grid(row=3, column=1, sticky=W)
    
	Label(frame1, text="Email").grid(row=2, column=0, sticky=W)
	emailVar = StringVar()
	email = Entry(frame1, textvariable=emailVar)
	email.grid(row=2, column=1, sticky=W)
	mail_button = Button(frame1, text="Email", fg="green", command=Email, cursor="hand2").grid(row=2, column=10)
    
   

	frame2 = Frame(win)
	frame2.pack()
	add_button = Button(frame2, text="Add", fg="green", command=add)
	update_button = Button(frame2, text="Update", fg="green", command=update)
	delete_button = Button(frame2, text="Delete", fg="red", command=delete)
	load_button = Button(frame2, text="Load", fg="green",  command=load) 
	send_mail_button = Button(frame2,text="Send Email", fg="green", command=callback)
	add_button.pack(side=LEFT); update_button.pack(side=LEFT)
	delete_button.pack(side=LEFT); load_button.pack(side=LEFT)
	frame3 = Frame(win)       
	frame3.pack()
	scroll = Scrollbar(frame3, orient=VERTICAL)
	select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
	scroll.config (command=select.yview)
	scroll.pack(side=RIGHT, fill=Y)
	select.pack(side=LEFT,  fill=BOTH, expand=1)
	return win

def setSelect() :
	phonelist.sort()
	select.delete(0,END)
	for name,phone,email,address in phonelist :
		select.insert (END, name)

win = makeWindow()
setSelect ()
win.mainloop()
