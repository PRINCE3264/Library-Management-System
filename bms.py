import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import datetime



class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1530x800+0+0")

       
        self.member_var = tk.StringVar()
        self.pnr_var = tk.StringVar()
       

        
        Framebutton = tk.Frame(self.root)
        Framebutton.pack()
        
        self.member_var=tk.StringVar()
        self.pnr_var=tk.StringVar()
        self.id_var=tk.StringVar()
        self.firstname_var=tk.StringVar()
        self.lastname_var=tk.StringVar()
        self.address1_var=tk.StringVar()
        self.address2_var=tk.StringVar()
        self.postcode_var=tk.StringVar()
        self.mobile_var=tk.StringVar()
        self.bookid_var=tk.StringVar()
        self.booktitle_var=tk.StringVar()
        self.auther_var=tk.StringVar()
        self.dateborroewd_var=tk.StringVar()
        self.datedue_var=tk.StringVar()
        self.dayonbook_var=tk.StringVar()
        self.lateratefine_var=tk.StringVar()
        self.dateoverdue_var=tk.StringVar()
        self.finalprice_var=tk.StringVar()



        self.member_var=StringVar()
        self.pnr_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborroewd_var=StringVar()
        self.datedue_var=StringVar()
        self.dayonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        

        # Title Label
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, 
                         font=("Times New Roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

    
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=12, relief=RIDGE, 
                                   font=("Times New Roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type:", font=("arial", 15, "bold"))
        lblMember.grid(row=0, column=0, sticky="W")
        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var, state="readonly", font=("arial", 12, "bold"), width=29)
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN_No:", font=("arial", 13, "bold"), padx=2)
        lblPRN_No.grid(row=1, column=0, sticky="W")
        txtPRN_No = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.pnr_var,width=29)
        txtPRN_No.grid(row=1, column=1)


         # ID Number
        lblID_No = Label(DataFrameLeft, bg="powder blue", text="ID Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblID_No.grid(row=2, column=0, sticky="W")
        txtID_No = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.id_var,width=29)
        txtID_No.grid(row=2, column=1)

        # First Name
        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky="W")
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3, column=1)

        # Last Name
        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky="W")
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4, column=1)

        # Address Line 1
        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address Line 1:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky="W")
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5, column=1)

        # Address Line 2
        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address Line 2:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky="W")
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable= self.address2_var,width=29)
        txtAddress2.grid(row=6, column=1)

        # Post Code
        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code:", font=("arial", 12, "bold"), padx=2, pady=4)
        lblPostCode.grid(row=7, column=0, sticky="W")
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7, column=1)

        # Mobile Number
        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky="W")
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8, column=1)

        # Book ID
        lblBookID = Label(DataFrameLeft, bg="powder blue", text="Book ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookID.grid(row=0, column=2, sticky="W")
        txtBookID = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.bookid_var,width=29)
        txtBookID.grid(row=0, column=3)

        # Book Title
        lblBookTitle =Label(DataFrameLeft, bg="powder blue", text="Book Title:", font=("arial", 12, "bold"), padx=2, pady=4)
        lblBookTitle.grid(row=1, column=2, sticky="W")
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1, column=3)

        # Author Name
        lblAuthorName = Label(DataFrameLeft, bg="powder blue", text="Author Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAuthorName.grid(row=2, column=2, sticky="W")
        txtAuthorName = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.auther_var,width=29)
        txtAuthorName.grid(row=2, column=3)

        # Date Borrowed
        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky="W")
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.dateborroewd_var,width=29)
        txtDateBorrowed.grid(row=3, column=3)

        # Date Due
        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky="W")
        txtDateDue = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4, column=3)

        # Days on Book
        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days on Book:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky="W")
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.dayonbook_var,width=29)
        txtDaysOnBook.grid(row=5, column=3)

        # Last Return Fine
        lblLastReturnFine = Label(DataFrameLeft, bg="powder blue", text="Last Return Fine:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLastReturnFine.grid(row=6, column=2, sticky="W")
        txtLastReturnFine = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.lateratefine_var,width=29)
        txtLastReturnFine.grid(row=6, column=3)

        # Date Overdue
        lblDateOverdue = Label(DataFrameLeft, bg="powder blue", text="Date Overdue:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOverdue.grid(row=7, column=2, sticky="W")
        txtDateOverdue = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverdue.grid(row=7, column=3)

        # Actual Price
        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky="W")
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8, column=3)

