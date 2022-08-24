# -------Importing Modules
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk

switch_value = True


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+220+145")
        self.root.title("UA")
        self.root.config(bg="#333333")
        self.root.focus_force()

        # ===== Style =====
        style = ttk.Style(self.root)

        icon = PhotoImage(file='images/logoB.png')
        self.root.iconphoto(False, icon)

        # ================== Variables ======================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_loc = StringVar()

        self.cat_list = []  # List Variable
        self.loc_list = []  # List Variable
        self.fetch_cat_loc()  # Calling Function

        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        # ====== Title =======
        self.title = Label(self.root, text="Manage Product Details", font=("Brush Script MT", 50, "bold")
                           , bg="#333333", fg="white", anchor="n")
        self.title.pack(side=TOP, fill=X)

        self.logo = ImageTk.PhotoImage(file="images/logoB.png")
        self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

        # ==============================================================
        self.product_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#333333")
        self.product_Frame.place(x=10, y=100, width=450, height=480)

        titleBg = '#333333'
        titleFg = 'white'
        titleFont = ('Agency FB', 18)

        # ====== Column 1 ======
        self.lbl_category = Label(self.product_Frame, text="Category", font=(titleFont), bg=titleBg, fg=titleFg)
        self.lbl_category.place(x=30, y=60)

        self.lbl_location = Label(self.product_Frame, text="Location", font=(titleFont), bg=titleBg, fg=titleFg)
        self.lbl_location.place(x=30, y=110)

        self.lbl_product_name = Label(self.product_Frame, text="Name", font=(titleFont), bg=titleBg, fg=titleFg)
        self.lbl_product_name.place(x=30, y=160)

        self.lbl_price = Label(self.product_Frame, text="Price", font=(titleFont), bg=titleBg, fg=titleFg)
        self.lbl_price.place(x=30, y=210)

        self.lbl_qty = Label(self.product_Frame, text="Quantity", font=(titleFont), bg=titleBg, fg=titleFg)
        self.lbl_qty.place(x=30, y=260)

        self.lbl_status = Label(self.product_Frame, text="Status", font=(titleFont), bg=titleBg, fg=titleFg)
        self.lbl_status.place(x=30, y=310)

        # ====== Column 2 ======
        cmb_cat = ttk.Combobox(self.product_Frame, textvariable=self.var_cat,
                               values=self.cat_list, state='readonly', justify=CENTER,
                               font=("Agency FB", 17))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_loc = ttk.Combobox(self.product_Frame, textvariable=self.var_loc,
                               values=self.loc_list, state='readonly', justify=CENTER,
                               font=("Agency FB", 17))
        cmb_loc.place(x=150, y=110, width=200)
        cmb_loc.current(0)

        txt_name = Entry(self.product_Frame, textvariable=self.var_name,
                         font=("goudy old style", 17),
                         bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=150, y=160, width=200)
        txt_price = Entry(self.product_Frame, textvariable=self.var_price,
                          font=("goudy old style", 17),
                          bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=150, y=210, width=200)
        txt_qty = Entry(self.product_Frame, textvariable=self.var_qty,
                        font=("goudy old style", 17),
                        bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=150, y=260, width=200)

        cmb_status = ttk.Combobox(self.product_Frame, textvariable=self.var_status,
                                  values=("Active", "Inactive"), state='readonly', justify=CENTER,
                                  font=("Agency FB", 17))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        # ====== Buttons ======
        self.addIcon = ImageTk.PhotoImage(file="images/add.png")
        self.btn_add = Button(self.product_Frame, text="Add", image=self.addIcon, font=("Agency FB", 15),
                              bg="#333333",
                              fg="white",
                              cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_add.place(x=30, y=380)
        self.btn_add.bind("<Return>", self.add)
        self.btn_add.bind("<ButtonRelease-1>", self.add)

        self.updateIcon = ImageTk.PhotoImage(file="images/update.png")
        self.btn_update = Button(self.product_Frame, text="Update", image=self.updateIcon, font=("Agency FB", 15),
                                 bg="#333333",
                                 fg="white",
                                 cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_update.place(x=140, y=380)
        self.btn_update.bind("<Return>", self.update)
        self.btn_update.bind("<ButtonRelease-1>", self.update)

        self.deleteIcon = ImageTk.PhotoImage(file="images/delete.png")
        self.btn_delete = Button(self.product_Frame, text="Delete", image=self.deleteIcon, font=("Agency FB", 15),
                                 bg="#333333",
                                 fg="white",
                                 cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_delete.place(x=250, y=380)
        self.btn_delete.bind("<Return>", self.delete)
        self.btn_delete.bind("<ButtonRelease-1>", self.delete)

        self.clearIcon = ImageTk.PhotoImage(file="images/clear.png")
        self.btn_clear = Button(self.product_Frame, text="Clear All", image=self.clearIcon, font=("Agency FB", 15),
                                bg="#333333",
                                fg="white",
                                cursor="hand2", borderwidth=0, compound=TOP)
        self.btn_clear.place(x=350, y=370)
        self.btn_clear.bind("<Return>", self.clear)
        self.btn_clear.bind("<ButtonRelease-1>", self.clear)

        # ====== Search Frame ======
        self.SearchFrame = LabelFrame(self.root, text="Search Product", fg='white',
                                      font=("goudy old style", 12, "bold"),
                                      bd=2,
                                      relief=RIDGE, bg="#333333")
        self.SearchFrame.place(x=480, y=90, width=600, height=80)

        cmb_search = ttk.Combobox(self.SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Category", "Location", "Name"), state='readonly', justify=CENTER,
                                  font=("Agency FB", 17))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(self.SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 17),
                           bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=198, y=10, width=200)

        self.searchIcon = ImageTk.PhotoImage(file='images/search.png')
        self.btn_search = Button(self.SearchFrame, text='Search', image=self.searchIcon, command=self.search, font=("goudy old style", 17),
                                 bg="#333333", fg='#F2F2F2', activebackground='#333333', cursor="hand2", borderwidth=0, compound=LEFT)
        self.btn_search.place(x=430, y=2)

        # ====== Product Details ======
        self.p_Frame = Frame(self.root, bg='white', bd=1)
        self.p_Frame.place(x=480, y=180, width=600, height=390)

        style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333", rowheight=30,
                        font=("Arial", 12))
        style.map("Treeview", background=[("selected", "#0078D7")])
        style.configure("Treeview.Heading", font=('Constantia', 12))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        scrolly = Scrollbar(self.p_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.p_Frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(self.p_Frame, style="Treeview", columns=(
            "pid", "category", "name", "price", "qty", "totalPrice", "status", "location"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        for column in self.product_table["columns"]:
            self.product_table.column(column, anchor=CENTER)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="Id")
        self.product_table.heading("category", text="Category")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Qty")
        self.product_table.heading("totalPrice", text="Total Price")
        self.product_table.heading("status", text="Status")
        self.product_table.heading("location", text="Location")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=80, minwidth=80)
        self.product_table.column("category", width=120, minwidth=120)
        self.product_table.column("name", width=100, minwidth=100)
        self.product_table.column("price", width=100, minwidth=100)
        self.product_table.column("qty", width=100, minwidth=100)
        self.product_table.column("totalPrice", width=100, minwidth=100)
        self.product_table.column("status", width=100, minwidth=100)
        self.product_table.column("location", width=100, minwidth=100)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        # ====== Dark or Light Mode ======
        self.light = ImageTk.PhotoImage(file="images/light-mode1.png")
        self.dark = ImageTk.PhotoImage(file="images/dark-mode.png")

        self.themeBtn = Button(self.root, image=self.dark, bg='#333333', activebackground='#333333', bd=0,
                               cursor="hand2")
        self.themeBtn.place(x=1000, y=30, width=80, height=30)
        self.themeBtn.bind("<ButtonRelease-1>", self.toggle)

        self.show()

    # ========================= Functions ==============================

    def toggle(self, e):
        global switch_value
        if switch_value is False:
            self.themeBtn.config(image=self.dark)

            # Changes the window to dark theme
            self.root.config(bg="#333333")
            self.title.config(bg="#333333", fg="white")
            self.themeBtn.config(bg="#333333", activebackground="#333333")
            self.product_Frame.config(bg="#333333", bd=2, relief=RIDGE)
            self.SearchFrame.config(bg="#333333", fg="white", bd=2, relief=RIDGE)
            self.p_Frame.config(bg="#ffffff", bd=1)

            self.logo = ImageTk.PhotoImage(file="images/logoB.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            self.lbl_category.config(bg="#333333", fg="white", activebackground="#333333")
            self.lbl_location.config(bg="#333333", fg="white", activebackground="#333333")
            self.lbl_product_name.config(bg="#333333", fg="white", activebackground="#333333")
            self.lbl_price.config(bg="#333333", fg="white", activebackground="#333333")
            self.lbl_qty.config(bg="#333333", fg="white", activebackground="#333333")
            self.lbl_status.config(bg="#333333", fg="white", activebackground="#333333")

            self.btn_add.config(bg="#333333", fg='#F2F2F2', activebackground="#333333")
            self.btn_update.config(bg="#333333", fg='#F2F2F2', activebackground="#333333")
            self.btn_delete.config(bg="#333333", fg='#F2F2F2', activebackground="#333333")
            self.btn_clear.config(bg="#333333", fg='#F2F2F2', activebackground="#333333")
            self.btn_search.config(bg="#333333", fg='#F2F2F2', activebackground="#333333")
            switch_value = True
        else:
            self.themeBtn.config(image=self.light)

            # Changes the window to light theme
            self.root.config(bg="#F2F2F2")
            self.title.config(bg="#F2F2F2", fg="black")
            self.themeBtn.config(bg="#F2F2F2", activebackground="#F2F2F2")
            self.product_Frame.config(bg="#F2F2F2", bd=0)
            self.SearchFrame.config(bg="#F2F2F2", fg="black", bd=0)
            self.p_Frame.config(bg="#F2F2F2", bd=0)

            self.logo = ImageTk.PhotoImage(file="images/logoW.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            self.lbl_category.config(bg="#F2F2F2", fg="black", activebackground="#F2F2F2")
            self.lbl_location.config(bg="#F2F2F2", fg="black", activebackground="#F2F2F2")
            self.lbl_product_name.config(bg="#F2F2F2", fg="black", activebackground="#F2F2F2")
            self.lbl_price.config(bg="#F2F2F2", fg="black", activebackground="#F2F2F2")
            self.lbl_qty.config(bg="#F2F2F2", fg="black", activebackground="#F2F2F2")
            self.lbl_status.config(bg="#F2F2F2", fg="black", activebackground="#F2F2F2")

            self.btn_add.config(bg="#F2F2F2", fg='#333333', activebackground="#F2F2F2")
            self.btn_update.config(bg="#F2F2F2", fg='#333333', activebackground="#F2F2F2")
            self.btn_delete.config(bg="#F2F2F2", fg='#333333', activebackground="#F2F2F2")
            self.btn_clear.config(bg="#F2F2F2", fg='#333333', activebackground="#F2F2F2")
            self.btn_search.config(bg="#F2F2F2", fg='#333333', activebackground="#F2F2F2")
            switch_value = False

    def fetch_cat_loc(self):
        self.cat_list.append("Empty")
        self.loc_list.append("Empty")

        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("SELECT name FROM locations")
            loc = cur.fetchall()
            if len(loc) > 0:
                del self.loc_list[:]
                self.loc_list.append("Select")
                for i in loc:
                    self.loc_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def add(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        total = int(self.var_price.get()) * int(self.var_qty.get())
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    op = messagebox.showinfo("Info",
                                             "Product already present, if you want to add more then press update button",
                                             parent=self.root)
                    if op == True:
                        cur.execute(
                            "INSERT INTO product(category,name,price,qty,totalPrice,status,location) values(?,?,?,?,?,?,?)",
                            (
                                self.var_cat.get(),
                                self.var_name.get(),
                                self.var_price.get(),
                                self.var_qty.get(),
                                total,
                                self.var_status.get(),
                                self.var_loc.get(),
                            ))
                        con.commit()
                        messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        try:
            f = self.product_table.focus()
            content = (self.product_table.item(f))
            row = content['values']
            self.var_pid.set(row[0])
            self.var_cat.set(row[1])
            self.var_name.set(row[2])
            self.var_price.set(row[3])
            self.var_qty.set(row[4])
            self.var_status.set(row[6])
            self.var_loc.set(row[7])
        except (Exception,):
            pass

    def update(self, e):
        try:
            con = sqlite3.connect(database=r'std.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
            row = cur.fetchone()
            Quant = int(self.var_qty.get()) + int(row[4])
            total = int(self.var_price.get()) * int(Quant)
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please Select Product From List", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE product set category=?, name=?, price=?, qty=?, totalPrice=?, status=?, location=? WHERE pid=?",
                        (
                            self.var_cat.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            Quant,
                            total,
                            self.var_status.get(),
                            self.var_loc.get(),
                            self.var_pid.get(),
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select Product From List", parent=self.root)
            else:
                cur.execute("SELECT * FROM Product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op is True:
                        cur.execute("DELETE FROM product WHERE pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self, e):
        self.var_cat.set("Select")
        self.var_loc.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")

        self.show()

    def search(self):
        try:
            con = sqlite3.connect(database=r'std.db')
            cur = con.cursor()
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            else:
                cur.execute(
                    "SELECT * FROM product WHERE " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
