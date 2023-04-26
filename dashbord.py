from tkinter import*
from PIL import Image,ImageTk
from Employee import employee
class erp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1580x780+0+0")
        self.root.title("ERP system  ||  Developed by Tushar")
        self.root.config(bg="white")
        
        #title
        self.icon_title=Image.open("logoErp.jpeg")
        self.icon_title=self.icon_title.resize((70,70),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root,text="UNITY INDUSTRIAL AUTOMATION Pvt Ltd.",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#4A4A70",fg="white",anchor="w",padx=20).place(x=0,y=-4,relwidth=1,height=80)
        
        #button
        btn_Logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#D2D2B4",fg="black",cursor="hand2",padx=10,pady=20,anchor=CENTER).place(x=1370,y=10,height=50,width=140)
        
        #clock
        self.lbl_clock=Label(self.root,text="Welcome to Erp system\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="grey",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #left_Menu
        self.menu_logo=Image.open("MENUicon.jpg")
        self.menu_logo=self.menu_logo.resize((300,300),Image.ANTIALIAS)
        self.menu_logo=ImageTk.PhotoImage(self.menu_logo)
    
        left_menu=Frame(self.root,bd=1,relief=RIDGE,bg="white")
        left_menu.place(x=0,y=102,width=280,height=610)
        
        lbl_menulogo=Label(left_menu,image=self.menu_logo)
        lbl_menulogo.pack(side=TOP,fill=X)
        
        lbl_menu=Label(left_menu,text="Menu",font=("times new roman",20),bg="#8A8A2B")
        lbl_menu.pack(side=TOP,fill=X)
        
        
        self.icon_side=Image.open("side.png")
        self.icon_side=self.icon_side.resize((20,20),Image.ANTIALIAS)
        self.icon_side=ImageTk.PhotoImage(self.icon_side)
        
        btn_HR=Button(left_menu,text="HRM",font=("times new roman",15,"bold"),image=self.icon_side,compound=LEFT,padx=6,anchor="w",bg="white",cursor="hand2",bd=2).pack(side=TOP,fill=X)
        btn_CRM=Button(left_menu,text="CRM",font=("times new roman",15,"bold"),image=self.icon_side,compound=LEFT,padx=6,anchor="w",bg="white",cursor="hand2",bd=2).pack(side=TOP,fill=X)
        btn_EMPLOYEE=Button(left_menu,text="EMPLOYEE",command=self.employee,font=("times new roman",15,"bold"),image=self.icon_side,compound=LEFT,padx=6,anchor="w",bg="white",cursor="hand2",bd=2).pack(side=TOP,fill=X)
        btn_ORDER=Button(left_menu,text="ORDER MANAGEMENT",font=("times new roman",15,"bold"),image=self.icon_side,compound=LEFT,padx=4,anchor="w",bg="white",cursor="hand2",bd=2).pack(side=TOP,fill=X)
        btn_MANUFACTURE=Button(left_menu,text="MANUFACTURING",font=("times new roman",15,"bold"),image=self.icon_side,compound=LEFT,padx=6,anchor="w",bg="white",cursor="hand2",bd=2).pack(side=TOP,fill=X)
        btn_ACCOUNT=Button(left_menu,text="ACCOUNTING",font=("times new roman",15,"bold"),image=self.icon_side,compound=LEFT,padx=6,anchor="w",bg="white",cursor="hand2",bd=2).pack(side=TOP,fill=X)
        btn_EXIT=Button(left_menu,text="EXIT",font=("times new roman",15,"bold"),image=self.icon_side,compound=LEFT,padx=6,anchor="w",bg="white",cursor="hand2",bd=2).pack(side=TOP,fill=X)
        
        #____content____
        self.lbl_Emp=Label(self.root,text="Total Employee\n[ 0 ]",font=("goudy old style",20,"bold"),bg="#33bbf9",fg="white",bd=4,relief=RIDGE)
        self.lbl_Emp.place(x=350,y=150,height=150,width=300)
        
        self.lbl_Ord=Label(self.root,text="Total Order\n[ 0 ]",font=("goudy old style",20,"bold"),bg="#33bbf9",fg="white",bd=4,relief=RIDGE)
        self.lbl_Ord.place(x=750,y=150,height=150,width=300)
        
        self.lbl_Ord=Label(self.root,text="Total Order\n[ 0 ]",font=("goudy old style",20,"bold"),bg="#33bbf9",fg="white",bd=4,relief=RIDGE)
        self.lbl_Ord.place(x=750,y=150,height=150,width=300)
        
        
        #____footer___
        lbl_footer=Label(self.root,text="ERP-Enterprise Resource Plannig || Developed by UIAPL Team\nFor any Technical Issue Contact:- 74xxxxxx84",padx=5,pady=14,anchor=CENTER,font=("times new roman",12),bg="grey",fg="white").pack(side=BOTTOM,fill=X)
    
    
    #_____________________Employee_page________________________________
    def employee(self):
        self.new_wind=Toplevel(self.root)
        self.new_obj=employee(self.new_wind)
        
        
        
root=Tk()
obj=erp(root)
root.mainloop()
