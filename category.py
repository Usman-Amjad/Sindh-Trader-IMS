# -------Importing Modules
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import ImageTk

switch_value = True


class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+200+130")
        self.root.title("UA")
        self.root.config(bg="#333333")
        self.root.focus_force()

        # ===== Variables =====
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # ===== Style =====
        style = ttk.Style(self.root)

        icon = PhotoImage(file='images/logoB.png')
        self.root.iconphoto(False, icon)

        # ====== Title ======
        self.lbl_title = Label(self.root, text="Manage Product Category", font=("Brush Script MT", 50), bg="#333333",
                               fg="white")
        self.lbl_title.pack(side=TOP, fill=X)

        self.logo = ImageTk.PhotoImage(file="images/logoB.png")
        self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

        self.lbl_name = Label(self.root, text="Enter Category Name", font=("Agency FB", 30), bg="#333333", fg='white')
        self.lbl_name.place(x=50, y=100)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("Agency FB", 18), bg="#F2F2F2")
        self.txt_name.place(x=50, y=170, width=300)
        self.txt_name.focus()

        btn_add = Button(self.root, text="Add", font=("Agency FB", 16), bg="#0078D7",
                         fg="white", cursor="hand2")
        btn_add.place(x=360, y=170, width=150, height=35)
        btn_add.bind("<Return>", self.add)
        btn_add.bind("<ButtonRelease-1>", self.add)

        btn_delete = Button(self.root, text="Delete", font=("Agency FB", 16), bg="#0078D7",
                            fg="white", cursor="hand2")
        btn_delete.place(x=520, y=170, width=150, height=35)
        btn_delete.bind("<Return>", self.delete)
        btn_delete.bind("<ButtonRelease-1>", self.delete)

        # ====== Category Details ======
        cat_frame = Frame(self.root, bd=1, relief=RIDGE)
        cat_frame.place(x=700, y=100, width=380, height=390)

        style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333", rowheight=30,
                        font=("Arial", 12))
        style.map("Treeview", background=[("selected", "#0078D7")])
        style.configure("Treeview.Heading", font=('Constantia', 12))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_frame, style="Treeview", columns=("cid", "name"),
                                          yscrollcommand=scrolly.set,
                                          xscrollcommand=scrollx.set)
        for column in self.categoryTable["columns"]:
            self.categoryTable.column(column, anchor=CENTER)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid", text="Id")
        self.categoryTable.heading("name", text="Name")

        self.categoryTable["show"] = "headings"

        self.categoryTable.column("cid", width=30, minwidth=30)
        self.categoryTable.column("name", width=100, minwidth=110)

        self.categoryTable.pack(fill=BOTH, expand=1)

        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        # ====== Dark or Light Mode ======
        self.light = ImageTk.PhotoImage(file="images/light-mode1.png")
        self.dark = ImageTk.PhotoImage(file="images/dark-mode.png")

        self.themeBtn = Button(self.root, image=self.dark, bg='#333333', activebackground='#333333', bd=0,
                               cursor="hand2")
        self.themeBtn.place(x=1000, y=30, width=80, height=30)
        self.themeBtn.bind("<ButtonRelease-1>", self.toggle)

    # ========================= Functions ==============================

    def toggle(self, e):
        global switch_value
        if switch_value is False:
            self.themeBtn.config(image=self.dark)

            # Changes the window to dark theme
            self.root.config(bg="#333333")
            self.lbl_title.config(bg="#333333", fg="white")
            self.lbl_name.config(bg="#333333", fg="white")
            self.themeBtn.config(bg="#333333", activebackground="#333333")
            self.txt_name.config(bg="#F2F2F2", fg='black', insertbackground='black')

            self.logo = ImageTk.PhotoImage(file="images/logoB.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            switch_value = True
        else:
            self.themeBtn.config(image=self.light)

            # Changes the window to light theme
            self.root.config(bg="#F2F2F2")
            self.lbl_title.config(bg="#F2F2F2", fg="black")
            self.lbl_name.config(bg="#F2F2F2", fg="black")
            self.themeBtn.config(bg="#F2F2F2", activebackground="#F2F2F2")
            self.txt_name.config(bg="#3c3f41", fg='#F2F2F2', insertbackground='white')

            self.logo = ImageTk.PhotoImage(file="images/logoW.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            switch_value = False

    def add(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category Name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Category already present, try different", parent=self.root)
                else:
                    cur.execute("INSERT INTO category(name) values(?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()
                    self.var_cat_id.set("")
                    self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        try:
            f = self.categoryTable.focus()
            content = (self.categoryTable.item(f))
            row = content['values']
            self.var_cat_id.set(row[0])
            self.var_name.set(row[1])
        except:
            pass

    def delete(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please Select Category From The List", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Error, Please try Again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op is True:
                        cur.execute("DELETE FROM category WHERE cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
