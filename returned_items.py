# -------Importing Modules
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk

# ===== Global Variable =====
switch_value = True


class returnedItems:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+220+145")
        self.root.title("UA")
        self.root.config(bg="#333333")
        self.root.focus_force()

        # ===== Style =====
        self.style = ttk.Style(self.root)

        icon = PhotoImage(file='images/logoB.png')
        self.root.iconphoto(False, icon)

        # ================== Variables ======================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_loc = StringVar()

        self.orderId = StringVar()
        self.var_name = StringVar()
        self.payType = StringVar()
        self.customerName = StringVar()
        self.customerPhone = StringVar()
        self.returnDate = StringVar()
        self.returnTime = StringVar()

        self.var_price = IntVar()
        self.var_qty = IntVar()
        self.totalPrice = IntVar()
        self.Discount = IntVar()
        self.NetPrice = IntVar()

        # ====== Title =======
        self.title = Label(self.root, text="Return Products", font=("Brush Script MT", 50, "bold")
                           , bg="#333333", fg="white", anchor="n")
        self.title.pack(side=TOP, fill=X)

        # ===== Logo Image =====
        self.logo = ImageTk.PhotoImage(file="images/logoB.png")
        self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

        # ==============================================================
        self.product_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#333333")
        self.product_Frame.place(x=10, y=100, width=450, height=482)

        fs = ('Agency FB', 20)
        self.bg = "#333333"
        self.fg = "#F2F2F2"

        # ====== Column 1 ======
        self.lblOrderID = Label(self.product_Frame, text="Order Id", font=(fs), bg=self.bg, fg=self.fg)
        self.lblOrderID.place(x=30, y=60)

        self.lblProductName = Label(self.product_Frame, text="Name", font=(fs), bg=self.bg, fg=self.fg)
        self.lblProductName.place(x=30, y=110)

        self.lblPrice = Label(self.product_Frame, text="Price", font=(fs), bg=self.bg, fg=self.fg)
        self.lblPrice.place(x=30, y=160)

        self.lblQty = Label(self.product_Frame, text="Quantity", font=(fs), bg=self.bg, fg=self.fg)
        self.lblQty.place(x=30, y=210)

        self.lblTotalPrice = Label(self.product_Frame, text="Total Price", font=(fs), bg=self.bg, fg=self.fg)
        self.lblTotalPrice.place(x=30, y=260)

        self.lblNetPrice = Label(self.product_Frame, text="Net Price", font=(fs), bg=self.bg, fg=self.fg)
        self.lblNetPrice.place(x=30, y=310)
        # lblPayType = Label(product_Frame, text="Pay Type", font=(fs, 18), bg="#333333", fg='white') \
        #     .place(x=30, y=410)
        # lblCustomerName = Label(product_Frame, text="Customer Name", font=(fs, 18), bg="#333333", fg='white') \
        #     .place(x=30, y=460)
        # lblCustomerPhone = Label(product_Frame, text="Customer Phone", font=(fs, 18), bg="#333333", fg='white') \
        #     .place(x=30, y=510)
        # lblReturnDate = Label(product_Frame, text="Return Date", font=(fs, 18), bg="#333333", fg='white') \
        #     .place(x=30, y=560)
        # lblReturnTime = Label(product_Frame, text="Return Time", font=(fs, 18), bg="#333333", fg='white') \
        #     .place(x=30, y=610)

        # ====== Column 2 ======
        txtOrderID = Entry(self.product_Frame, textvariable=self.orderId,
                           font=("goudy old style", 16),
                           bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        txtOrderID.place(x=200, y=65, width=200)
        txtOrderID.selection_clear()

        txtName = Entry(self.product_Frame, textvariable=self.var_name,
                        font=("goudy old style", 16),
                        bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        txtName.place(x=200, y=115, width=200)
        txtName.selection_clear()

        txtPrice = Entry(self.product_Frame, textvariable=self.var_price,
                         font=("goudy old style", 16),
                         bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        txtPrice.place(x=200, y=165, width=200)
        txtPrice.selection_clear()

        txtQty = Entry(self.product_Frame, textvariable=self.var_qty,
                       font=("goudy old style", 16),
                       bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        txtQty.place(x=200, y=215, width=200)
        txtQty.selection_clear()

        txtTotalPrice = Entry(self.product_Frame, textvariable=self.totalPrice,
                              font=("goudy old style", 16),
                              bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        txtTotalPrice.place(x=200, y=265, width=200)
        txtTotalPrice.selection_clear()

        txtNetPrice = Entry(self.product_Frame, textvariable=self.NetPrice,
                            font=("goudy old style", 16),
                            bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        txtNetPrice.place(x=200, y=310, width=200)
        txtNetPrice.selection_clear()
        # txtPayType = Entry(product_Frame, textvariable=self.payType,
        #                    font=("goudy old style", 15), bg="light yellow").place(x=200, y=415, width=200)
        # txtCustomerName = Entry(product_Frame, textvariable=self.customerName,
        #                         font=("goudy old style", 15), bg="light yellow").place(x=200, y=465, width=200)
        # txtCustomerPhone = Entry(product_Frame, textvariable=self.customerPhone,
        #                          font=("goudy old style", 15), bg="light yellow").place(x=200, y=515, width=200)
        # txtReturnDate = Entry(product_Frame, textvariable=self.returnDate,
        #                       font=("goudy old style", 15), bg="light yellow").place(x=200, y=565, width=200)
        # txtReturnTime = Entry(product_Frame, textvariable=self.returnTime,
        #                       font=("goudy old style", 15), bg="light yellow").place(x=200, y=615, width=200)

        # ====== Buttons ======
        bs = ('Agency FB', 16)

        btn_return = Button(self.product_Frame, text="Return", font=(bs),
                            bg="#0078D7",
                            fg="white",
                            cursor="hand2")
        btn_return.place(x=190, y=400, width=100, height=40)
        btn_return.bind("<Return>", self.update)
        btn_return.bind("<ButtonRelease-1>", self.update)

        btn_clear = Button(self.product_Frame, text="Clear", font=(bs), bg="#0078D7",
                           fg="white",
                           cursor="hand2")
        btn_clear.place(x=300, y=400, width=100, height=40)
        btn_clear.bind("<Return>", self.clear)
        btn_clear.bind("<ButtonRelease-1>", self.clear)

        # ====== Search Frame ======
        self.SearchFrame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 12, "bold"), bd=2,
                                      relief=RIDGE, bg="#333333", fg='white')
        self.SearchFrame.place(x=480, y=90, width=600, height=80)

        cmb_search = ttk.Combobox(self.SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Bill No", "Item Name"), state='readonly', justify=CENTER,
                                  font=("Agency FB", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(self.SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 16),
                           bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        txt_search.place(x=200, y=10, width=200)
        txt_search.focus()

        btn_search = Button(self.SearchFrame, text="Search", command=self.search, font=("Agency FB", 16), bg="#0078D7",
                            fg="white", cursor="hand2", bd=1, relief=RIDGE).place(x=410, y=9, width=150, height=30)

        # ====== Product Details ======
        p_Frame = Frame(self.root, bg='white', bd=1)
        p_Frame.place(x=480, y=180, width=600, height=400)

        self.style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333",
                             rowheight=30,
                             font=("Arial", 12))
        self.style.map("Treeview", background=[("selected", "#0078D7")])  # added blue color when a row is selected
        self.style.configure("Treeview.Heading", font=('Constantia', 12))
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        scrolly = Scrollbar(p_Frame, orient=VERTICAL)
        scrollx = Scrollbar(p_Frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_Frame, style="Treeview", columns=(
            "orderId", "orderItemName", "perItemPrice", "orderQty", "orderTotalPrice", "orderDiscount", "orderNetPrice",
            "orderPayType", "orderCustomerName", "orderCustomerPhone", "orderDate", "orderTime"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, selectmode='browse')
        for column in self.product_table["columns"]:
            self.product_table.column(column, anchor=CENTER)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("orderId", text="Id")
        self.product_table.heading("orderItemName", text="Name")
        self.product_table.heading("perItemPrice", text="Price")
        self.product_table.heading("orderQty", text="Qty")
        self.product_table.heading("orderTotalPrice", text="Total price")
        self.product_table.heading("orderDiscount", text="Discount")
        self.product_table.heading("orderNetPrice", text="Net Price")
        self.product_table.heading("orderPayType", text="Pay type")
        self.product_table.heading("orderCustomerName", text="Customer Name")
        self.product_table.heading("orderCustomerPhone", text="Customer Phone")
        self.product_table.heading("orderDate", text="Order Date")
        self.product_table.heading("orderTime", text="Order Time")

        self.product_table["show"] = "headings"

        self.product_table.column("orderId", width=80, minwidth=80)
        self.product_table.column("orderItemName", width=100, minwidth=100)
        self.product_table.column("perItemPrice", width=100, minwidth=100)
        self.product_table.column("orderQty", width=100, minwidth=100)
        self.product_table.column("orderTotalPrice", width=100, minwidth=100)
        self.product_table.column("orderDiscount", width=100, minwidth=100)
        self.product_table.column("orderNetPrice", width=100, minwidth=100)
        self.product_table.column("orderPayType", width=100, minwidth=100)
        self.product_table.column("orderCustomerName", width=130, minwidth=130)
        self.product_table.column("orderCustomerPhone", width=130, minwidth=130)
        self.product_table.column("orderDate", width=100, minwidth=100)
        self.product_table.column("orderTime", width=100, minwidth=100)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

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
            self.title.config(bg="#333333", fg="white")
            self.themeBtn.config(bg="#333333", activebackground="#333333")
            self.product_Frame.config(bg="#333333", bd=2, relief=RIDGE)
            self.SearchFrame.config(bg="#333333", fg="white", bd=2, relief=RIDGE)

            self.logo = ImageTk.PhotoImage(file="images/logoB.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            self.lblOrderID.config(bg="#333333", fg="white")
            self.lblProductName.config(bg="#333333", fg="white")
            self.lblPrice.config(bg="#333333", fg="white")
            self.lblQty.config(bg="#333333", fg="white")
            self.lblTotalPrice.config(bg="#333333", fg="white")
            self.lblNetPrice.config(bg="#333333", fg="white")
            switch_value = True
        else:
            self.themeBtn.config(image=self.light)

            # Changes the window to light theme
            self.root.config(bg="#F2F2F2")
            self.title.config(bg="#F2F2F2", fg="black")
            self.themeBtn.config(bg="#F2F2F2", activebackground="#F2F2F2")
            self.product_Frame.config(bg="#F2F2F2", bd=0)
            self.SearchFrame.config(bg="#F2F2F2", fg="black", bd=0)

            self.logo = ImageTk.PhotoImage(file="images/logoW.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            self.lblOrderID.config(bg="#F2F2F2", fg="black")
            self.lblProductName.config(bg="#F2F2F2", fg="black")
            self.lblPrice.config(bg="#F2F2F2", fg="black")
            self.lblQty.config(bg="#F2F2F2", fg="black")
            self.lblTotalPrice.config(bg="#F2F2F2", fg="black")
            self.lblNetPrice.config(bg="#F2F2F2", fg="black")
            switch_value = False

    def show(self):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            cur.execute(
                "SELECT orderId, orderItemName, perItemPrice, orderQty, orderTotalPrice, orderDiscount, orderNetPrice, orderPayType, orderCustomerName, orderCustomerPhone, orderDate, orderTime FROM orders")
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
            self.orderId.set(row[0])
            self.var_name.set(row[1])
            self.var_price.set(row[2])
            self.var_qty.set(row[3])
            self.totalPrice.set(row[4])
            self.Discount.set(row[5])
            self.NetPrice.set(row[6])
            self.payType.set(row[7])
            self.customerName.set(row[8])
            self.customerPhone.set(row[9])
            self.returnDate.set(row[10])
            self.returnTime.set(row[11])
        except (Exception,):
            pass

    def update(self, e):
        try:
            con = sqlite3.connect(database=r'std.db')
            cur = con.cursor()
            orderStatus = 'returned'
            total = int(self.var_price.get()) * int(self.var_qty.get())
            cur.execute("SELECT * FROM orders WHERE orderId=?", (self.orderId.get(),))
            row = cur.fetchone()
            if self.orderId.get() == "":
                messagebox.showerror("Error", "Please Select Product From List", parent=self.root)
            else:
                cur.execute("SELECT * FROM orders WHERE orderId=?", (self.orderId.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE product SET qty = qty+?, totalPrice= totalPrice+? WHERE name=? AND status='Active'",
                        (
                            self.var_qty.get(),
                            total,
                            self.var_name.get(),
                        ))
                    con.commit()
                    cur.execute(
                        "INSERT INTO returnedOrders(orderId, orderItemName, perItemPrice, orderQty, orderTotalPrice, orderStatus, orderDiscount, orderNetPrice, orderPayType, orderCustomerName, orderCustomerPhone, orderDate, orderTime) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.orderId.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.totalPrice.get(),
                            orderStatus,
                            self.Discount.get(),
                            self.NetPrice.get(),
                            self.payType.get(),
                            self.customerName.get(),
                            self.customerPhone.get(),
                            self.returnDate.get(),
                            self.returnTime.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    cur.execute(
                        "DELETE FROM orders WHERE orderId=? AND orderItemName=?",
                        (self.orderId.get(), self.var_name.get()))
                    con.commit()
                    con.close()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self, e):
        self.orderId.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.totalPrice.set("")
        self.NetPrice.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")

        self.show()

    def search(self):
        try:
            con = sqlite3.connect(database=r'std.db')
            cur = con.cursor()
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_searchby.get() == "Bill No":
                cur.execute(
                    "SELECT orderId, orderItemName, perItemPrice, orderQty, orderTotalPrice, orderDiscount, orderNetPrice, orderPayType, orderCustomerName, orderCustomerPhone, orderDate, orderTime FROM orders WHERE orderId LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
            elif self.var_searchby.get() == "Item Name":
                cur.execute(
                    "SELECT orderId, orderItemName, perItemPrice, orderQty, orderTotalPrice, orderDiscount, orderNetPrice, orderPayType, orderCustomerName, orderCustomerPhone, orderDate, orderTime FROM orders WHERE orderItemName LIKE '%" + self.var_searchtxt.get() + "%'")
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
    obj = returnedItems(root)
    root.mainloop()

# # -------Importing Modules
# from tkinter import *
# from tkinter import ttk, messagebox
# import sqlite3
#
#
# class returnedItems:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1100x600+200+110")
#         self.root.title("UA")
#         self.root.config(bg="#333333")
#         self.root.focus_force()
#
#         # ===== Variables =====
#         self.cat_list = []  # category List fetching Variable
#
#         self.var_cat_id = StringVar()
#         self.var_name = StringVar()
#         self.search_cat = StringVar()  # Dropdown Category Variable
#         self.returnAmount = StringVar()  # Returning Amount Variable
#         self.productName = StringVar()  # Product Name Variable
#
#         self.fetch_cat_loc()  # Fetching Category List
#
#         # ===== Style =====
#         style = ttk.Style(self.root)
#         style.theme_use('clam')
#
#         # ====== Title ======
#         lbl_title = Label(self.root, text="Return Items", font=("Brush Script MT", 30), bg="#202020",
#                           fg="white").pack(side=TOP, fill=X)
#
#         # ===== Product Search Frame =====
#         ProductFrame2 = Frame(self.root, bg="#FAFAFA", bd=2, relief=RIDGE)
#         ProductFrame2.place(x=10, y=60, width=398, height=350)
#
#         selectCategory = Label(ProductFrame2, text="Select Category", font=("times new roman", 15), bg="white").place(
#             x=5, y=8)
#         searchLoc = ttk.Combobox(ProductFrame2, font=("times new roman", 13), textvariable=self.search_cat,
#                                  values=self.cat_list, state="readonly", justify=CENTER)
#         searchLoc.place(x=5, y=45, width=120)
#         searchLoc.current(0)
#         # searchLoc.bind("<<ComboboxSelected>>", self.fetch_cat_loc)
#
#         lbl_p_name = Label(ProductFrame2, text="Product Name", font=("times new roman", 15), bg="white").place(
#             x=5, y=80)
#         txt_p_name = Entry(ProductFrame2, textvariable=self.productName, font=("times new roman", 15),
#                            bg="light yellow").place(x=5, y=110, width=150, height=22)
#
#         lbl_p_price = Label(ProductFrame2, text="Return Amount", font=("times new roman", 15), bg="white").place(
#             x=5, y=140)
#         txt_p_price = Entry(ProductFrame2, textvariable=self.returnAmount, font=("times new roman", 15),
#                             bg="light yellow").place(x=5, y=170, width=150, height=22)
#
#         btnSearch = Button(ProductFrame2, text="Search", font=("goudy old style", 15), bg="#4caf50",
#                            fg="white", cursor="hand2")
#         btnSearch.place(x=5, y=220, width=100, height=30)
#         btnSearch.bind("<Return>", self.search)
#         btnSearch.bind("<ButtonRelease-1>", self.search)
#
#         btn_add = Button(ProductFrame2, text="Add", font=("goudy old style", 15), bg="#4caf50",
#                          fg="white", cursor="hand2")
#         btn_add.place(x=110, y=220, width=100, height=30)
#         btn_add.bind("<Return>", self.add)
#         btn_add.bind("<ButtonRelease-1>", self.add)
#
#         btn_delete = Button(ProductFrame2, text="Delete", font=("goudy old style", 15), bg="red",
#                             fg="white", cursor="hand2")
#         btn_delete.place(x=215, y=220, width=100, height=30)
#         btn_delete.bind("<Return>", self.delete)
#         btn_delete.bind("<ButtonRelease-1>", self.delete)
#
#         # ====== Category Details ======
#         cat_frame = Frame(self.root)
#         cat_frame.place(x=409, y=60, width=688, height=350)
#
#         scrolly = Scrollbar(cat_frame, orient=VERTICAL)
#         scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)
#
#         self.categoryTable = ttk.Treeview(cat_frame, columns=("cid", "category", "name", "price"), yscrollcommand=scrolly.set,
#                                           xscrollcommand=scrollx.set)
#         scrollx.pack(side=BOTTOM, fill=X)
#         scrolly.pack(side=RIGHT, fill=Y)
#         scrollx.config(command=self.categoryTable.xview)
#         scrolly.config(command=self.categoryTable.yview)
#
#         self.categoryTable.heading("cid", text="Category ID")
#         self.categoryTable.heading("category", text="Category")
#         self.categoryTable.heading("name", text="Name")
#         self.categoryTable.heading("price", text="Price")
#
#         self.categoryTable["show"] = "headings"
#
#         self.categoryTable.column("cid", width=70)
#         self.categoryTable.column("category", width=100)
#         self.categoryTable.column("name", width=100)
#         self.categoryTable.column("price", width=100)
#
#         self.categoryTable.pack(fill=BOTH, expand=1)
#
#         self.categoryTable.bind("<ButtonRelease-1>", self.get_data)
#         self.show()
#
#     # ========================= Functions ==============================
#
#     def fetch_cat_loc(self):
#         try:
#             self.cat_list.append("Empty")
#             con = sqlite3.connect(database=r'std.db')
#             cur = con.cursor()
#
#             cur.execute("SELECT name FROM category")
#             loc = cur.fetchall()
#             if len(loc) > 0:
#                 del self.cat_list[:]
#                 self.cat_list.append("Select")
#                 for i in loc:
#                     self.cat_list.append(i[0])
#
#         except Exception as ex:
#             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
#
#     def search(self, e):
#         conn = sqlite3.connect(database=r'std.db')
#         cursor = conn.cursor()
#
#         if self.search_cat.get() in self.cat_list:
#             cursor.execute(
#                 "SELECT pid, category, name, price FROM product WHERE category LIKE '%" + self.search_cat.get() + "%' AND status='Active'")
#             rows = cursor.fetchall()
#             if len(rows) != 0:
#                 self.categoryTable.delete(*self.categoryTable.get_children())
#                 for row in rows:
#                     self.categoryTable.insert('', END, values=row)
#             else:
#                 messagebox.showerror("Error", "No record found!!!", parent=self.root)
#         else:
#             messagebox.showerror("Error", "Select Valid Category", parent=self.root)
#
#     def add(self, e):
#         con = sqlite3.connect(database=r'std.db')
#         cur = con.cursor()
#         try:
#             if self.var_name.get() == "":
#                 messagebox.showerror("Error", "Category Name must be required", parent=self.root)
#             else:
#                 cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
#                 row = cur.fetchone()
#                 if row is not None:
#                     messagebox.showerror("Error", "Category already present, try different", parent=self.root)
#                 else:
#                     cur.execute("INSERT INTO category(name) values(?)", (self.var_name.get(),))
#                     con.commit()
#                     messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
#                     self.show()
#                     self.var_cat_id.set("")
#                     self.var_name.set("")
#         except Exception as ex:
#             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
#
#     def show(self):
#         con = sqlite3.connect(database=r'std.db')
#         cur = con.cursor()
#         try:
#             cur.execute("SELECT * FROM category")
#             rows = cur.fetchall()
#             self.categoryTable.delete(*self.categoryTable.get_children())
#             for row in rows:
#                 self.categoryTable.insert('', END, values=row)
#         except Exception as ex:
#             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
#
#     def get_data(self, ev):
#         f = self.categoryTable.focus()
#         content = (self.categoryTable.item(f))
#         row = content['values']
#         self.productName.set(row[2])
#
#     def delete(self, e):
#         con = sqlite3.connect(database=r'std.db')
#         cur = con.cursor()
#         try:
#             if self.var_cat_id.get() == "":
#                 messagebox.showerror("Error", "Please Select Category From The List", parent=self.root)
#             else:
#                 cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
#                 row = cur.fetchone()
#                 if row is None:
#                     messagebox.showerror("Error", "Error, Please try Again", parent=self.root)
#                 else:
#                     op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
#                     if op is True:
#                         cur.execute("DELETE FROM category WHERE cid=?", (self.var_cat_id.get(),))
#                         con.commit()
#                         messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
#                         self.show()
#                         self.var_cat_id.set("")
#                         self.var_name.set("")
#         except Exception as ex:
#             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
#
#
# if __name__ == "__main__":
#     root = Tk()
#     obj = returnedItems(root)
#     root.mainloop()
