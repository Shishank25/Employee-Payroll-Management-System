from tkinter import*
from tkinter import messagebox
import pymysql
import time

class EmployeeSystem:
    def __init__(self,root):
        self.root = root
        self.root.title('Employee Payroll Mgmt Sys')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')
        title = Label(self.root,text = "Employee Payroll Mgmt Sys", font = ('',30,'bold'),bg='#262626',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        btn_allemps = Button(self.root,text='Show All Employees',font = ('times new roman',15,'bold'),bg="#7FA1C3",fg='white').place(rely=0.01,relx=0.85,)    

#----------------------------FRAMES--------------------------

    #   Frame 1 Variables

        self.empc = StringVar()
        self.desg = StringVar()
        self.doj = StringVar()
        self.name = StringVar()
        self.dob = StringVar()
        self.age = StringVar()
        self.exp = StringVar()
        self.gender = StringVar()
        self.proof = StringVar()
        self.mail = StringVar()
        self.contact = StringVar()
        self.jloc = StringVar()
        self.status = StringVar()


    #   Frame 1
    
        Frame1 = Frame(self.root,bd=5,relief =RIDGE,bg='white')
        Frame1.place(relx=0.01,y=70,relwidth=750,height=620) 
        title2 = Label(Frame1,text = "Employee Details", font = ('times new roman',30,'bold'),bg='darkgray',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        

        lbl_code = Label(Frame1,text = "Employee Code :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=70)
        entry_code = Entry(Frame1, font = ('times new roman',20),textvariable=self.empc,bg='lightyellow',fg='black').place(x=210,y=80,width=200,height=30)
        btn_search = Button(Frame1,text = "Search",command=self.search, font = ('times new roman',15),bg='lightblue',fg='black',relief=GROOVE).place(x=440,y=75)

        #   RoW 1        
        lbl_desg = Label(Frame1,text = "Designation :", font = ('times new roman',20,),bg='white',fg='black',anchor='w').place(x=10,y=120)
        entry_desg = Entry(Frame1, font = ('times new roman',20),textvariable=self.desg,bg='lightyellow',fg='black').place(x=170,y=130,width=200,height=30)
    
        lbl_doj = Label(Frame1,text = "D.O.J. :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=120)
        entry_doj = Entry(Frame1, font = ('times new roman',20),textvariable=self.doj,bg='lightyellow',fg='black').place(x=525,y=130,width=200,height=30)
    
        #   RoW 2        
        lbl_name = Label(Frame1,text = "Name :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=170)
        entry_name = Entry(Frame1, font = ('times new roman',20),textvariable=self.name,bg='lightyellow',fg='black').place(x=170,y=180,width=200,height=30)
    
        lbl_dob = Label(Frame1,text = "D.O.B. :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=170)
        entry_dob = Entry(Frame1, font = ('times new roman',20),textvariable=self.dob,bg='lightyellow',fg='black').place(x=525,y=180,width=200,height=30)

        #   RoW 3        
        lbl_age = Label(Frame1,text = "Age :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=220)
        entry_age = Entry(Frame1, font = ('times new roman',20),textvariable=self.age,bg='lightyellow',fg='black').place(x=170,y=230,width=200,height=30)
    
        lbl_exp = Label(Frame1,text = "Experience :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=220)
        entry_exp = Entry(Frame1, font = ('times new roman',20),textvariable=self.exp,bg='lightyellow',fg='black').place(x=525,y=230,width=200,height=30)
   
        #   RoW 4        
        lbl_gender = Label(Frame1,text = "Gender :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=270)
        entry_gender = Entry(Frame1, font = ('times new roman',20),textvariable=self.gender,bg='lightyellow',fg='black').place(x=170,y=280,width=200,height=30)
    
        lbl_proof = Label(Frame1,text = "Proof ID :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=270)
        entry_proof = Entry(Frame1, font = ('times new roman',20),textvariable=self.proof,bg='lightyellow',fg='black').place(x=525,y=280,width=200,height=30)

        #   RoW 5
        lbl_mail = Label(Frame1,text = "Email :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=320)
        entry_mail = Entry(Frame1, font = ('times new roman',20),textvariable=self.mail,bg='lightyellow',fg='black').place(x=170,y=330,width=200,height=30)
    
        lbl_cno = Label(Frame1,text = "Contact No :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=320)
        entry_cno = Entry(Frame1, font = ('times new roman',20),textvariable=self.contact,bg='lightyellow',fg='black').place(x=525,y=330,width=200,height=30)

        #   RoW 6       
        lbl_jloc = Label(Frame1,text = "Job Location :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=370)
        entry_jloc = Entry(Frame1, font = ('times new roman',20),textvariable=self.jloc,bg='lightyellow',fg='black').place(x=170,y=380,width=200,height=30)
    
        lbl_status = Label(Frame1,text = "Status :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=370)
        entry_status = Entry(Frame1, font = ('times new roman',20),textvariable=self.status,bg='lightyellow',fg='black').place(x=525,y=380,width=200,height=30)

        #   RoW 7       
        lbl_address = Label(Frame1,text = "Address :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=420)
        self.txt_address = Text(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black')
        self.txt_address.place(x=170,y=430, width = 550, height=100)

    
    #   Frame 2 Variables

        self.month = StringVar()
        self.year = StringVar()
        self.basepay = StringVar()
        self.tdays = StringVar()
        self.absent = StringVar()
        self.medical = StringVar()
        self.pf = StringVar()
        self.convence = StringVar()
        self.netsal = StringVar()
    
    #   Frame 2

        Frame2 = Frame(self.root,bd=5,relief =RIDGE,bg='white')
        Frame2.place(x=770,y=70,width=580,height=300) 

        title3 = Label(Frame2,text = "Employee Salary Details", font = ('times new roman',30,'bold'),bg='darkgray',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        #   RoW 1        
        lbl_month = Label(Frame2,text = "Month ", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=10,y=70)
        entry_month = Entry(Frame2, font = ('times new roman',15),textvariable=self.month,bg='lightyellow',fg='black').place(x=75,y=75,width=100,height=25)
    
        lbl_year = Label(Frame2,text = "Year ", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=190,y=70)
        entry_year = Entry(Frame2, font = ('times new roman',15),textvariable=self.year,bg='lightyellow',fg='black').place(x=245,y=75,width=100,height=25)

        lbl_bp = Label(Frame2,text = "Base Pay", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=360,y=70)
        entry_bp = Entry(Frame2, font = ('times new roman',15),textvariable=self.basepay,bg='lightyellow',fg='black').place(x=450,y=75,width=110,height=25)

        #   Row 2
        lbl_tdays = Label(Frame2,text = "Total Days", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=10,y=105)
        entry_tdays = Entry(Frame2, font = ('times new roman',15),textvariable=self.tdays,bg='lightyellow',fg='black').place(x=105,y=110,width=100,height=25)
    
        lbl_absent = Label(Frame2,text = "Absents", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=225,y=105)
        entry_absent = Entry(Frame2, font = ('times new roman',15),textvariable=self.absent,bg='lightyellow',fg='black').place(x=300,y=110,width=100,height=25)

        #   RoW 3        
        lbl_med = Label(Frame2,text = "Medical", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=10,y=155)
        entry_med = Entry(Frame2, font = ('times new roman',15),textvariable=self.medical,bg='lightyellow',fg='black').place(x=90,y=160,width=100,height=25)
    
        lbl_pf = Label(Frame2,text = "Provident Fund", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=210,y=155)
        entry_pf = Entry(Frame2, font = ('times new roman',15),textvariable=self.pf,bg='lightyellow',fg='black').place(x=345,y=160,width=100,height=25)

        #   Row 4
        lbl_convence = Label(Frame2,text = "Convence", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=10,y=190)
        entry_convence = Entry(Frame2, font = ('times new roman',15),textvariable=self.convence,bg='lightyellow',fg='black').place(x=100,y=195,width=100,height=25)
    
        lbl_netsal = Label(Frame2,text = "Net Salary", font = ('times new roman',15),bg='white',fg='black',anchor='w').place(x=225,y=190)
        entry_netsal = Entry(Frame2, font = ('times new roman',15),textvariable=self.netsal,bg='lightyellow',fg='black').place(x=320,y=195,width=100,height=25)

        # RoW 5
        btn_upd = Button(Frame2,text = "Update",command=self.Update, font = ('times new roman',15),bg='#A1D6B2',fg='black',relief=GROOVE).place(relx=0.3,y=265,anchor=CENTER)
        btn_dlt = Button(Frame2,text = "Delete",command=self.delete, font = ('times new roman',15),bg='#E4003A',fg='black',relief=GROOVE).place(relx=0.85,y=265,anchor=CENTER)
        btn_calc = Button(Frame2,text = "Calculate",command=self.Calculate, font = ('times new roman',15),bg='lightblue',fg='black',relief=GROOVE).place(relx=0.12,y=265,anchor=CENTER)
        btn_save = Button(Frame2,text = "Save", font = ('times new roman',15),command=self.add,bg='#83B4FF',fg='black',relief=GROOVE).place(relx=0.5,y=265,anchor=CENTER)
        btn_clr = Button(Frame2,text = "Clear",command=self.Clear, font = ('times new roman',15),bg='#C7253E',fg='black',relief=GROOVE).place(relx=0.72,y=265,anchor=CENTER)


    #   Frame 3

        Frame3 = Frame(self.root,bd=5,relief =RIDGE,bg='white')
        Frame3.place(x=770,y=380,width=580,height=310)

        res_frame = Frame(Frame3,bg='white',bd=2,relief=RIDGE) 
        res_frame.place(x=2,y=2,width=280,height=40)

        self.txt_result = Entry(res_frame,bg='#E1F7F5',font=('times new roman',17),justify=RIGHT)
        self.txt_result.place(x=0,y=0,width=225,height=35)

        btn_dot = Button(res_frame, text='.',font=('times new roman',15,),bd=1,relief=GROOVE,command=lambda x='.': self.on_button_click(x))
        btn_dot.place(x=230,y=2,height=35,width=40)

        #---------------Calculator------------------------------#
        
        cal_frame = Frame(Frame3,bg='white',bd=2,relief=RIDGE)
        cal_frame.place(x=2,y=40,width=280,height=258)

        # Buttons
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '+', '=']


        for i in range(4):
            for j in range(4):
                btn = Button(cal_frame, text=button_texts[i*4 + j], font=('times new roman', 15), bd=1, relief=RIDGE,command=lambda x=button_texts[i*4 + j]: self.on_button_click(x))
                btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        # Configure the grid layout to ensure buttons resize properly
        for i in range(4):
            cal_frame.grid_columnconfigure(i, weight=1)
            cal_frame.grid_rowconfigure(i, weight=1)

        
        #---------------Salary Frame---------------------------#

        sample = f'''\tCompany Name, XYZ\n\tAddress: ABC, Floor2
------------------------------------
 Employee ID\t\t: 
 Salary of\t\t: MON-YYYY
 Generated on\t\t: DD-MM-YYYY
------------------------------------
 Totql Days\t\t:  DD
 Total Present\t\t:  DD
 Total Absent\t\t:  DD
 Convence\t\t:  Rs.----
 Medical\t\t:  Rs.----
 PF\t\t\t:  Rs.----
 Gross Payment\t\t:  Rs.------
 Net Salary\t\t:  Rs.------
------------------------------------
This is a computer generated slip, 
signature not required
'''
        sal_frame = Frame(Frame3,bg='white',bd=2,relief=RIDGE)
        sal_frame.place(x=284,y=2,width=285,height=296)

        sal_title = Label(sal_frame,text='Salary Receipt',font=('times new roman',18,'bold'),bg='darkgray',fg='white',anchor = 'w').place(x=2,y=2,width=277)

        dis_frame = Frame(sal_frame,bg='white',bd=2,relief=RIDGE)
        dis_frame.place(x=2,y=35,width=277,height=220)

        scroll_y = Scrollbar(dis_frame,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salrec = Text(dis_frame,font=('times new roman',12),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salrec.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salrec.yview)
        self.txt_salrec.insert(END,sample)
        
        prnt_btn = Button(sal_frame,text='Print',font=('times new roman',15),bg='lightgray')
        prnt_btn.place(relx=0.5,anchor=CENTER,rely=0.935,height=30,relwidth=0.5)

        self.check_connection()




    #-------------------END OF INIT----------------------------------#
    
    def delete(self):

        if self.empc.get()=='':
            messagebox.showinfo('','Please Enter Employee ID to Search')

        else:

            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='emps')
                cur=con.cursor()
                cur.execute('Select * from emp_sal where emp_code=%s',(self.empc.get()))
                rows=cur.fetchone()
                if rows==None:
                    messagebox.showerror('Not Found','Employee ID does not exist',parent=self.root)
                else:
                    self.search()
                    op=messagebox.askyesno('','Do you want to delete this record?')
                    if op==True:
                        cur.execute('delete from emp_sal where emp_code=%s',(self.empc.get()))
                        con.commit()
                        con.close()


            except Exception as ex:
                messagebox.showerror('Error',f'Error due to:{str(ex)}')

    def Clear(self):
     
        self.empc.set('')
        self.desg.set('')
        self.name.set('')
        self.age.set('')
        self.doj.set('')
        self.dob.set('')
        self.exp.set('')
        self.gender.set('')
        self.proof.set('')
        self.mail.set('')
        self.contact.set('')
        self.jloc.set('')
        self.status.set('')
        self.txt_address.delete('1.0',END)
        self.txt_address.insert('1.0','')
        self.month.set('')
        self.year.set('')
        self.basepay.set('')
        self.tdays.set('')
        self.absent.set('')
        self.medical.set('')
        self.pf.set('')
        self.convence.set('')
        self.netsal.set('')

    
    def search(self):

        if self.empc.get()=='':
            messagebox.showinfo('','Please Enter Employee ID to Search')

        else:

            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='emps')
                cur=con.cursor()
                cur.execute('Select * from emp_sal where emp_code=%s',(self.empc.get()))
                rows=cur.fetchone()
                if rows==None:
                    messagebox.showinfo('Not Found','Employee ID not found',parent=self.root)
                else:
                    self.empc.set(rows[0])
                    self.desg.set(rows[1])
                    self.name.set(rows[2])
                    self.age.set(rows[3])
                    self.doj.set(rows[4])
                    self.dob.set(rows[5])
                    self.exp.set(rows[6])
                    self.gender.set(rows[7])
                    self.proof.set(rows[8])
                    self.mail.set(rows[9])
                    self.contact.set(rows[10])
                    self.jloc.set(rows[11])
                    self.status.set(rows[12])
                    self.txt_address.delete('1.0',END)
                    self.txt_address.insert('1.0',rows[13])
                    self.month.set(rows[14])
                    self.year.set(rows[15])
                    self.basepay.set(rows[16])
                    self.tdays.set(rows[17])
                    self.absent.set(rows[18])
                    self.medical.set(rows[19])
                    self.pf.set(rows[20])
                    self.convence.set(rows[21])
                    self.netsal.set(rows[22])

                    file1=open('salary_receipts/'+str(rows[23]),'r')
                    self.txt_salrec.delete('1.0',END)

                    for i in file1:
                        self.txt_salrec.insert(END,i)

                    file1.close()


            except Exception as ex:
                messagebox.showerror('Error',f'Error due to:{str(ex)}')    


    def add(self):

        if self.empc.get()==''    or  self.name.get()==''   or  self.proof.get()=='':

            messagebox.showerror('Error','Employee ID, Name and Proof cannot be Blank')

        else:

            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='emps')
                cur=con.cursor()
                cur.execute('Select * from emp_sal where emp_code=%s',(self.empc.get()))
                rows=cur.fetchone()
                if rows!=None:
                    messagebox.showerror('Error','An employee with this Employee ID already exists',parent=self.root)
                else:
                    cur.execute('insert into emp_sal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        (
                            self.empc.get(),
                            self.desg.get(),
                            self.name.get(),
                            self.age.get(),
                            self.doj.get(),
                            self.dob.get(),
                            self.exp.get(),
                            self.gender.get(),
                            self.proof.get(),
                            self.mail.get(),
                            self.contact.get(),
                            self.jloc.get(),
                            self.status.get(),
                            self.txt_address.get('1.0',END),

                            self.month.get(),
                            self.year.get(),
                            self.basepay.get(),
                            self.tdays.get(),
                            self.absent.get(),
                            self.medical.get(),
                            self.pf.get(),
                            self.convence.get(),
                            self.netsal.get(),
                            self.empc.get()+'.txt'
                            
                        )
                    )
                    con.commit()
                    con.close()
                    file1=open('salary_receipts/'+str(self.empc.get())+'.txt','w')
                    file1.write(self.txt_salrec.get('1.0',END))
                    file1.close()

                    messagebox.showinfo('Record Added','Your record has been added to the DataBase')


            except Exception as ex:
                messagebox.showerror('Error',f'Error due to:{str(ex)}')

    
    def Update(self):

        if self.empc.get()=='':

            messagebox.showinfo('','Please Enter Employee ID')

        else:

            try:
                con = pymysql.connect(host='localhost',user='root',password='',db='emps')
                cur=con.cursor()
                cur.execute('Select * from emp_sal where emp_code=%s',(self.empc.get()))
                rows=cur.fetchone()
                if rows==None:
                    messagebox.showerror('Error','Employee ID not found',parent=self.root)
                else:
                    cur.execute("UPDATE `emp_sal` SET `designation`=%s,`name`=%s,`age`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`gender`=%s,`proof`=%s,`mail`=%s,`contact`=%s,`jobloc`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basepay`=%s,`tdays`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`netsal`=%s,`salrec`=%s WHERE `emp_code`=%s",
                        (
                            self.desg.get(),
                            self.name.get(),
                            self.age.get(),
                            self.doj.get(),
                            self.dob.get(),
                            self.exp.get(),
                            self.gender.get(),
                            self.proof.get(),
                            self.mail.get(),
                            self.contact.get(),
                            self.jloc.get(),
                            self.status.get(),
                            self.txt_address.get('1.0',END),

                            self.month.get(),
                            self.year.get(),
                            self.basepay.get(),
                            self.tdays.get(),
                            self.absent.get(),
                            self.medical.get(),
                            self.pf.get(),
                            self.convence.get(),
                            self.netsal.get(),
                            self.empc.get()+'.txt',
                            self.empc.get(),
                            
                        )
                    )
                    con.commit()
                    con.close()
                    file1=open('salary_receipts/'+str(self.empc.get())+'.txt','w')
                    file1.write(self.txt_salrec.get('1.0',END))
                    file1.close()

                    messagebox.showinfo('Record Updated','Your record has been Updated')


            except Exception as ex:
                messagebox.showerror('Error',f'Error due to:{str(ex)}')

    def Calculate(self):
    
        # # Frame 1 Variable
            #     print(self.empc.get(),
            #     self.desg.get(),
            #     self.doj.get(),
            #     self.name.get(),
            #     self.dob.get(),
            #     self.age.get(),
            #     self.exp.get(),
            #     self.gender.get(),
            #     self.proof.get(),
            #     self.mail.get(),
            #     self.contact.get(),
            #     self.jloc.get(),
            #     self.status.get())

        # # Frame 2 Variables

            #     print(self.month.get(),
            #     self.year.get(),
            #     self.basepay.get(),
            #     self.tdays.get(),
            #     self.absent.get(),
            #     self.medical.get(),
            #     self.pf.get(),
            #     self.convence.get(),
            #     self.netsal.get(),
            #     self.txt_address.get('1.0',END),)

        if self.month.get()=='' or  self.year.get()=='' or  self.basepay.get()=='' or self.tdays.get()=='' or self.absent.get()=='':
                messagebox.showerror('Error','All fields are required')
        else:
                #   self.var_net_salary.set("RESULT")
                #   35000/31==1752
                #   31-10=21*1752
                per_day=int(self.basepay.get()) / int(self.tdays.get())
                work_day=int(self.tdays.get()) - int(self.absent.get())
                sal_=per_day*work_day
                deduct=int(self.medical.get()) + int(self.pf.get())
                addition=int(self.convence.get())
                net_sal=sal_-deduct+addition
                self.netsal.set(str(round(net_sal,2)))
                
                
                new_sample = f'''\tCompany Name, XYZ\n\tAddress: ABC, Floor2
------------------------------------
 Employee ID\t\t:  {self.empc.get()}
 Salary of\t\t: {self.month.get()}-{self.year.get()}
 Generated on\t\t: {time.strftime('%d-%m-%Y')}
------------------------------------
 Totql Days\t\t:  {self.tdays.get()}
 Total Present\t\t:  {int(self.tdays.get())-int(self.absent.get())}
 Total Absent\t\t:  {self.absent.get()}
 Convence\t\t:  Rs.{self.convence.get()}
 Medical\t\t:  Rs.{self.medical.get()}
 PF\t\t:  Rs.{self.pf.get()}
 Gross Payment\t\t:  Rs.{self.basepay.get()}
 Net Salary\t\t:  Rs.{self.netsal.get()}
------------------------------------
This is a computer generated slip, 
signature not required
'''             
                self.txt_salrec.delete('1.0',END)
                self.txt_salrec.insert(END,new_sample)

    def on_button_click(self, value):
        current_text = self.txt_result.get()
        if value == "C":
            # Clear the display
            self.txt_result.delete(0, END)
        elif value == "=":
            # Evaluate the expression and show the result
            try:
                result = str(eval(current_text))
                self.txt_result.delete(0, END)
                self.txt_result.insert(END, result)
            except:
                self.txt_result.delete(0, END)
                self.txt_result.insert(END, "Error")
        else:
            # Append the pressed button's value to the display
            self.txt_result.insert(END, value)

    def check_connection(self):

        try:
            con = pymysql.connect(host='localhost',user='root',password='',db='emps')
            cur=con.cursor()
            cur.execute('Select * from emp_sal')
            rows=cur.fetchall()
            print(rows)

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to:{str(ex)}')
            


#----------------------END OF EMPLOYEE SYSTEM----------------------------------------


#--------------------------MAIN LOOP------------------------

root = Tk()
obj = EmployeeSystem(root)
root.mainloop() 
