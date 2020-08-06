from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class loginsys:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System By Raj")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #Image
        self.phone_image=ImageTk.PhotoImage(file="image/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=250,y=-50)
        #login frames
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=1000,y=90,width=350,height=460)
        title=Label(login_frame,text="Logic System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lbl_user=Label(login_frame,text="Username",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()

        txt_username=Entry(login_frame,textvariable=self.username,font=('times new roman',15),bg='#ECECEC').place(x=50,y=140,width=250)
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=('times new roman',15),bg='#ECECEC').place(x=50,y=240,width=250)
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        hr=Label(login_frame,bg="lightgray").place(x=50,y=380,width=250,height=2)
        hr=Label(login_frame,bg="lightgray").place(x=50,y=380,width=250,height=2)
        or_=Label(login_frame,text="OR",fg="lightgray",bg="white",font=('times new roman',15,"bold")).place(x=150,y=355)
        btn_forg=Button(login_frame,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0).place(x=100,y=400)

        #frame2
        regis_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        regis_frame.place(x=1000, y=600, width=350, height=60)
        lgl_reg=Label(regis_frame,text="Don't have an account",font=("time new roman",13),bg="white").place(x=45,y=20)
        btn_sig=Button(regis_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0).place(x=200,y=17)


        #aniamtion
        self.a1=ImageTk.PhotoImage(file="image/a1.png")
        self.a2 = ImageTk.PhotoImage(file="image/a2.png")
        self.a3 = ImageTk.PhotoImage(file="image/a3.png")
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=548,y=78,width=370,height=720)
        self.animate()
    def animate(self):
        self.a=self.a1
        self.a1=self.a2
        self.a2=self.a3
        self.a3=self.a
        self.lbl_change_image.config(image=self.a)
        self.lbl_change_image.after(2000,self.animate)






    def login(self):
        if self.username.get()=="" or self.password=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.username.get()!="Abhishek" or self.password.get()!="123456":
            messagebox.showerror("Error","Invalid Username or Password\n Try Again")
        else:
            messagebox.showinfo("information",f"welcome :{self.username.get()}\nYour Password:{self.password.get()} ")








root=Tk()
obj=loginsys(root)
root.mainloop()