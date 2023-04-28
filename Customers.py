from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class customer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x550+300+150")
        self.root.title("ERP system  ||  Developed by Tushar")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #All variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_empid=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_aadhar=StringVar()
        self.var_pan=StringVar()
        
        #____Title_Customer____
        cust_lbl=Label(self.root,text="Customer Details",font=("goudy old style",25,'bold'),bg="#8A8A2B",fg='white').pack(side=TOP,fill=X)
        
        #___content_emp______row1
        name_lbl=Label(self.root,text="Full Name",font=("times new roman",15),bg="white").place(x=50,y=100)
        name_txt=Entry(self.root,font=("times new roman",15),bg="lightyellow").place(x=150,y=100)
        
        #______row2_________
        
        email_lbl=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=50,y=170)
        email_txt=Entry(self.root,font=("times new roman",15),bg="lightyellow").place(x=150,y=170)
        
        #_____row3_______
        contact_lbl=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=50,y=240)
        contact_txt=Entry(self.root,font=("times new roman",15),bg="lightyellow").place(x=150,y=240)
        
        #____row4_______
        Addr_lbl=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=320)
        self.address_txt=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.address_txt.place(x=150,y=320,width=200,height=90)
        
        
        #_______row5_______
        Project_lbl=Label(self.root,text="Projects",font=("times new roman",15),bg="white").place(x=50,y=450)
        project_txt=Entry(self.root,font=("times new roman",15),bg="lightyellow").place(x=150,y=450)
        
        #______Customer_Table_______
        cust_frame=Frame(self.root,bd=3,relief=RIDGE)
        cust_frame.place(x=400,y=100,height=300,width=750)
        
        scrollX=Scrollbar(cust_frame,orient=HORIZONTAL)
        scrollY=Scrollbar(cust_frame,orient=VERTICAL)
        
        
        #customer table info
        self.customerTable=ttk.Treeview(cust_frame,columns=('name','email','contact','addr','projects'),yscrollcommand=scrollY.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.customerTable.xview)
        scrollY.config(command=self.customerTable.yview)
        self.customerTable.heading('name',text='Name')
        self.customerTable.heading('email',text='Email')
        self.customerTable.heading('contact',text='Contact')
        self.customerTable.heading('addr',text='Address')
        self.customerTable.heading('projects',text='Projects')
        
        self.customerTable["show"]="headings"
        self.customerTable.column('name',width=100)
        self.customerTable.column('email',width=100)
        self.customerTable.column('contact',width=100)
        self.customerTable.column('addr',width=100)
        self.customerTable.column('projects',width=100)
        self.customerTable.pack(fill=BOTH,expand=1)
        
        #Buttons
        btn_clear=Button(self.root,text="Clear",bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=400,y=450,width=100,height=25)
        btn_save=Button(self.root,text="Save",bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=550,y=450,width=100,height=25)
        btn_update=Button(self.root,text="Update",bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=700,y=450,width=100,height=25)
        btn_delete=Button(self.root,text="Delete",bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=850,y=450,width=100,height=25)
        
        
        
        
        
        
        

        
        
  
        
        
    
    
        
        

if __name__=="__main__":
    root=Tk()
    obj=customer(root)
    root.mainloop()

        