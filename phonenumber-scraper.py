import os
import phonenumbers as a
from phonenumbers import carrier as b
from tkinter import*
from tkinter import messagebox as msg
import phonenumbers as pn
from phonenumbers import*
from phonenumbers.carrier import name_for_number
top= Tk()
top.title("Phone number scraper")
top.geometry("500x200")
k = Label(text="Enter the phone number with country code",font="40")
e = Entry(bd=5, font="36")
def main():
	try:
		device = str(name_for_number(a.parse(e.get(),None),"en"))
		msg.showinfo("Carrier",device)
	except:
		msg.showerror("Carrier","Try Again with - +<countrycode><yournumber>\n eg.= +919388*****")
bb = Button(text="Scrap",command=main,relief="groove",activebackground="black", activeforeground="white",background="white",font=36)

k.place(x=10,y=20)
e.place(x=60,y=50)
bb.place(x=110,y=100)
top.mainloop()