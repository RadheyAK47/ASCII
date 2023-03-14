from tkinter import *
root=Tk()

root.title("ASCII")
root.geometry("400x500")
root.configure(background="#800237")

word=Entry(root)
word.place(relx=0.5,rely=0.2,anchor=CENTER)

label=Label(root,text="Name in ASCII : ",fg="#FFD700",bg="#800237")
label.place(relx=0.5,rely=0.3,anchor=CENTER)

label2=Label(root,text="",fg="#FFD700",bg="#800237")
label2.place(relx=0.5,rely=0.4,anchor=CENTER)

def conveter():
    inputword=word.get()
    for i in inputword:
        label2["text"]+=str(ord(i))+" "

btn=Button(root,text="ascii",command=conveter,bg="#FFD700",fg="black")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()