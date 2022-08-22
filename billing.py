# -------Importing Modules
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os
import tempfile
import time
from datetime import datetime
from PIL import ImageTk

switch_value = True


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1370x720+80+50")
        self.root.title("Sindh Traders")
        self.root.config(bg="#F2F2F2")
        self.root.resizable(False, False)

        # ===== Style =====
        self.style = ttk.Style(self.root)

        icon = PhotoImage(file='images/logoB.png')
        self.root.iconphoto(False, icon)

        # ===== Variables =====
        self.cat_list = []  # List Variable
        self.fetch_cat_loc()  # Calling Function

        self.cart_list = []
        self.chk_print = 0

        # ====== Title =======
        self.title = Label(self.root, text="Billing Menu", font=("Brush Script MT", 50, "bold")
                           , bg="#333333", fg="white", anchor="n")
        self.title.pack(side=TOP, fill=X)

        # ===== Logo Image =====
        self.logo = ImageTk.PhotoImage(file="images/logoB.png")
        self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

        # ====== Clock ======
        self.lbl_clock = Label(self.root, text="Welcome to Stock Management System\t\t Date:DD-MM-YYYY\t\t Time: "
                                               "HH:MM:SS", font=("times new roman", 15), bg="#333333", fg="#F2F2F2")
        self.lbl_clock.place(x=0, y=90, relwidth=1, height=30)

        # ====== Product Frame ======
        # ===== Variable =====
        self.var_search = StringVar()
        self.search_cat = StringVar()

        self.ProductFrame1 = Frame(self.root, bg="#333333", bd=4, relief=RIDGE)
        self.ProductFrame1.place(x=6, y=125, width=410, height=550)

        self.pTitle = Label(self.ProductFrame1, text="All Products", font=("Brush Script MT", 20, "bold"), bg="#333333",
                            fg="white")
        self.pTitle.pack(side=TOP, fill=X)

        # ===== Product Search Frame =====
        self.ProductFrame2 = Frame(self.ProductFrame1, bg="#333333")
        self.ProductFrame2.place(x=2, y=42, width=398, height=90)

        self.lbl_search = Label(self.ProductFrame2, text="Search Product | By Category", font=("Agency FB", 17, "bold"),
                                bg="#333333", fg="white")
        self.lbl_search.place(x=2, y=5)

        searchLoc = ttk.Combobox(self.ProductFrame2, font=("times new roman", 13), textvariable=self.search_cat,
                                 values=self.cat_list, state="readonly", justify=CENTER)
        searchLoc.place(x=2, y=45, width=120, height=30)
        searchLoc.current(0)

        self.txt_search = Entry(self.ProductFrame2, textvariable=self.var_search, font=("times new roman", 15),
                                bg="#3c3f41", fg='#F2F2F2', insertbackground='white')
        self.txt_search.place(x=128, y=45, width=150, height=30)

        self.searchIcon = ImageTk.PhotoImage(file='images/search.png')
        self.btn_search = Button(self.ProductFrame2, image=self.searchIcon, command=self.search,
                                 bg="#333333", activebackground='#333333', cursor="hand2", borderwidth=0)
        self.btn_search.place(x=310, y=30)

        btn_show_all = Button(self.ProductFrame2, text="Show All", command=self.show, font=("Agency FB", 15, 'bold'),
                              bg="#0078D7", fg="white", cursor="hand2").place(x=285, y=0, width=90, height=30)

        # ===== Product Detail Frame =====
        self.ProductFrame3 = Frame(self.ProductFrame1)
        self.ProductFrame3.place(x=2, y=140, width=398, height=375)

        self.style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333",
                             rowheight=30,
                             font=("Arial", 12))
        self.style.map("Treeview", background=[("selected", "#0078D7")])  # added blue color when a row is selected
        self.style.configure("Treeview.Heading", font=('Constantia', 12))
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        scrolly = Scrollbar(self.ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(self.ProductFrame3, orient=HORIZONTAL)

        self.Product_Table = ttk.Treeview(self.ProductFrame3, style='Treeview', columns=(
            "pid", "category", "name", "price", "qty", "location"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        for column in self.Product_Table["columns"]:
            self.Product_Table.column(column, anchor=CENTER)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Product_Table.xview)
        scrolly.config(command=self.Product_Table.yview)

        self.Product_Table.heading("pid", text="PID")
        self.Product_Table.heading("category", text="Category")
        self.Product_Table.heading("name", text="Name")
        self.Product_Table.heading("price", text="Price")
        self.Product_Table.heading("qty", text="Quantity")
        self.Product_Table.heading("location", text="Location")

        self.Product_Table["show"] = "headings"

        self.Product_Table.column("pid", width=40)
        self.Product_Table.column("category", width=100)
        self.Product_Table.column("name", width=100)
        self.Product_Table.column("price", width=40)
        self.Product_Table.column("qty", width=90)
        self.Product_Table.column("location", width=90)

        self.Product_Table.pack(fill=BOTH, expand=1)
        self.Product_Table.bind("<ButtonRelease-1>", self.get_data)

        self.lbl_note = Label(self.ProductFrame1, text="Note: Enter 0 Quantity to remove the product from cart",
                              font=("goudy old style", 13, 'bold'), anchor="w", bg="#333333", fg="white")
        self.lbl_note.pack(side=BOTTOM, fill=X)

        # ===== Customer Details Frame =====
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        self.paymentType = StringVar()

        self.CustomerFrame = Frame(self.root, bg="#333333", bd=2, relief=RIDGE)
        self.CustomerFrame.place(x=420, y=125, width=530, height=70)

        self.lblPaymentType = Label(self.CustomerFrame, text="Payment Type", font=("Agency FB", 17), bg="#333333",
                                    fg='white')
        self.lblPaymentType.place(x=100, y=0)

        searchLoc = ttk.Combobox(self.CustomerFrame, font=("times new roman", 13), textvariable=self.paymentType,
                                 values=["Select", "Credit", "Debit"], state="readonly", justify=CENTER)
        searchLoc.place(x=220, y=5, width=140)
        searchLoc.current(0)

        self.lbl_name = Label(self.CustomerFrame, text="Name", font=("Agency FB", 17), bg="#333333", fg='white')
        self.lbl_name.place(x=5, y=30)
        txt_name = Entry(self.CustomerFrame, textvariable=self.var_cname, font=("times new roman", 13),
                         bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=65, y=35, width=180)

        self.lbl_contact = Label(self.CustomerFrame, text="Contact No.", font=("Agency FB", 17), bg="#333333",
                                 fg='white')
        self.lbl_contact.place(x=250, y=30)
        txt_contact = Entry(self.CustomerFrame, textvariable=self.var_contact, font=("times new roman", 13),
                            bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=350, y=35, width=160)

        # ===== Cal Cart Frame =====
        self.Cal_Cart_Frame = Frame(self.root, bg="#333333", bd=2, relief=RIDGE)
        self.Cal_Cart_Frame.place(x=420, y=200, width=530, height=360)

        # ===== Calculator Frame =====
        self.var_cal_input = StringVar()

        self.Cal_Frame = Frame(self.Cal_Cart_Frame, bg="white", bd=9, relief=RIDGE)
        self.Cal_Frame.place(x=5, y=10, width=268, height=340)

        txt_cal_input = Entry(self.Cal_Frame, textvariable=self.var_cal_input, bg='#333333', fg='#333333',
                              font=("arial", 15, "bold"), width=21, bd=8,
                              relief=GROOVE, state='readonly', justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)
        txt_cal_input.focus()

        btn_7 = Button(self.Cal_Frame, text="7", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(7), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_7.grid(row=1, column=0)
        txt_cal_input.bind('7', lambda event: self.get_input(7))
        btn_8 = Button(self.Cal_Frame, text="8", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(8), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_8.grid(row=1, column=1)
        txt_cal_input.bind('8', lambda event: self.get_input(8))
        btn_9 = Button(self.Cal_Frame, text="9", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(9), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_9.grid(row=1, column=2)
        txt_cal_input.bind('9', lambda event: self.get_input(9))
        btn_sum = Button(self.Cal_Frame, text='+', font=("arial", 15, "bold"), bg='#333333', fg='white',
                         command=lambda: self.get_input('+'), bd=5,
                         width=4, pady=10, cursor="hand2")
        btn_sum.grid(row=1, column=3)
        txt_cal_input.bind('+', lambda event: self.get_input('+'))

        btn_4 = Button(self.Cal_Frame, text="4", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(4), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_4.grid(row=2, column=0)
        txt_cal_input.bind('4', lambda event: self.get_input(4))
        btn_5 = Button(self.Cal_Frame, text="5", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(5), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_5.grid(row=2, column=1)
        txt_cal_input.bind('5', lambda event: self.get_input(5))
        btn_6 = Button(self.Cal_Frame, text="6", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(6), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_6.grid(row=2, column=2)
        txt_cal_input.bind('6', lambda event: self.get_input(6))
        btn_sub = Button(self.Cal_Frame, text='-', font=("arial", 15, "bold"), bg='#333333', fg='white',
                         command=lambda: self.get_input('-'), bd=5,
                         width=4, pady=10, cursor="hand2")
        btn_sub.grid(row=2, column=3)
        txt_cal_input.bind('-', lambda event: self.get_input('-'))

        btn_1 = Button(self.Cal_Frame, text="1", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(1), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_1.grid(row=3, column=0)
        txt_cal_input.bind('1', lambda event: self.get_input(1))
        btn_2 = Button(self.Cal_Frame, text="2", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(2), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_2.grid(row=3, column=1)
        txt_cal_input.bind('2', lambda event: self.get_input(2))
        btn_3 = Button(self.Cal_Frame, text="3", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(3), bd=5,
                       width=4, pady=10, cursor="hand2")
        btn_3.grid(row=3, column=2)
        txt_cal_input.bind('3', lambda event: self.get_input(3))
        btn_mul = Button(self.Cal_Frame, text='x', font=("arial", 15, "bold"), bg='#333333', fg='white',
                         command=lambda: self.get_input('*'), bd=5,
                         width=4, pady=10, cursor="hand2")
        btn_mul.grid(row=3, column=3)
        txt_cal_input.bind('*', lambda event: self.get_input('*'))

        btn_0 = Button(self.Cal_Frame, text="0", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=lambda: self.get_input(0), bd=5,
                       width=4, pady=15, cursor="hand2")
        btn_0.grid(row=4, column=0)
        txt_cal_input.bind('0', lambda event: self.get_input(0))
        btn_c = Button(self.Cal_Frame, text="c", font=("arial", 15, "bold"), bg='#333333', fg='white',
                       command=self.clear_cal, bd=5, width=4, pady=15,
                       cursor="hand2")
        btn_c.grid(row=4, column=1)
        txt_cal_input.bind('c', lambda event: self.clear_cal())
        btn_eq = Button(self.Cal_Frame, text="=", font=("arial", 15, "bold"), bg='#333333', fg='white',
                        command=self.perform_cal, bd=5, width=4,
                        pady=15, cursor="hand2")
        btn_eq.grid(row=4, column=2)
        txt_cal_input.bind('<Return>', lambda event: self.perform_cal())
        btn_div = Button(self.Cal_Frame, text='/', font=("arial", 15, "bold"), bg='#333333', fg='white',
                         command=lambda: self.get_input('/'), bd=5,
                         width=4, pady=15, cursor="hand2")
        btn_div.grid(row=4, column=3)
        txt_cal_input.bind('/', lambda event: self.get_input('/'))

        # ===== Cart Frame =====
        self.cart_Frame = Frame(self.Cal_Cart_Frame)
        self.cart_Frame.place(x=280, y=8, width=245, height=342)

        self.cartTitle = Label(self.cart_Frame, text="Cart \t Total Products: [0]",
                               font=("goudy old style", 15, 'bold'),
                               bg='#333333', fg='white')
        self.cartTitle.pack(side=TOP, fill=X)

        self.style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333",
                             rowheight=30,
                             font=("Arial", 12))
        self.style.map("Treeview", background=[("selected", "#0078D7")])  # added blue color when a row is selected
        self.style.configure("Treeview.Heading", font=('Constantia', 12))
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        scrolly = Scrollbar(self.cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.cart_Frame, orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(self.cart_Frame, style='Treeview', columns=("pid", "name", "price", "qty"),
                                      yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        for column in self.CartTable["columns"]:
            self.CartTable.column(column, anchor=CENTER)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid", text="PID")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="Qty")

        self.CartTable["show"] = "headings"

        self.CartTable.column("pid", width=40)
        self.CartTable.column("name", width=90)
        self.CartTable.column("price", width=90)
        self.CartTable.column("qty", width=40)

        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease-1>", self.get_data_cart)

        # ===== Add Cart Widgets Frame =====
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        self.Add_CartWidgetsFrame = Frame(self.root, bg="#333333", bd=2, relief=RIDGE)
        self.Add_CartWidgetsFrame.place(x=420, y=565, width=530, height=110)

        self.lbl_p_name = Label(self.Add_CartWidgetsFrame, text="Product Name", font=("times new roman", 15, 'bold'),
                                bg='#333333',
                                fg='white')
        self.lbl_p_name.place(x=5, y=5)

        txt_p_name = Entry(self.Add_CartWidgetsFrame, textvariable=self.var_pname, font=("times new roman", 15),
                           bg="#3c3f41", fg='#F2F2F2', insertbackground='white', state='readonly').place(x=5, y=35,
                                                                                                         width=190,
                                                                                                         height=22)

        self.lbl_p_price = Label(self.Add_CartWidgetsFrame, text="Price Per Qty", font=("times new roman", 15, 'bold'),
                                 bg='#333333',
                                 fg='white')
        self.lbl_p_price.place(x=230, y=5)

        txt_p_price = Entry(self.Add_CartWidgetsFrame, textvariable=self.var_price, font=("times new roman", 15),
                            bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=230, y=35, width=150,
                                                                                        height=22)

        self.lbl_p_qty = Label(self.Add_CartWidgetsFrame, text="Quantity", font=("times new roman", 15, 'bold'),
                               bg='#333333',
                               fg='white')
        self.lbl_p_qty.place(x=390, y=5)

        txt_p_qty = Entry(self.Add_CartWidgetsFrame, textvariable=self.var_qty, font=("times new roman", 15),
                          bg="#3c3f41", fg='#F2F2F2', insertbackground='white').place(x=390, y=35, width=120, height=22)

        self.lbl_instock = Label(self.Add_CartWidgetsFrame, text="In Stock", font=("times new roman", 15, 'bold'),
                                 bg='#333333',
                                 fg='#F2F2F2')
        self.lbl_instock.place(x=5, y=70)

        btn_clear_cart = Button(self.Add_CartWidgetsFrame, text="Clear",
                                font=("times new roman", 15, "bold"), bg="light gray", cursor="hand2")
        btn_clear_cart.place(x=180, y=70, width=150, height=30)

        btn_add_cart = Button(self.Add_CartWidgetsFrame, text="Add | Update Cart",
                              font=("times new roman", 15, "bold"), bg="orange", cursor="hand2")
        btn_add_cart.place(x=340, y=70, width=180, height=30)
        btn_add_cart.bind("<Return>", self.add_update_cart)
        btn_add_cart.bind("<ButtonRelease-1>", self.add_update_cart)

        # ===== Billing Area =====
        self.billFrame = Frame(self.root, bg="#333333", bd=2, relief=RIDGE)
        self.billFrame.place(x=953, y=125, width=410, height=405)

        self.BTitle = Label(self.billFrame, text="Customer Bill Area", font=("goudy old style", 20, "bold"),
                            bg="#333333",
                            fg="white")
        self.BTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(self.billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(self.billFrame, yscrollcommand=scrolly.set, font=("goudy old style", 13),
                                  bg="#333333",
                                  fg="white", insertbackground="white")
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # ===== Billing Buttons =====
        self.txt_disc = IntVar()

        self.billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg="#333333")
        self.billMenuFrame.place(x=953, y=535, width=410, height=140)

        self.lbl_amnt = Label(self.billMenuFrame, text="Bill Amount\n[0]", font=("goudy old style", 15, "bold"),
                              bg="#3f51b5", fg="white")
        self.lbl_amnt.place(x=2, y=5, width=120, height=70)

        self.lbl_discount = Label(self.billMenuFrame, text="Discount\n", font=("goudy old style", 15, "bold"),
                                  bg="#8bc34a",
                                  fg="white")
        self.lbl_discount.place(x=124, y=5, width=120, height=70)

        txt_discount = Entry(self.billMenuFrame, textvariable=self.txt_disc,
                             font=("goudy old style", 15, "bold")).place(
            x=146, y=42, width=75, height=30)

        self.lbl_net_pay = Label(self.billMenuFrame, text="Net Pay\n[0]", font=("goudy old style", 15, "bold"),
                                 bg="#607d8b",
                                 fg="white")
        self.lbl_net_pay.place(x=246, y=5, width=158, height=70)

        self.printIcon = ImageTk.PhotoImage(file='images/print.png')
        self.btnPrint = Button(self.billMenuFrame, text="Print", image=self.printIcon, compound=RIGHT,
                               font=("times new roman", 12, 'bold'), bg='#333333', fg='#F2F2F2', borderwidth=0,
                               command=self.print_bill, activebackground='#333333', cursor="hand2")
        self.btnPrint.place(x=10, y=80)

        self.clearIcon = ImageTk.PhotoImage(file='images/clear.png')
        self.btn_clear_all = Button(self.billMenuFrame, text="Clear All", compound=RIGHT,
                                    font=("times new roman", 12, 'bold'), fg='#F2F2F2', image=self.clearIcon,
                                    command=self.clear_all, cursor="hand2",
                                    bg="#333333", activebackground='#333333', borderwidth=0)
        self.btn_clear_all.place(x=130, y=80, width=120, height=50)

        self.billIcon = ImageTk.PhotoImage(file='images/bill.png')
        self.btn_generate = Button(self.billMenuFrame, text="Save Bill", compound=RIGHT,
                                   font=("times new roman", 12, 'bold'), fg='#F2F2F2', image=self.billIcon,
                                   command=self.generate_bill, borderwidth=0,
                                   cursor="hand2", activebackground='#333333', bg="#333333")
        self.btn_generate.place(x=280, y=80)

        # ===== Footer =====
        self.footer = Label(self.root,
                            text="Sindh Distribution - Stock Management System | Developed By UA\nFor any Technical Issue contact: "
                                 "+923448112288",
                            font=("times new roman", 12), bg="#333333", fg="#F2F2F2")
        self.footer.pack(side=BOTTOM, fill=X)

        self.show()
        self.update_date_time()

        # ====== Dark or Light Mode ======
        self.light = ImageTk.PhotoImage(file="images/light-mode1.png")
        self.dark = ImageTk.PhotoImage(file="images/dark-mode.png")

        self.themeBtn = Button(self.root, image=self.dark, bg='#333333', activebackground='#333333', bd=0,
                               cursor="hand2")
        self.themeBtn.place(x=1280, y=30, width=80, height=30)
        self.themeBtn.bind("<ButtonRelease-1>", self.toggle)

    # ==================== All Functions ==========================================

    def fetch_cat_loc(self):
        try:
            self.cat_list.append("Empty")
            con = sqlite3.connect(database=r'std.db')
            cur = con.cursor()

            cur.execute("SELECT name FROM category")
            loc = cur.fetchall()
            if len(loc) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in loc:
                    self.cat_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_input(self, num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        conn = sqlite3.connect(database=r'std.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT pid, category, name, price, qty, location FROM product WHERE status='Active'")
            rows = cursor.fetchall()
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
                self.Product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def search(self):
        conn = sqlite3.connect(database=r'std.db')
        cursor = conn.cursor()

        if self.search_cat.get() in self.cat_list:
            cursor.execute(
                "SELECT pid, category, name, price, qty FROM product WHERE name LIKE '%" + self.var_search.get() + "%' AND status='Active'")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.Product_Table.delete(*self.Product_Table.get_children())
                for row in rows:
                    self.Product_Table.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found!!!", parent=self.root)
        else:
            messagebox.showerror("Error", "Select Valid Category", parent=self.root)

    def get_data(self, ev):
        f = self.Product_Table.focus()
        content = (self.Product_Table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[2])
        self.var_price.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        self.var_qty.set('1')
        self.search_cat.set(row[1])

    def get_data_cart(self, ev):
        f = self.CartTable.focus()
        content = (self.CartTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]", bg='#333333', fg='white')
        self.var_stock.set(row[4])

    def add_update_cart(self, e):
        if self.var_pid.get() == '':
            messagebox.showerror("Error", "Please select product from the list", parent=self.root)
        elif self.var_qty.get() == '':
            messagebox.showerror("Error", "Quantity is Required", parent=self.root)
        elif float(self.var_qty.get()) > float(self.var_stock.get()):
            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)
        else:
            conn = sqlite3.connect(database=r'std.db')
            cursor = conn.cursor()

            billAmt = float(self.var_price.get()) * float(self.var_qty.get())
            price_cal = self.var_price.get()
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get(), self.var_stock.get(),
                         billAmt, self.search_cat.get()]

            # ===== Update Cart =====
            present = 'no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno('Confirm',
                                         "Product already present\nDo you want to Update | Remove from the Cart List",
                                         parent=self.root)
                if op == True:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][3] = self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amnt = 0
        for row in self.cart_list:
            self.bill_amnt = self.bill_amnt + (float(row[2]) * float(row[3]))

        self.lbl_amnt.config(text=f'Bill Amnt\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.bill_amnt)}')
        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def generate_bill(self):
        self.addDate = datetime.now().strftime("%m/%d/%Y")
        self.addTime = time.strftime("%I:%M:%S")
        conn = sqlite3.connect(database=r'std.db')
        cursor = conn.cursor()

        op = messagebox.askyesno("Confirm", "Do you really want to Generate Bill?", parent=self.root)
        if len(self.cart_list) == 0:
            messagebox.showerror("Error", "Please Add Product to the Cart!!!", parent=self.root)
        elif op == True:
            # ===== Bill Top =====
            self.bill_top()
            # ===== Bill Middle =====
            self.bill_middle()
            # ===== Bill Bottom =====
            self.bill_bottom()

            for row in self.cart_list:
                name = row[1]
                bill_amt = row[2]
                totalPrice = row[5]
                cursor.execute(
                    "INSERT INTO orders(orderId, orderItemName, perItemPrice, orderQty, orderTotalPrice, orderDiscount, orderNetPrice, orderPayType, orderCustomerName, orderCustomerPhone, orderDate, orderTime) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        self.invoice,
                        name,
                        self.var_price.get(),
                        self.var_qty.get(),
                        totalPrice,
                        self.discount,
                        self.net_pay,
                        self.paymentType.get(),
                        self.var_cname.get(),
                        self.var_contact.get(),
                        self.addDate,
                        self.addTime,
                    ))
                conn.commit()

            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo('Saved', "Bill has been generated/Save in Backend", parent=self.root)

        self.chk_print = 1

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t   ST, Main Bazaar, Sanghar
\t     Phone No. +923043786863
{str("=" * 42)}
 Customer Name: {self.var_cname.get()}
 Ph No: {self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%m/%d/%Y"))}
{str("=" * 42)}
 Product Name\t\t\tQty\tPrice
{str("=" * 42)} 
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        self.discount = float(self.txt_disc.get())
        self.net_pay = float(self.bill_amnt) - float(self.discount)
        bill_bottom_temp = f'''
{str("=" * 42)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("=" * 42)}
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        try:
            conn = sqlite3.connect(database=r'std.db')
            cursor = conn.cursor()

            self.time_1 = datetime.now().strftime("%m/%d/%Y")
            self.total_price = float(self.var_price.get()) * float(self.var_qty.get())
            if self.search_cat.get() in self.cat_list:
                for row in self.cart_list:
                    self.pid = row[0]
                    self.name = row[1]
                    qty = float(row[4]) - float(row[3])
                    if float(row[3]) == float(row[4]):
                        status = 'Inactive'
                    if float(row[3]) != float(row[4]):
                        status = 'Active'
                    price = float(row[2]) * float(row[3])
                    price = str(price)
                    self.txt_bill_area.insert(END, "\n " + self.name + "\t\t\t" + row[3] + "\tRs." + price)

                    cursor.execute("SELECT price FROM product WHERE pid=?", (
                        self.pid,
                    ))
                    row = cursor.fetchone()
                    totalPrice = float(qty) * float(row[0])

                    # ===== Update Qty In Product Table =====
                    cursor.execute("UPDATE product SET qty=?, totalPrice=?, status=? WHERE pid=?", (
                        qty,
                        totalPrice,
                        status,
                        self.pid
                    ))
                    conn.commit()
                conn.close()
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In Stock")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0', END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print = 0

    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(
            text=f"Welcome to Stock Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200, self.update_date_time)

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo('Print', "Please wait while printing", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showinfo('Print', "Please generate bill, to print the receipt", parent=self.root)

    def toggle(self, e):
        global switch_value
        if switch_value is False:
            self.themeBtn.config(image=self.dark)

            # Changes the window to dark theme
            # Top
            self.logo = ImageTk.PhotoImage(file="images/logoB.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            self.title.config(bg='#333333', fg='#F2F2F2')
            self.root.config(bg="#F2F2F2")
            self.themeBtn.config(bg='#333333', activebackground='#333333')
            self.lbl_clock.config(bg='#333333', fg='#F2F2F2')
            self.btn_search.config(bg='#333333', activebackground='#333333')

            # Left Side
            self.ProductFrame1.config(bg='#333333')
            self.pTitle.config(bg='#333333', fg='#F2F2F2')
            self.ProductFrame2.config(bg='#333333')
            self.lbl_search.config(bg='#333333', fg='#F2F2F2')
            self.lbl_note.config(bg='#333333', fg='#F2F2F2')

            # Center
            self.CustomerFrame.config(bg='#333333')
            self.lblPaymentType.config(bg='#333333', fg='#F2F2F2')
            self.lbl_name.config(bg='#333333', fg='#F2F2F2')
            self.lbl_contact.config(bg='#333333', fg='#F2F2F2')
            self.Cal_Cart_Frame.config(bg='#333333')
            self.cart_Frame.config(bg='#333333')
            self.cartTitle.config(bg='#333333', fg='#F2F2F2')
            self.Add_CartWidgetsFrame.config(bg='#333333')
            self.lbl_p_name.config(bg='#333333', fg='#F2F2F2')
            self.lbl_p_price.config(bg='#333333', fg='#F2F2F2')
            self.lbl_p_qty.config(bg='#333333', fg='#F2F2F2')
            self.lbl_instock.config(bg='#333333', fg='#F2F2F2')

            # Right Side
            self.billFrame.config(bg='#333333')
            self.BTitle.config(bg='#333333', fg='#F2F2F2')
            self.billMenuFrame.config(bg='#333333')
            self.btnPrint.config(bg='#333333', fg='#F2F2F2', activebackground='#333333')
            self.btn_clear_all.config(bg='#333333', fg='#F2F2F2', activebackground='#333333')
            self.btn_generate.config(bg='#333333', fg='#F2F2F2', activebackground='#333333')

            switch_value = True
        else:
            self.themeBtn.config(image=self.light)

            # Changes the window to light theme
            # Top
            self.logo = ImageTk.PhotoImage(file="images/logoW.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            self.title.config(bg='#F2F2F2', fg='#333333')
            self.root.config(bg="#333333")
            self.themeBtn.config(bg='#F2F2F2', activebackground='#F2F2F2')
            self.lbl_clock.config(bg='#F2F2F2', fg='#333333')
            self.btn_search.config(bg='#F2F2F2', activebackground='#F2F2F2')

            # Left Side
            self.ProductFrame1.config(bg='#F2F2F2')
            self.pTitle.config(bg='#F2F2F2', fg='#333333')
            self.ProductFrame2.config(bg='#F2F2F2')
            self.lbl_search.config(bg='#F2F2F2', fg='#333333')
            self.lbl_note.config(bg='#F2F2F2', fg='#333333')

            # Center
            self.CustomerFrame.config(bg='#F2F2F2')
            self.lblPaymentType.config(bg='#F2F2F2', fg='#333333')
            self.lbl_name.config(bg='#F2F2F2', fg='#333333')
            self.lbl_contact.config(bg='#F2F2F2', fg='#333333')
            self.Cal_Cart_Frame.config(bg='#F2F2F2')
            self.cart_Frame.config(bg='#F2F2F2')
            self.cartTitle.config(bg='#F2F2F2', fg='#333333')
            self.Add_CartWidgetsFrame.config(bg='#F2F2F2')
            self.lbl_p_name.config(bg='#F2F2F2', fg='#333333')
            self.lbl_p_price.config(bg='#F2F2F2', fg='#333333')
            self.lbl_p_qty.config(bg='#F2F2F2', fg='#333333')
            self.lbl_instock.config(bg='#F2F2F2', fg='#333333')

            # Right Side
            self.billFrame.config(bg='#F2F2F2')
            self.BTitle.config(bg='#F2F2F2', fg='#333333')
            self.billMenuFrame.config(bg='#F2F2F2')
            self.btnPrint.config(bg='#F2F2F2', fg='#333333', activebackground='#F2F2F2')
            self.btn_clear_all.config(bg='#F2F2F2', fg='#333333', activebackground='#F2F2F2')
            self.btn_generate.config(bg='#F2F2F2', fg='#333333', activebackground='#F2F2F2')

            switch_value = False


if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
