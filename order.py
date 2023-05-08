from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from tkcalendar import Calendar, DateEntry
class Order:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x550+300+150")
        self.root.title("ERP system  ||  Developed by Tushar")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #All variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        
        self.var_po_Num=StringVar()        
        self.var_offer_num=StringVar()        
        self.var_po_date=StringVar()
        self.var_cname=StringVar()
        self.var_addr=StringVar()
        self.var_pName=StringVar()                                   
        self.var_cont=StringVar()   
        self.var_email=StringVar()              
        self.var_projLdr=StringVar()         
        
        #____searchFrame______
        searchFrame=LabelFrame(self.root,text="Search Order",bg="white",font=("goudy old style",15,"bold"),relief=RIDGE,bd=2)
        searchFrame.place(x=250,y=15,width=700,height=70)
        
        #____OPTIONS__________
        option_box=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","po_NO"),state="readonly",justify=CENTER,font=("goudy old style",11))
        option_box.place(x=10,y=10,width=180)
        option_box.current(0)
        
        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,bg="lightyellow",font=("goudy old style",15))
        txt_search.place(x=200,y=10)
        
        btn_search=Button(searchFrame,text="Search",bg="green",command=self.search,fg="white",cursor="hand2",font=("goudy old style",14,"bold")).place(x=410,y=10,width=150,height=25)
        
         
        #____Title_ord____
        ord_lbl=Label(self.root,text="Order Details",font=("goudy old style",20,'bold'),bg="#45458B",fg='white').place(x=60,y=100,width=1100)
        
        #___content_ord______row1
        po_lbl=Label(self.root,text="P.O No.",font=("times new roman",15),bg="white").place(x=80,y=150)
        offer_lbl=Label(self.root,text="Offer No.",font=("times new roman",15),bg="white").place(x=450,y=150)
        po_date_lbl=Label(self.root,text="P.O Date",font=("times new roman",15),bg="white").place(x=800,y=150)
        
        
        po_txt=Entry(self.root,textvariable=self.var_po_Num,font=("times new roman",15),bg="lightyellow").place(x=220,y=150)
        offer_txt=Entry(self.root,textvariable=self.var_offer_num,font=("times new roman",15),bg="lightyellow").place(x=550,y=150)
        podate_txt = DateEntry(self.root, width= 16, background= "magenta3", foreground= "white",bd=2)
        podate_txt.place(x=930,y=150,width=200)
        
        #Row 2
        Cname_lbl=Label(self.root,text="Company Name",font=("times new roman",15),bg="white").place(x=80,y=200)
        Cname_txt=Entry(self.root,textvariable=self.var_cname,font=("times new roman",15),bg="lightyellow").place(x=220,y=200)
        
        addr_lbl=Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=450,y=200)
        addr_txt=Entry(self.root,textvariable=self.var_addr,font=("times new roman",15),bg="lightyellow").place(x=550,y=200)
        
        perName_lbl=Label(self.root,text="Person Name",font=("times new roman",15),bg="white").place(x=800,y=200)
        perName_txt=Entry(self.root,textvariable=self.var_pName,font=("times new roman",15),bg="lightyellow").place(x=930,y=200)
        
        contact_lbl=Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=80,y=250)
        contact_txt=Entry(self.root,textvariable=self.var_cont,font=("times new roman",15),bg="lightyellow").place(x=220,y=250)
        
        email_lbl=Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=450,y=250)
        email_txt=Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="lightyellow").place(x=550,y=250)
        
        projectLdr_lbl=Label(self.root,text="Project Leader",font=("times new roman",15),bg="white").place(x=800,y=250)
        projectLdr_txt=Entry(self.root,textvariable=self.var_projLdr,font=("times new roman",15),bg="lightyellow").place(x=930,y=250)
        
        
         #_______Button_________
        btn_save=Button(self.root,text="Save",command=self.add,bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=80,y=320,width=100,height=25)
        btn_update=Button(self.root,text="Update",command=self.update,bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=200,y=320,width=100,height=25)
        btn_delete=Button(self.root,text="Delete",command=self.delete,bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=320,y=320,width=100,height=25)
        btn_clear=Button(self.root,text="Clear",command=self.clear,bg="Grey",fg="white",font=("goudy old style",14,"bold"),cursor='hand2').place(x=440,y=320,width=100,height=25)
        
        #______Order_table_________
        ord_frame=Frame(self.root,bd=3,relief=RIDGE)
        ord_frame.place(x=0,y=370,relwidth=1,height=170)
        
        scrollX=Scrollbar(ord_frame,orient=HORIZONTAL)
        scrollY=Scrollbar(ord_frame,orient=VERTICAL)
        
        self.orderTable=ttk.Treeview(ord_frame,columns=('po_NO','offerNo','podate','Cname','addr','pName','contact','email','project_leader'),yscrollcommand=scrollY.set,xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.orderTable.xview)
        scrollY.config(command=self.orderTable.yview)
        
        self.orderTable.heading('po_NO',text='P.O No.')
        self.orderTable.heading('offerNo',text='Offer No.')
        self.orderTable.heading('podate',text='P.O. Date')
        self.orderTable.heading('Cname',text='Company Name')
        self.orderTable.heading('addr',text='Address')
        self.orderTable.heading('pName',text='Person Name')
        self.orderTable.heading('contact',text='Contact')
        self.orderTable.heading('email',text='Email')
        self.orderTable.heading('project_leader',text='Project Leader')     
        
        
        self.orderTable["show"]="headings"
        
        self.orderTable.column('po_NO',width=90)
        self.orderTable.column('offerNo',width=100)
        self.orderTable.column('podate',width=100)
        self.orderTable.column('Cname',width=100)
        self.orderTable.column('addr',width=100)
        self.orderTable.column('pName',width=100)
        self.orderTable.column('contact',width=100)
        self.orderTable.column('email',width=100)
        self.orderTable.column('project_leader',width=100)
        
        self.orderTable.pack(fill=BOTH,expand=1)
        self.orderTable.bind("<ButtonRelease-1>",self.get_data)
        #self.show()
    
    
    #_______saveButton_________
    def add(self):
        con=sqlite3.Connection(database=r'ord.db')
        cur=con.cursor()
        try:
            if self.var_po_Num.get()=="":
                messagebox.showerror("Error",'PO Number must be required',parent=self.root)
            else:
                cur.execute('Select * from Order_ where po_NO=?',(self.var_po_Num.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error',"This PO number already registered",parent=self.root)
                else:
                    cur.execute("Insert into Order_(po_NO,offerNo,podate,Cname,addr,pName,contact,email,project_leader) values(?,?,?,?,?,?,?,?,?)",(
                        self.var_po_Num.get(),
                        self.var_offer_num.get(),
                        self.var_po_date.get(),
                        self.var_cname.get(),
                        self.var_addr.get(),
                        self.var_pName.get(),
                        self.var_cont.get(),
                        self.var_email.get(),
                        self.var_projLdr.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","order Info added successfully",parent=self.root) 
                    self.show()   
        except Exception as e:
            messagebox.showerror('Error',f'error due to: {str(e)}',parent=self.root)
            
    #_______ShowInfo__________
    def show(self):
        con=sqlite3.Connection(database=r'ord.db')
        cur=con.cursor()
        try:
            cur.execute("select * from Order_")
            rows=cur.fetchall()
            self.orderTable.delete(*self.orderTable.get_children())
            for row in rows:
                self.orderTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror('Error',f'error due to: {str(e)}',parent=self.root)
            
    def get_data(self,ev):
        f=self.orderTable.focus()
        content=(self.orderTable.item(f))
        row=content['values']
        #print(row)
        self.var_po_Num.set(row[0])
        self.var_offer_num.set(row[1])
        self.var_po_date.set(row[2])
        self.var_cname.set(row[3])
        self.var_addr.set(row[4])
        self.var_pName.set(row[5])
        self.var_cont.set(row[6])
        self.var_email.set(row[7])
        self.var_projLdr.set(row[8])
        
    
    #____Update_________
    
    def update(self):
        con=sqlite3.Connection(database=r'ord.db')
        cur=con.cursor()
        try:
            if self.var_po_Num.get()=="":
                messagebox.showerror("Error",'Po No. must be required',parent=self.root)
            else:
                cur.execute('Select * from Order_ where po_NO=?',(self.var_po_Num.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error',"Invaild po No.",parent=self.root)
                else:
                    cur.execute("Update Order_ set offerNo=?,podate=?,Cname=?,addr=?,pName=?,contact=?,email=?,project_leader=? where po_NO=?",(
                        self.var_offer_num.get(),
                        self.var_po_date.get(),
                        self.var_cname.get(),
                        self.var_addr.get(),
                        self.var_pName.get(),
                        self.var_cont.get(),
                        self.var_email.get(),
                        self.var_projLdr.get(),
                        self.var_po_Num.get(),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","order Info updated successfully",parent=self.root) 
                    self.show()
        except Exception as e:
            messagebox.showerror('Error',f'error due to: {str(e)}',parent=self.root)
            
    
    #_________Delete__________
    
    def delete(self):
        con=sqlite3.Connection(database=r'ord.db')
        cur=con.cursor()
        try:
            if self.var_po_Num.get()=="":
                messagebox.showerror("Error",'po No. must be required',parent=self.root)
            else:
                cur.execute('Select * from Order_ where po_NO=?',(self.var_po_Num.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error',"Invalid Po No.",parent=self.root)
                else:
                    op=messagebox.askyesno('confirm','Do you want to delete?',parent=self.root)
                    if op==True:
                        cur.execute("delete from Order_ where po_NO=?", (self.var_po_Num.get(),))
                        con.commit()
                        messagebox.showinfo("Success","order Info Deleted successfully",parent=self.root) 
                        self.clear()
        except Exception as e:
            messagebox.showerror('Error',f'error due to: {str(e)}',parent=self.root)
            
    
    #______Clear____
    
    def clear(self):
        self.var_po_Num.set('')
        self.var_offer_num.set('')
        self.var_po_date.set('')
        self.var_cname.set('')
        self.var_addr.set('')
        self.var_pName.set('')
        self.var_cont.set('')
        self.var_email.set('')
        self.var_projLdr.set('')
        self.var_searchtxt.set('')
        self.var_searchby.set('Select')
        self.show()
        
    #________Search__________
    def search(self):
        con=sqlite3.Connection(database=r'ord.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=='Select':
                messagebox.showerror('Error','select Searchby option',parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror('Error',"Search input should be required",parent=self.root)
            else:
                cur.execute('select * from Order_ where po_NO LIKE "1%"')
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.orderTable.delete(*self.orderTable.get_children())
                    for row in rows:
                        self.orderTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as e:
            messagebox.showerror('Error',f'error due to: {str(e)}',parent=self.root)
            
            
        
if __name__=="__main__":
    root=Tk()
    obj=Order(root)
    root.mainloop()

