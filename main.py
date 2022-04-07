from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
root = Tk()
root.title("Password Generator")
root.geometry("500x500")

# LOGO
# program_logo = PhotoImage(file = "logo.png")
# root.iconphoto(False, program_logo)

# Heading Frame
frame_head = Frame(root)
frame_head.pack()
head_label = Label(frame_head, text="Password Generator",padx=15,pady=15,font="SegoeUI 14",fg="red")
head_label.grid(row=1,column=1,pady=10,padx=5,columnspan=3)

# FUNCTIONS
def gen_fun():
    pw_entry.delete(0,END)
    pw_lenth = int(my_entry.get())
    my_password = ''
    for i in range(pw_lenth):
        my_password+= chr(randint(33, 126))
    pw_entry.insert(0,my_password)

def cpy_fun():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Password Generator","Password Copied")

# Lable 1

lf = LabelFrame(root, text="Enter Number - Length")
lf.pack(pady=20)
# ENTER BOX
my_entry = Entry(lf, font=("Arial", 18))
my_entry.pack(pady=20, padx=20)

# Lable 2

lf2 = LabelFrame(root, text="Your Password")
lf2.pack(pady=20)
# ENTER BOX
pw_entry = Entry(lf2, font=("Arial", 18))
pw_entry.pack(pady=20, padx=20)

# BUTTONS BOX
frame_button = Frame(root)
frame_button.pack(pady=20)
gen_btn = ttk.Button(frame_button,text="Generate Password",command=gen_fun)

gen_btn.grid(row=0,column=0,padx=10)

cpy_btn = ttk.Button(frame_button,text="Copy Password",command=cpy_fun)

cpy_btn.grid(row=0,column=1,padx=10)


root.mainloop()
