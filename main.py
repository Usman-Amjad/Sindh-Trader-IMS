from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from product import productClass
from category import categoryClass
from locations import locationClass
from billing import BillClass
from returned_items import returnedItems
from summary import allSummary

switch_value = True


class stockManagement:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1425x700+50+20")
        self.root.title("Sindh Traders")

        # ===== Style =====
        style = ttk.Style(root)

        # ===== Background Image =====
        self.bgFrame = Frame(bg='blue')
        self.bgFrame.place(y=123, height=670, relwidth=1)
        self.bg = Image.open("images/bg.jpg")
        self.bg = self.bg.resize((1920, 700), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bgImage = Label(self.bgFrame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===== Icon image =====
        icon = PhotoImage(file='images/logoB.png')
        self.root.iconphoto(False, icon)

        # ====== Title =======
        self.title = Label(self.root, text="Sindh Traders", font=("Brush Script MT", 50, "bold")
                           , bg="#333333", fg="#F2F2F2", anchor="n")
        self.title.pack(side=TOP, fill=X)

        self.divider = Frame(bg='#F2F2F2')
        self.divider.pack(side=TOP, fill=X, ipady=1)

        # ===== Logo Image =====
        self.logo = ImageTk.PhotoImage(file="images/logoB.png")
        self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

        # ===== Menu Bar =====
        backgroundColor = '#333333'
        foregroundColor = '#F2F2F2'
        self.lbl_menu = Frame(bg=backgroundColor)
        self.lbl_menu.pack(side=TOP, fill=X, ipady=15)

        self.btn_category = Button(self.lbl_menu, text="CATEGORY", command=self.category,
                                   font=("times new roman", 12, "bold"),
                                   bg=backgroundColor, fg=foregroundColor, bd=0, cursor="hand2")
        self.btn_category.place(x=2, y=0, width=90, height=30)

        self.btn_location = Button(self.lbl_menu, text="LOCATIONS", command=self.location,
                                   font=("times new roman", 12, "bold"),
                                   bg=backgroundColor, fg=foregroundColor, bd=0, cursor="hand2")
        self.btn_location.place(x=110, y=0, width=95, height=30)

        self.btn_product = Button(self.lbl_menu, text="PRODUCT", command=self.product,
                                  font=("times new roman", 12, "bold"),
                                  bg=backgroundColor, fg=foregroundColor, bd=0, cursor="hand2")
        self.btn_product.place(x=220, y=0, width=80, height=30)

        self.btn_billing = Button(self.lbl_menu, text="BILLING", command=self.billing,
                                  font=("times new roman", 12, "bold"),
                                  bg=backgroundColor, fg=foregroundColor, bd=0, cursor="hand2")
        self.btn_billing.place(x=310, y=0, width=80, height=30)

        self.btnReturnedItems = Button(self.lbl_menu, text="RETURN", command=self.returnedItem,
                                       font=("times new roman", 12, "bold"),
                                       bg=backgroundColor, fg=foregroundColor, bd=0, cursor="hand2")
        self.btnReturnedItems.place(x=400, y=0, width=85, height=30)

        self.btnSummary = Button(self.lbl_menu, text="SUMMARY", command=self.summary,
                                 font=("times new roman", 12, "bold"),
                                 bg=backgroundColor, fg=foregroundColor, bd=0, cursor="hand2")
        self.btnSummary.place(x=490, y=0, width=85, height=30)

        # ====== Dark or Light Mode ======
        self.light = ImageTk.PhotoImage(file="images/light-mode1.png")
        self.dark = ImageTk.PhotoImage(file="images/dark-mode.png")

        self.themeBtn = Button(self.root, image=self.dark, bg='#333333', activebackground='#333333', bd=0,
                               cursor="hand2")
        self.themeBtn.place(x=1450, y=30, width=80, height=30)
        self.themeBtn.bind("<ButtonRelease-1>", self.toggle)

    def toggle(self, e):
        global switch_value
        if switch_value is False:
            self.themeBtn.config(image=self.dark)

            # Changes the window to dark theme
            self.title.config(bg='#333333', fg='#F2F2F2')
            self.divider.config(bg='#F2F2F2')
            self.themeBtn.config(bg='#333333', activebackground='#333333')
            self.lbl_menu.config(bg="#333333")
            self.btn_category.config(bg="#333333", fg="white")
            self.btn_location.config(bg="#333333", fg="white")
            self.btn_product.config(bg="#333333", fg="white")
            self.btn_billing.config(bg="#333333", fg="white")
            self.btnReturnedItems.config(bg="#333333", fg="white")

            self.logo = ImageTk.PhotoImage(file="images/logoB.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            switch_value = True
        else:
            self.themeBtn.config(image=self.light)

            # Changes the window to light theme
            self.title.config(bg='#F2F2F2', fg='#333333')
            self.divider.config(bg='#333333')
            self.themeBtn.config(bg='#F2F2F2', activebackground='#F2F2F2')
            self.lbl_menu.config(bg="#F2F2F2")
            self.btn_category.config(bg="#F2F2F2", fg="black")
            self.btn_location.config(bg="#F2F2F2", fg="black")
            self.btn_product.config(bg="#F2F2F2", fg="black")
            self.btn_billing.config(bg="#F2F2F2", fg="black")
            self.btnReturnedItems.config(bg="#F2F2F2", fg="black")

            self.logo = ImageTk.PhotoImage(file="images/logoW.png")
            self.logoImage = Label(self.root, image=self.logo).place(x=5, y=5, width=120, height=80)

            switch_value = False

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def location(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = locationClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillClass(self.new_win)

    def returnedItem(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = returnedItems(self.new_win)

    def summary(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = allSummary(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = stockManagement(root)
    root.mainloop()

# Software By Usman Amjad(UA)
