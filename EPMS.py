from tkinter import*


class EmployeeSystem:
    def __init__(self,root):
        self.root = root
        self.root.title('Employee Payroll Mgmt Sys')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')
        title = Label(self.root,text = "Employee Payroll Mgmt Sys", font = ('',30,'bold'),bg='#262626',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

#----------------------------FRAMES--------------------------

    #   Frame 1
    
        Frame1 = Frame(self.root,bd=5,relief =RIDGE,bg='white')
        Frame1.place(x=10,y=70,width=750,height=620) 
        title2 = Label(Frame1,text = "Employee Details", font = ('times new roman',30,'bold'),bg='darkgray',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        lbl_code = Label(Frame1,text = "Employee Code :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=70)
        entry_code = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=210,y=80,width=200,height=30)
        btn_search = Button(Frame1,text = "Search", font = ('times new roman',15),bg='lightblue',fg='black',relief=GROOVE).place(x=440,y=75)

        #   RoW 1        
        lbl_desg = Label(Frame1,text = "Designation :", font = ('times new roman',20,),bg='white',fg='black',anchor='w').place(x=10,y=120)
        entry_desg = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=170,y=130,width=200,height=30)
    
        lbl_doj = Label(Frame1,text = "D.O.J. :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=120)
        entry_doj = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=525,y=130,width=200,height=30)
    
        #   RoW 2        
        lbl_name = Label(Frame1,text = "Name :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=170)
        entry_name = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=170,y=180,width=200,height=30)
    
        lbl_dob = Label(Frame1,text = "D.O.B. :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=170)
        entry_dob = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=525,y=180,width=200,height=30)

        #   RoW 3        
        lbl_age = Label(Frame1,text = "Age :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=220)
        entry_age = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=170,y=230,width=200,height=30)
    
        lbl_exp = Label(Frame1,text = "Experience :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=220)
        entry_exp = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=525,y=230,width=200,height=30)
   
        #   RoW 4        
        lbl_gender = Label(Frame1,text = "Gender :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=270)
        entry_gender = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=170,y=280,width=200,height=30)
    
        lbl_proof = Label(Frame1,text = "Proof ID :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=270)
        entry_proof = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=525,y=280,width=200,height=30)

        #   RoW 5
        lbl_mail = Label(Frame1,text = "Email :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=320)
        entry_mail = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=170,y=330,width=200,height=30)
    
        lbl_cno = Label(Frame1,text = "Contact No :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=320)
        entry_cno = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=525,y=330,width=200,height=30)

        #   RoW 6       
        lbl_jloc = Label(Frame1,text = "Job Location :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=370)
        entry_jloc = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=170,y=380,width=200,height=30)
    
        lbl_status = Label(Frame1,text = "Status :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=380,y=370)
        entry_status = Entry(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black').place(x=525,y=380,width=200,height=30)

        #   RoW 7       
        lbl_address = Label(Frame1,text = "Address :", font = ('times new roman',20),bg='white',fg='black',anchor='w').place(x=10,y=420)
        txt_address = Text(Frame1, font = ('times new roman',20),bg='lightyellow',fg='black')
        txt_address.place(x=170,y=430, width = 550, height=100)

    #   Frame 2

        Frame2 = Frame(self.root,bd=5,relief =RIDGE,bg='white')
        Frame2.place(x=770,y=70,width=580,height=300) 

    #   Frame 3

        Frame3 = Frame(self.root,bd=5,relief =RIDGE,bg='white')
        Frame3.place(x=770,y=380,width=580,height=310) 

#--------------------------------------------------------------

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()