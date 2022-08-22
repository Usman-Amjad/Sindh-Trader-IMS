# -------Importing Modules
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import ImageTk

switch_value = True


class locationClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+200+130")
        self.root.title("ASB")
        self.root.config(bg="#333333")
        self.root.focus_force()

        # ===== Variables =====
        self.var_loc_id = StringVar()
        self.var_name = StringVar()
        self.address = StringVar()

        # ===== Style =====
        style = ttk.Style(self.root)

        icon = PhotoImage(file='images/logoB.png')
        self.root.iconphoto(False, icon)

        # ====== Title ======
        self.lbl_title = Label(self.root, text="Manage Location", font=("Brush Script MT", 50), bg="#333333",
                               fg="white")
        self.lbl_title.pack(side=TOP, fill=X)

        self.logo = ImageTk.PhotoImage(file="images/logoB.png")
        self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

        self.lbl_name = Label(self.root, text="Name \t             Address", font=("goudy old style", 25),
                              bg="#333333", fg='white')
        self.lbl_name.place(x=50, y=105)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg="#F2F2F2")
        self.txt_name.place(x=50, y=160, width=200)
        self.txt_name.focus()

        self.txtAddress = Entry(self.root, textvariable=self.address, font=("goudy old style", 18), bg="#F2F2F2")
        self.txtAddress.place(x=290, y=160, width=300)

        btn_add = Button(self.root, text="ADD", font=("goudy old style", 15), bg="#0078D7",
                         fg="white", cursor="hand2")
        btn_add.place(x=280, y=210, width=150, height=35)
        btn_add.bind("<Return>", self.add)
        btn_add.bind("<ButtonRelease-1>", self.add)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15), bg="#0078D7",
                            fg="white", cursor="hand2")
        btn_delete.place(x=440, y=210, width=150, height=35)
        btn_delete.bind("<Return>", self.delete)
        btn_delete.bind("<ButtonRelease-1>", self.delete)

        # ====== Location Details ======
        loc_frame = Frame(self.root, bd=1, relief=RIDGE)
        loc_frame.place(x=700, y=100, width=380, height=390)

        style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333", rowheight=30,
                        font=("Arial", 12))
        style.map("Treeview", background=[("selected", "#0078D7")])
        style.configure("Treeview.Heading", font=('Constantia', 12))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        scrolly = Scrollbar(loc_frame, orient=VERTICAL)
        scrollx = Scrollbar(loc_frame, orient=HORIZONTAL)

        self.locationTable = ttk.Treeview(loc_frame, style="Treeview", columns=("lid", "name", "address"),
                                          yscrollcommand=scrolly.set,
                                          xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.locationTable.xview)
        scrolly.config(command=self.locationTable.yview)

        self.locationTable.heading("lid", text="Location ID")
        self.locationTable.heading("name", text="Name")
        self.locationTable.heading("address", text="Address")

        self.locationTable["show"] = "headings"

        self.locationTable.column("lid", width=70)
        self.locationTable.column("name", width=100)
        self.locationTable.column("address", width=100)

        self.locationTable.pack(fill=BOTH, expand=1)

        self.locationTable.bind("<ButtonRelease-1>", self.get_data)
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
            self.txtAddress.config(bg="#F2F2F2", fg='black', insertbackground='black')

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
            self.txtAddress.config(bg="#3c3f41", fg='#F2F2F2', insertbackground='white')

            self.logo = ImageTk.PhotoImage(file="images/logoW.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            switch_value = False

    def add(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Location Name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM locations WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Location already present, try different", parent=self.root)
                else:
                    cur.execute("INSERT INTO locations(name, address) values(?,?)",
                                (self.var_name.get(), self.address.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Location Added Successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM locations")
            rows = cur.fetchall()
            self.locationTable.delete(*self.locationTable.get_children())
            for row in rows:
                self.locationTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_loc_id.set("")
        self.var_name.set("")
        self.address.set("")

    def get_data(self, ev):
        f = self.locationTable.focus()
        content = (self.locationTable.item(f))
        row = content['values']
        self.var_loc_id.set(row[0])
        self.var_name.set(row[1])
        self.address.set(row[2])

    def delete(self, e):
        con = sqlite3.connect(database=r'std.db')
        cur = con.cursor()
        try:
            if self.var_loc_id.get() == "":
                messagebox.showerror("Error", "Please Select Location From The List", parent=self.root)
            else:
                cur.execute("SELECT * FROM locations WHERE lid=?", (self.var_loc_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Error, Please try Again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op is True:
                        cur.execute("DELETE FROM locations WHERE lid=?", (self.var_loc_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Location Deleted Successfully", parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = locationClass(root)
    root.mainloop()
