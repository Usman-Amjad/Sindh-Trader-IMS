# -------Importing Modules
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import ImageTk

# ===== Global Variable =====
switch_value = True


class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+200+130")
        self.root.title("UA")
        self.root.config(bg="#333333")
        self.root.focus_force()
        # ========================================
        # ============ All variables ===========
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()  # Date of Birth
        self.var_doj = StringVar()  # Date of joining
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()  # User Type
        self.var_salary = StringVar()

        # ===== Style =====
        self.style = ttk.Style(self.root)

        icon = PhotoImage(file='images/logoB.png')
        self.root.iconphoto(False, icon)

        # ====== Title =======
        self.title = Label(self.root, text="Return Products", font=("Brush Script MT", 38, "bold")
                           , bg="#333333", fg="white", anchor="n")
        self.title.pack(side=TOP, fill=X)

        # ===== Logo Image =====
        self.logo = ImageTk.PhotoImage(file="images/logoB.png")
        self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

        # ====== Search Frame ======
        self.SearchFrame = LabelFrame(self.root, text="Search employee", font=("goudy old style", 12, "bold"), bd=2,
                                      relief=RIDGE, bg="#333333", fg='#F2F2F2')
        self.SearchFrame.place(x=250, y=70, width=600, height=70)

        # ====== Options ======
        cmb_search = ttk.Combobox(self.SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        self.txtSearch = Entry(self.SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15),
                               bg="#F2F2F2", fg='#000000', insertbackground='#333333')
        self.txtSearch.place(x=200, y=10)

        btn_search = Button(self.SearchFrame, text="Search", command=self.search, font=("goudy old style", 15),
                            bg="#4caf50",
                            fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

        # ====== Title ======
        title = Label(self.root, text="Employee Details", font=("goudy old style", 15, 'bold'), bg="#0f4d7d",
                      fg="white").place(
            x=50, y=150, width=1000)

        # ===== Content ======
        # ====== Row 1 ======
        # Label Styling
        backgroundColor = '#333333'
        foregroundColor = '#F2F2F2'
        fontStyle = ("Agency FB", 17, 'bold')

        # Entry Box Styling
        entryBg = "#F2F2F2"
        entryFg = "#000000"
        entryInsertBg = "#333333"

        self.lblEmpId = Label(self.root, text="Emp Id", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblEmpId.place(x=50, y=200)
        self.lblGender = Label(self.root, text="Gender", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblGender.place(x=350, y=200)
        self.lblContact = Label(self.root, text="Contact", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblContact.place(x=750, y=200)

        self.txtEmpId = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 15),
                              bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtEmpId.place(x=150, y=200, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                  values=("Select", "Male", "Female", "Other"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15))
        cmb_gender.place(x=500, y=200, width=180)
        cmb_gender.current(0)

        self.txtContact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15),
                                bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtContact.place(x=850, y=200, width=180)

        # ====== Row 2 ======
        self.lblName = Label(self.root, text="Name", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblName.place(x=50, y=240)
        self.lblDob = Label(self.root, text="D.O.B", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblDob.place(x=350, y=240)
        self.lblDoj = Label(self.root, text="D.O.J", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblDoj.place(x=750, y=240)

        self.txtName = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),
                             bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtName.place(x=150, y=240, width=180)
        self.txtDob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15),
                            bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtDob.place(x=500, y=240, width=180)
        self.txtDoj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 15),
                            bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtDoj.place(x=850, y=240, width=180)

        # ====== Row 3 ======
        self.lblEmail = Label(self.root, text="Email", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblEmail.place(x=50, y=280)
        self.lblPass = Label(self.root, text="Password", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblPass.place(x=350, y=280)
        self.lblUtype = Label(self.root, text="User Type", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblUtype.place(x=750, y=280)

        self.txtEmail = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15),
                              bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtEmail.place(x=150, y=280, width=180)
        self.txtPass = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 15),
                             bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtPass.place(x=500, y=280, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype,
                                 values=("Admin", "Employee"), state='readonly', justify=CENTER,
                                 font=("goudy old style", 15))
        cmb_utype.place(x=850, y=280, width=180)
        cmb_utype.current(0)

        # ====== Row 4 ======
        self.lblAddress = Label(self.root, text="Address", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblAddress.place(x=50, y=330)
        self.lblSalary = Label(self.root, text="Salary", font=fontStyle, bg=backgroundColor, fg=foregroundColor)
        self.lblSalary.place(x=500, y=330)

        self.txtAddress = Text(self.root, font=("goudy old style", 15),
                               bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtAddress.place(x=150, y=330, width=300, height=60)
        self.txtSalary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 15),
                               bg=entryBg, fg=entryFg, insertbackground=entryInsertBg)
        self.txtSalary.place(x=580, y=330, width=180)

        # ====== Buttons ======
        self.addIcon = ImageTk.PhotoImage(file="images/add.png")
        self.btn_add = Button(self.root, text="Add", image=self.addIcon, font=("Agency FB", 15),
                              bg="#333333",
                              fg="white",
                              cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_add.place(x=570, y=370)
        self.btn_add.bind("<Return>", self.add)
        self.btn_add.bind("<ButtonRelease-1>", self.add)

        self.updateIcon = ImageTk.PhotoImage(file="images/update.png")
        self.btn_update = Button(self.root, text="Update", image=self.updateIcon, font=("Agency FB", 15),
                                 bg="#333333",
                                 fg="white",
                                 cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_update.place(x=670, y=370)
        self.btn_update.bind("<Return>", self.update)
        self.btn_update.bind("<ButtonRelease-1>", self.update)

        self.deleteIcon = ImageTk.PhotoImage(file="images/delete.png")
        self.btn_delete = Button(self.root, text="Delete", image=self.deleteIcon, font=("Agency FB", 15),
                                 bg="#333333",
                                 fg="white",
                                 cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_delete.place(x=770, y=370)
        self.btn_delete.bind("<Return>", self.delete)
        self.btn_delete.bind("<ButtonRelease-1>", self.delete)

        self.clearIcon = ImageTk.PhotoImage(file="images/clear.png")
        self.btn_clear = Button(self.root, text="Clear All", image=self.clearIcon, font=("Agency FB", 15),
                                bg="#333333",
                                fg="white",
                                cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_clear.place(x=860, y=360)
        self.btn_clear.bind("<Return>", self.clear)
        self.btn_clear.bind("<ButtonRelease-1>", self.clear)

        # ====== Employee Details ======
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=450, relwidth=1, height=150)

        self.style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333",
                             rowheight=30,
                             font=("Arial", 12))
        self.style.map("Treeview", background=[("selected", "#0078D7")])  # added blue color when a row is selected
        self.style.configure("Treeview.Heading", font=('Constantia', 12))
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, style='Treeview', columns=(
            "eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        for column in self.EmployeeTable["columns"]:
            self.EmployeeTable.column(column, anchor=CENTER)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=60, minwidth=60)
        self.EmployeeTable.column("name", width=140, minwidth=140)
        self.EmployeeTable.column("email", width=140, minwidth=140)
        self.EmployeeTable.column("gender", width=140, minwidth=140)
        self.EmployeeTable.column("contact", width=140, minwidth=140)
        self.EmployeeTable.column("dob", width=140, minwidth=140)
        self.EmployeeTable.column("doj", width=140, minwidth=140)
        self.EmployeeTable.column("pass", width=140, minwidth=140)
        self.EmployeeTable.column("utype", width=140, minwidth=140)
        self.EmployeeTable.column("address", width=140, minwidth=140)
        self.EmployeeTable.column("salary", width=140, minwidth=140)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()
        # ====== Dark or Light Mode ======
        self.light = ImageTk.PhotoImage(file="images/light-mode1.png")
        self.dark = ImageTk.PhotoImage(file="images/dark-mode.png")

        self.themeBtn = Button(self.root, image=self.dark, bg='#333333', activebackground='#333333', bd=0,
                               cursor="hand2")
        self.themeBtn.place(x=1000, y=30, width=80, height=30)
        self.themeBtn.bind("<ButtonRelease-1>", self.toggle)
        # ========================================================================================

    def toggle(self, e):
        global switch_value
        if switch_value is False:
            self.themeBtn.config(image=self.dark)

            # Changes the window to dark theme
            self.root.config(bg="#333333")
            self.title.config(bg="#333333", fg="#F2F2F2")
            self.themeBtn.config(bg="#333333", activebackground="#333333")
            self.SearchFrame.config(bg="#333333", fg="white", bd=2, relief=RIDGE)

            self.lblEmpId.config(bg="#333333", fg="#F2F2F2")
            self.lblGender.config(bg="#333333", fg="#F2F2F2")
            self.lblContact.config(bg="#333333", fg="#F2F2F2")
            self.lblName.config(bg="#333333", fg="#F2F2F2")
            self.lblDob.config(bg="#333333", fg="#F2F2F2")
            self.lblDoj.config(bg="#333333", fg="#F2F2F2")
            self.lblEmail.config(bg="#333333", fg="#F2F2F2")
            self.lblPass.config(bg="#333333", fg="#F2F2F2")
            self.lblUtype.config(bg="#333333", fg="#F2F2F2")
            self.lblAddress.config(bg="#333333", fg="#F2F2F2")
            self.lblSalary.config(bg="#333333", fg="#F2F2F2")

            self.txtSearch.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtEmpId.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtContact.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtName.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtDob.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtDoj.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtEmail.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtPass.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtAddress.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")
            self.txtSalary.config(bg="#F2F2F2", fg="black", insertbackground="#F2F2F2")

            self.logo = ImageTk.PhotoImage(file="images/logoB.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            switch_value = True
        else:
            self.themeBtn.config(image=self.light)

            # Changes the window to light theme
            self.root.config(bg="#F2F2F2")
            self.title.config(bg="#F2F2F2", fg="black")
            self.themeBtn.config(bg="#F2F2F2", activebackground="#F2F2F2")
            self.SearchFrame.config(bg="#F2F2F2", fg="black", bd=0)

            self.lblEmpId.config(bg="#F2F2F2", fg="#333333")
            self.lblGender.config(bg="#F2F2F2", fg="#333333")
            self.lblContact.config(bg="#F2F2F2", fg="#333333")
            self.lblName.config(bg="#F2F2F2", fg="#333333")
            self.lblDob.config(bg="#F2F2F2", fg="#333333")
            self.lblDoj.config(bg="#F2F2F2", fg="#333333")
            self.lblEmail.config(bg="#F2F2F2", fg="#333333")
            self.lblPass.config(bg="#F2F2F2", fg="#333333")
            self.lblUtype.config(bg="#F2F2F2", fg="#333333")
            self.lblAddress.config(bg="#F2F2F2", fg="#333333")
            self.lblSalary.config(bg="#F2F2F2", fg="#333333")

            self.txtSearch.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtEmpId.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtContact.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtName.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtDob.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtDoj.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtEmail.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtPass.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtAddress.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")
            self.txtSalary.config(bg="#333333", fg="#F2F2F2", insertbackground="#F2F2F2")

            self.logo = ImageTk.PhotoImage(file="images/logoW.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            switch_value = False

    def add(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try different", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txtAddress.get('1.0', END),
                            self.var_salary.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        try:
            f = self.EmployeeTable.focus()
            content = (self.EmployeeTable.item(f))
            row = content['values']
            self.var_emp_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.var_dob.set(row[5])
            self.var_doj.set(row[6])
            self.var_pass.set(row[7])
            self.var_utype.set(row[8])
            self.txtAddress.delete('1.0', END),
            self.txtAddress.insert(END, row[9]),
            self.var_salary.set(row[10])
        except (Exception,):
            pass

    def update(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? WHERE eid=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txtAddress.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear(e)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self, e):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txtAddress.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Select input should be required", parent=self.root)
            else:
                cur.execute(
                    "SELECT * FROM employee WHERE " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