#=================Data fram righr======#
     
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12, relief=RIDGE, 
                                    font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.textBox=Text(DataFrameRight, font=("arial", 12, "bold"),width=32,height=16,padx=2,pady=6)
        self.textBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBoooks=['C','C++','C#','Python','Java','Data Structure Algorithm','Database Management System','JQuery',
                 'Node js','React js','Java script','PHP','Android Application','Flutter','CSS','HTML','Software Engineering',"Cyber security"]
        
        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "C#":
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("C# Essentials: A Developer's Guide")
                self.auther_var.set(" Emily Clark")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborroewd_var.set(d1)
            self.datedue_var.set(d3)
            self.dayonbook_var.set(15)
            self.lateratefine_var.set("Rs.50")
            self.dateoverdue_var.set("No")
            self.finalprice_var.set("Rs.775")


            if x == "Node js":
                self.bookid_var.set("BDKID5454")
                self.booktitle_var.set("Node.js for Real-Time Applications")
                self.auther_var.set("Emma Green")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.10")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.275")

            elif x == "PHP":
                self.bookid_var.set("VKID5454")
                self.booktitle_var.set("PHP: A Complete Web Developer's Guide")
                self.auther_var.set(" Daniel Smith")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.500")

            elif x == "Java":
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Java for Web and Mobile Developers")
                self.auther_var.set("Michael Johnson")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.455")

            elif x == "Python Programming: From Beginner to Expert":
                self.bookid_var.set("LKID5454")
                self.booktitle_var.set("Thomsol")
                self.auther_var.set(" John Smith")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.10")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.70")

            elif x == "Data Structure Algorithm":
                self.bookid_var.set("SKID5454")
                self.booktitle_var.set("Data Structures and Algorithms for Coders")
                self.auther_var.set(" Sarah Lee")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.255")

            elif x == "C":
                self.bookid_var.set("MKID5454")
                self.booktitle_var.set("Mastering C Programming")
                self.auther_var.set("John Doe")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.#0")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.300")

            elif x == "C++":
                self.bookid_var.set("DFKID5454")
                self.booktitle_var.set("C++ Programming for Professionals")
                self.auther_var.set(" Alex Bennett")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.40")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1400")

            elif x == "HTML":
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("CSS and HTML: Designing the Web")
                self.auther_var.set("Julia Green")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.90")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.200")

            elif x == "CSS":
                self.bookid_var.set("BKID54DT4")
                self.booktitle_var.set("CSS and HTML: Designing the Web")
                self.auther_var.set("Julia Green")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.70")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.900")
            elif x == "React js":
                self.bookid_var.set("OKID54DT4")
                self.booktitle_var.set("React.js: Build Modern Web Apps")
                self.auther_var.set(" Mark Taylor")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.(0")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.100")

            elif x == "JQuery":
                self.bookid_var.set("JKID54DT4")
                self.booktitle_var.set("Learning jQuery: The Power of JavaScript Frameworks")
                self.auther_var.set(" Robert Brown")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.200")

            elif x == "Android Application":
                self.bookid_var.set("DKID54DT4")
                self.booktitle_var.set("Android Application Development: Build Your First App")
                self.auther_var.set("Olivia Davis")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.95")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1200")   

            elif x == "Software Engineering":
                self.bookid_var.set("KKID54DT4")
                self.booktitle_var.set("Software Engineering Best Practices")
                self.auther_var.set(" James Taylor")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.58")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1000")

            elif x == "Java script":
                self.bookid_var.set("BHID54DT4")
                self.booktitle_var.set("JavaScript and Web Development Mastery")
                self.auther_var.set("Jennifer White")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.850")  


            elif x == "Database Management System":
                self.bookid_var.set("KHID54DT4")
                self.booktitle_var.set("Mastering Database Management Systems")
                self.auther_var.set("David Williams")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.120")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1450")  

            elif x == "Flutter":
                self.bookid_var.set("FHID54DT4")
                self.booktitle_var.set("Flutter: Cross-Platform App Developmen")
                self.auther_var.set("Thomas Lee")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.220")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1870")

            elif x == "Cyber security":
                self.bookid_var.set("FHID54DT4")
                self.booktitle_var.set("Cybersecurity Fundamentals: Protecting Your Digital World")
                self.auther_var.set("Lisa Brown")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborroewd_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.lateratefine_var.set("Rs.60")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1070")              
            else:
                    print("Invalid choice")                               




        listBox=Listbox(DataFrameRight,font=("arial", 12, "bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
                listBox.insert(END, item)

        # Button Frame
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        # Add Data button
        print("add_data method exists:", hasattr(self, 'add_data')) 
        btnAddData = tk.Button(Framebutton, text="Add Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(Framebutton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white",command=self.showData)
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(Framebutton, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white",command=self.update)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Framebutton, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white",command=self.delete)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.reset)
        btnReset.grid(row=0, column=4)

        btnExit = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.iExit)
        btnExit.grid(row=0, column=5)

      
        FrameDetail = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetail.place(x=0, y=590, width=1530, height=210)


        Table_frame = Frame(FrameDetail, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=4,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table = ttk.Treeview(
        Table_frame,
        columns=('membertype', 'pnrno', 'id', 'firstname', 'lastname', 'address1', 'address2', 'postid', 'mobile',
             'bookid', 'booktitle', 'auther', 'dateborrowed', "datedue", 'days', 'laterefundfine', 'dateoverdue', 
             'finalprice'),
            xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set
)



        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("pnrno",text="PNR_No")
        self.library_table.heading("id",text="ID")
        self.library_table.heading("firstname",text="FirstName")
        self.library_table.heading("lastname",text="LastName")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="BookTitle")
        self.library_table.heading("auther",text="Authe Name")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("laterefundfine",text="Last return Fine")
        self.library_table.heading("dateoverdue",text="Date OverDue")
        self.library_table.heading("finalprice",text="Actual Price")

        self.library_table['show'] = "headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("pnrno", width=100)
        self.library_table.column("id", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("laterefundfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)  
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    
    def iExit(self):
        """Exit confirmation method."""
        iExit = messagebox.askyesno("Library Management System", "Do you want to Exit?")
        if iExit > 0:
            self.root.destroy() 
            return
   
    def reset(self):
        """Reset all fields and clear the text box."""
        self.member_var.set("")
        self.pnr_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborroewd_var.set("")
        self.datedue_var.set("")
        self.dayonbook_var.set("")
        self.lateratefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.textBox.delete("1.0",END)         
     #Add Data   
    def add_data(self):
        try:
            
            conn = mysql.connector.connect(host='localhost', username='root', password='', database='python_db')
            if conn.is_connected():
                my_cursor = conn.cursor()
                query = """
                INSERT INTO library_data (member, pnr, id, firstname, lastname, address1, address2, postcode, mobile, bookid, booktitle, author, dateborrowed, datedue, days, laterefundfine, dateoverdue, finalprice)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s);
                                                                                            """

                data=(
                     
                    self.member_var.get(),
                    self.pnr_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.auther_var.get(),
                    self.dateborroewd_var.get(),
                    self.datedue_var.get(),
                    self.dayonbook_var.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue_var.get(),
                    self.finalprice_var.get()

               )
                

               
            if len(data) == 18:
                    my_cursor.execute(query, data)
                    conn.commit()  

                    self.fetch_data()

                    conn.close() 

                    
                    messagebox.showinfo("Success", "Data has been inserted successfully!")

            else:
                    print("Data mismatch: The number of fields does not match the number of columns in the table.")
                    messagebox.showerror("Error", "Column count mismatch.")

        except mysql.connector.Error as err:
            
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Failed to insert data: {err}")
   
    #Fetch Data
    def fetch_data(self):
        try:
           
            conn = mysql.connector.connect(host='localhost', username='root', password='', database='python_db')
            my_cursor = conn.cursor()

           
            my_cursor.execute("SELECT * FROM library_data")
            rows = my_cursor.fetchall()

            
            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())  

           
                for row in rows:
                    self.library_table.insert("", "end", values=row)

            
            conn.close()

        except mysql.connector.Error as err:
           
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Failed to fetch data: {err}")
     
    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus() 
        content = self.library_table.item(cursor_row)  
        row = content['values']  
        self.member_var.set(row[0])
        self.pnr_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborroewd_var.set(row[12])
        self.datedue_var.set(row[13])
        self.dayonbook_var.set(row[14])
        self.lateratefine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def showData(self):
        self.textBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")  
        self.textBox.insert(END,"PNR_No:\t\t"+self.pnr_var.get()+"\n")  
        self.textBox.insert(END,"ID:\t\t"+self.id_var.get()+"\n")  
        self.textBox.insert(END,"FirstName:\t\t"+self.firstname_var.get()+"\n")  
        self.textBox.insert(END,"LastName:\t\t"+self.lastname_var.get()+"\n")  
        self.textBox.insert(END,"Address1:\t\t"+self.address1_var.get()+"\n")  
        self.textBox.insert(END,"Address2:\t\t"+self.address2_var.get()+"\n")  
        self.textBox.insert(END,"Post Code:\t\t"+self.postcode_var.get()+"\n")  
        self.textBox.insert(END,"Mobile:\t\t"+self.mobile_var.get()+"\n")  
        self.textBox.insert(END,"BookId:\t\t"+self.bookid_var.get()+"\n")  
        self.textBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")  
        self.textBox.insert(END,"Auther:\t\t"+self.auther_var.get()+"\n")  
        self.textBox.insert(END,"DateBorroewd:\t\t"+self.dateborroewd_var.get()+"\n")  
        self.textBox.insert(END,"DateDue:\t\t"+self.datedue_var.get()+"\n")  
        self.textBox.insert(END,"DayOnBook:\t\t"+self.dayonbook_var.get()+"\n")  
        self.textBox.insert(END,"LateRateFine:\t\t"+self.lateratefine_var.get()+"\n")  
        self.textBox.insert(END,"DataOverDue:\t\t"+self.dateoverdue_var.get()+"\n")  
        self.textBox.insert(END,"FinalPrice:\t\t"+self.finalprice_var.get()+"\n") 

    def update(self):
        """This method will handle updating records."""
        try:
           
            conn = mysql.connector.connect(host='localhost', username='root', password='', database='python_db')
            if conn.is_connected():
                my_cursor = conn.cursor()

            
                query_check = "SELECT * FROM library_data WHERE pnr = %s"
                value_check = (self.pnr_var.get(),)
                my_cursor.execute(query_check, value_check)
                record = my_cursor.fetchone()

                if record:
                
                    query = """
                    UPDATE library_data
                    SET member = %s, id = %s, firstname = %s, lastname = %s, address1 = %s, address2 = %s, postcode = %s, 
                        mobile = %s, bookid = %s, booktitle = %s, author = %s, dateborrowed = %s, datedue = %s, days = %s, 
                        laterefundfine = %s, dateoverdue = %s, finalprice = %s
                    WHERE pnr = %s;
                    """
                    
               
                    data = (
                        self.member_var.get(),
                        self.id_var.get(),
                        self.firstname_var.get(),
                        self.lastname_var.get(),
                        self.address1_var.get(),
                        self.address2_var.get(),
                        self.postcode_var.get(),
                        self.mobile_var.get(),
                        self.bookid_var.get(),
                        self.booktitle_var.get(),
                        self.auther_var.get(),
                        self.dateborroewd_var.get(),
                        self.datedue_var.get(),
                        self.dayonbook_var.get(),
                        self.lateratefine_var.get(),
                        self.dateoverdue_var.get(),
                        self.finalprice_var.get(),
                        self.pnr_var.get()  
                    )

                   
                    my_cursor.execute(query, data)
                    conn.commit()

                    self.fetch_data()
                    self.reset()

                   
                    conn.close()

                    messagebox.showinfo("Success", "Member has been updated")
                else:
                    messagebox.showinfo("Error", "Record not found with the provided PNR")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Failed to update member: {err}")

    def delete(self):
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='', database='python_db')
            if conn.is_connected():
                my_cursor = conn.cursor()

                
                query_check = "SELECT * FROM library_data WHERE id = %s"
                value_check = (self.id_var.get(),)
                my_cursor.execute(query_check, value_check)
                record = my_cursor.fetchone()
                
                if record:
                    
                    query_delete = "DELETE FROM library_data WHERE id = %s"
                    my_cursor.execute(query_delete, value_check)
                    conn.commit()
                    
                    
                    self.fetch_data()

                    
                    self.reset()

              
                    messagebox.showinfo("Success", "Record deleted successfully!")
                else:
                    messagebox.showinfo("Error", "Record not found with the provided ID.")
                
                conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Failed to delete record: {err}")



                               
if __name__ == "__main__":                      
    root = tk.Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()  