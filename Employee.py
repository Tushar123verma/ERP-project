from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
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
        self.var_aadhar=StringVar()
        self.var_pan=StringVar()
        
        
        #____searchFrame____________
        searchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",15,"bold"),relief=RIDGE,bd=2)
        searchFrame.place(x=250,y=20,width=700,height=70)
        
        #____OPTIONS__________
        option_box=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Name","Email","Contact"),state="readonly",justify=CENTER,font=("goudy old style",11))
        option_box.place(x=10,y=10,width=180)
        option_box.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,bg="lightyellow",font=("goudy old style",15))
        txt_search.place(x=200,y=10)
        
        btn_search=Button(searchFrame,text="Search",bg="green",fg="white",cursor="hand2",font=("goudy old style",14,"bold")).place(x=410,y=10,width=150,height=25)
        
        #____Title_emp____
        emp_lbl=Label(self.root,text="Employee Details",font=("goudy old style",15,'bold'),bg="#45458B",fg='white').place(x=80,y=100,width=1030)
        
        #___content_emp______row1
        empid_lbl=Label(self.root,text="Employee Id",font=("times new roman",15),bg="white").place(x=80,y=150)
        gender_lbl=Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=450,y=150)
        contact_lbl=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=800,y=150)
        
        empid_txt=Entry(self.root,textvariable=self.var_empid,font=("times new roman",15),bg="lightyellow").place(x=200,y=150)
        gender_box=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state="readonly",justify=CENTER,font=("goudy old style",12))
        gender_box.place(x=550,y=150,width=200)
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
        usertype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state="readonly",justify=CENTER,font=("goudy old style",12))
        usertype.place(x=900,y=250,width=200)
        usertype.current(0)
        
        #Row 4
        Address_lbl=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=80,y=300)
        Aadhar_lbl=Label(self.root,text="Aadhar",font=("times new roman",15),bg="white").place(x=450,y=300)
        pan_lbl=Label(self.root,text="PAN",font=("times new roman",15),bg="white").place(x=800,y=300)
        
        self.address_txt=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.address_txt.place(x=200,y=300,width=200,height=100)
        aadhar_txt=Entry(self.root,textvariable=self.var_aadhar,font=("times new roman",15),bg="lightyellow").place(x=550,y=300)
        pan_txt=Entry(self.root,textvariable=self.var_pan,font=("times new roman",15),bg="lightyellow").place(x=900,y=300)
        
        
        #_______Button_________
        btn_save=Button(self.root,text="Save",command=self.add,bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=450,y=360,width=100,height=25)
        btn_update=Button(self.root,text="Update",bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=570,y=360,width=100,height=25)
        btn_delete=Button(self.root,text="Delete",bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=690,y=360,width=100,height=25)
        btn_update=Button(self.root,text="Clear",bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=810,y=360,width=100,height=25)
        
        #______Employee_table_________
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=405,relwidth=1,height=150)
        
        scrollX=Scrollbar(emp_frame,orient=HORIZONTAL)
        scrollY=Scrollbar(emp_frame,orient=VERTICAL)
        
        self.employeeTable=ttk.Treeview(emp_frame,columns=('eid','name','email','gender','contact','dob','doj','pass','usertype','aadhar','pan','address'),yscrollcommand=scrollY.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.employeeTable.xview)
        scrollY.config(command=self.employeeTable.yview)
        self.employeeTable.heading('eid',text='Emp id')
        self.employeeTable.heading('name',text='Name')
        self.employeeTable.heading('email',text='Email')
        self.employeeTable.heading('gender',text='Gender')
        self.employeeTable.heading('contact',text='Contact')
        self.employeeTable.heading('dob',text='D.O.B')
        self.employeeTable.heading('doj',text='D.O.J')
        self.employeeTable.heading('pass',text='Password')
        self.employeeTable.heading('usertype',text='User Type')
        self.employeeTable.heading('aadhar',text='Aadhar')
        self.employeeTable.heading('pan',text='PAN')
        self.employeeTable.heading('address',text='Address')
        
        self.employeeTable["show"]="headings"
        
        self.employeeTable.column('eid',width=90)
        self.employeeTable.column('name',width=100)
        self.employeeTable.column('email',width=100)
        self.employeeTable.column('gender',width=100)
        self.employeeTable.column('contact',width=100)
        self.employeeTable.column('dob',width=100)
        self.employeeTable.column('doj',width=100)
        self.employeeTable.column('pass',width=100)
        self.employeeTable.column('usertype',width=100)
        self.employeeTable.column('aadhar',width=100)
        self.employeeTable.column('pan',width=100)
        self.employeeTable.column('address',width=200)
        
        self.employeeTable.pack(fill=BOTH,expand=1)
        self.employeeTable.bind("<ButtonRelease-1>",self.get_data)
        
        
        #self.show()
        
        
    #_______saveButton__________
    def add(self):
        con=sqlite3.Connection(database=r'erp.db')
        cur=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror("Error",'Employee ID must be required',parent=self.root)
            else:
                cur.execute('Select * from employee where eid=?',(self.var_empid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error',"This emp id already registered",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,usertype,aadhar,pan,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_empid.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.var_aadhar.get(),
                        self.var_pan.get(),
                        self.address_txt.get('1.0',END),
                        
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee added successfully",parent=self.root) 
                    self.show()   
        except Exception as e:
            messagebox.showerror('Error',f'error due to: {str(e)}',parent=self.root)
            

    #_______ShowInfo______________
    def show(self):
        con=sqlite3.Connection(database=r'erp.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employeeTable.delete(*self.employeeTable.get_children())
            for row in rows:
                self.employeeTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror('Error',f'error due to: {str(e)}',parent=self.root)  
            
        
    def get_data(self,ev):
        f=self.employeeTable.focus()
        content=(self.employeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_empid.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.var_aadhar.set(row[9])
        self.var_pan.set(row[10])
        self.address_txt.delete('1.0',END)
        self.address_txt.insert(END,row[11])
        
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=employee(root)
    root.mainloop()

        