from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class employee:
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
        
        #____searchFrame____________
        searchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",15,"bold"),relief=RIDGE,bd=2)
        searchFrame.place(x=250,y=20,width=700,height=70)
        
        #____OPTIONS__________
        option_box=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Name","Email","Contact"),state="readonly",justify=CENTER,font=("goudy old style",11))
        option_box.place(x=10,y=10,width=180)
        option_box.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,bg="lightyellow",font=("goudy old style",15))
        txt_search.place(x=200,y=10)
        
        btn_search=Button(searchFrame,text="Search",bg="green",fg="white",font=("goudy old style",14,"bold")).place(x=410,y=10,width=150,height=25)
        
        #____Title_emp____
        emp_lbl=Label(self.root,text="Employee Details",font=("goudy old style",15,'bold'),bg="#45458B",fg='white').place(x=80,y=100,width=1000)
        
        #___content_emp______row1
        empid_lbl=Label(self.root,text="Employee Id",font=("times new roman",15),bg="white").place(x=80,y=150)
        gender_lbl=Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=450,y=150)
        contact_lbl=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=800,y=150)
        
        empid_txt=Entry(self.root,textvariable=self.var_empid,font=("times new roman",15),bg="lightyellow").place(x=200,y=150)
        gender_box=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state="readonly",justify=CENTER,font=("goudy old style",12))
        gender_box.place(x=550,y=150)
        gender_box.current(0)
        contact_txt=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=900,y=150)
        
        #Row 2
        Name_lbl=Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=80,y=200)
        dob_lbl=Label(self.root,text="D.O.B",font=("times new roman",15),bg="white").place(x=450,y=200)
        doj_lbl=Label(self.root,text="D.O.J",font=("times new roman",15),bg="white").place(x=800,y=200)
        
        name_txt=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow").place(x=200,y=200)
        dob_txt=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="lightyellow").place(x=550,y=200)
        doj_txt=Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),bg="lightyellow").place(x=900,y=200)
        
        #Row 3
        email_lbl=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=80,y=250)
        pass_lbl=Label(self.root,text="Password",font=("times new roman",15),bg="white").place(x=450,y=250)
        usertype_lbl=Label(self.root,text="User Type",font=("times new roman",15),bg="white").place(x=800,y=250)
        
        email_txt=Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="lightyellow").place(x=200,y=250)
        pass_txt=Entry(self.root,textvariable=self.var_pass,font=("times new roman",15),bg="lightyellow").place(x=550,y=250)
        usertype_txt=Entry(self.root,textvariable=self.var_utype,font=("times new roman",15),bg="lightyellow").place(x=900,y=250)
        
        #Row 4
        Address_lbl=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=80,y=300)
        
        
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=employee(root)
    root.mainloop()

        