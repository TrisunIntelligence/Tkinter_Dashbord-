# from tkinter import *
# from tkinter import messagebox
# from database_connectivity import connect_db
# import re

# class UpdateUser:
#     def __init__(self, root, user_id):
#         self.root = root
#         self.user_id = user_id
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         self.root.title("Update User")
#         self.root.configure(bg="#f8f9fa")

#         Label(self.root, text="Update User Information", font=("Segoe UI", 20, "bold"),
#               bg="#343A40", fg="white", pady=15).pack(fill="x")

#         # Input Variables
#         self.name_var = StringVar()
#         self.username_var = StringVar()
#         self.email_var = StringVar()
#         self.mobile_var = StringVar()
#         self.department_var = StringVar()
#         self.password_var = StringVar()
#         self.role_var = StringVar()

#         # Labels and Entries
#         form_y = 120
#         Label(self.root, text="Name:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=30, y=form_y)
#         Entry(self.root, textvariable=self.name_var, font=("Segoe UI", 12)).place(x=150, y=form_y)

#         Label(self.root, text="Username:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=450, y=form_y)
#         Entry(self.root, textvariable=self.username_var, font=("Segoe UI", 12), state='readonly').place(x=570, y=form_y)

#         Label(self.root, text="Email:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=30, y=form_y+40)
#         Entry(self.root, textvariable=self.email_var, font=("Segoe UI", 12)).place(x=150, y=form_y+40)

#         Label(self.root, text="Mobile:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=450, y=form_y+40)
#         Entry(self.root, textvariable=self.mobile_var, font=("Segoe UI", 12)).place(x=570, y=form_y+40)

#         Label(self.root, text="Password:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=30, y=form_y+80)
#         Entry(self.root, textvariable=self.password_var, font=("Segoe UI", 12), show="*", state='readonly').place(x=150, y=form_y+80)

#         Label(self.root, text="Department:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=450, y=form_y+80)
#         OptionMenu(self.root, self.department_var, "HR", "IT", "Sales", "Marketing", "Production", "Finance", "R&D").place(x=570, y=form_y+80)

#         Label(self.root, text="Role:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=30, y=form_y+120)
#         OptionMenu(self.root, self.role_var, "Admin", "Operator").place(x=150, y=form_y+120)

#         # Buttons
#         Button(self.root, text="Update", font=("Segoe UI", 12, "bold"), bg="#28a745", fg="white",
#                cursor="hand2", command=self.update_user).place(x=250, y=480, width=100, height=35)

#         Button(self.root, text="Back", font=("Segoe UI", 12), bg="#6c757d", fg="white",
#                cursor="hand2", command=self.back).place(x=370, y=480, width=100, height=35)

#         self.load_user_data()

#     def load_user_data(self):
#         try:
#             db = connect_db()
#             cursor = db.cursor()
#             cursor.execute("SELECT name, username, email, mobile, department, password, role FROM users WHERE id = %s", (self.user_id,))
#             result = cursor.fetchone()
#             if result:
#                 self.name_var.set(result[0])
#                 self.username_var.set(result[1])
#                 self.email_var.set(result[2])
#                 self.mobile_var.set(result[3])
#                 self.department_var.set(result[4])
#                 self.password_var.set(result[5])
#                 self.role_var.set(result[6])
#             else:
#                 messagebox.showerror("Error", "User not found.")
#         except Exception as e:
#             messagebox.showerror("Database Error", str(e))

#     def update_user(self):
#         name = self.name_var.get().strip()
#         username = self.username_var.get().strip()
#         email = self.email_var.get().strip()
#         mobile = self.mobile_var.get().strip()
#         department = self.department_var.get().strip()
#         password = self.password_var.get().strip()
#         role = self.role_var.get().strip()

#         # --- Validation ---
#         if not all([name, username, email, mobile, department, password, role]):
#             messagebox.showerror("Validation Error", "All fields are required.")
#             return

#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             messagebox.showerror("Validation Error", "Invalid email format.")
#             return

#         if not (mobile.isdigit() and len(mobile) == 10):
#             messagebox.showerror("Validation Error", "Mobile number must be exactly 10 digits.")
#             return

#         # --- Database Update ---
#         try:
#             db = connect_db()
#             cursor = db.cursor()
#             cursor.execute("""
#                 UPDATE users SET 
#                     name=%s, username=%s, email=%s, mobile=%s, 
#                     department=%s, password=%s, role=%s 
#                 WHERE id=%s
#             """, (
#                 name, username, email, mobile,
#                 department, password, role,
#                 self.user_id
#             ))
#             db.commit()
#             self.back()
#             messagebox.showinfo("Success", "User updated successfully!")
#         except Exception as e:
#             messagebox.showerror("Database Error", str(e))

#     def back(self):
#         from view_users import ViewUsers
#         ViewUsers(self.root)
from tkinter import *
from tkinter import messagebox
from database_connectivity import connect_db
import re

class UpdateUser:
    def __init__(self, root, user_id):
        self.root, self.user_id = root, user_id
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Update User")
        self.root.configure(bg="#f8f9fa")
        Label(self.root, text="Update User Information", font=("Segoe UI", 20, "bold"),
              bg="#343A40", fg="white", pady=15).pack(fill="x")

        # Variables
        self.name_var = StringVar()
        self.username_var = StringVar()
        self.email_var = StringVar()
        self.mobile_var = StringVar()
        self.department_var = StringVar()
        self.password_var = StringVar()
        self.role_var = StringVar()

        # Form Layout
        form_y = 120
        fields = [
            ("Name:", self.name_var, 30, 0, "entry"),
            ("Username:", self.username_var, 450, 0, "readonly"),
            ("Email:", self.email_var, 30, 40, "entry"),
            ("Mobile:", self.mobile_var, 450, 40, "entry"),
            ("Password:", self.password_var, 30, 80, "readonly_pw"),
            ("Department:", self.department_var, 450, 80, "option", ["HR", "IT", "Sales", "Marketing", "Production", "Finance", "R&D"]),
            ("Role:", self.role_var, 30, 120, "option", ["Admin", "Operator"])
        ]

        for label, var, x, dy, ftype, *opts in fields:
            Label(self.root, text=label, font=("Segoe UI", 12), bg="#f8f9fa").place(x=x, y=form_y+dy)
            px = x + 120
            py = form_y + dy
            if ftype == "entry":
                Entry(self.root, textvariable=var, font=("Segoe UI", 12)).place(x=px, y=py)
            elif ftype == "readonly":
                Entry(self.root, textvariable=var, font=("Segoe UI", 12), state='readonly').place(x=px, y=py)
            elif ftype == "readonly_pw":
                Entry(self.root, textvariable=var, font=("Segoe UI", 12), state='readonly', show="*").place(x=px, y=py)
            elif ftype == "option":
                OptionMenu(self.root, var, *opts[0]).place(x=px, y=py)

        # Buttons
        Button(self.root, text="Update", font=("Segoe UI", 12, "bold"), bg="#28a745", fg="white",
               cursor="hand2", command=self.update_user).place(x=250, y=480, width=100, height=35)
        Button(self.root, text="Back", font=("Segoe UI", 12), bg="#6c757d", fg="white",
               cursor="hand2", command=self.back).place(x=370, y=480, width=100, height=35)

        self.load_user_data()

    def load_user_data(self):
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT name, username, email, mobile, department, password, role FROM users WHERE id = %s", (self.user_id,))
            result = cursor.fetchone()
            if result:
                vars_ = [self.name_var, self.username_var, self.email_var, self.mobile_var,
                         self.department_var, self.password_var, self.role_var]
                for var, value in zip(vars_, result):
                    var.set(value)
            else:
                messagebox.showerror("Error", "User not found.")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def update_user(self):
        name, username = self.name_var.get().strip(), self.username_var.get().strip()
        email, mobile = self.email_var.get().strip(), self.mobile_var.get().strip()
        department, password = self.department_var.get().strip(), self.password_var.get().strip()
        role = self.role_var.get().strip()

        if not all([name, username, email, mobile, department, password, role]):
            return messagebox.showerror("Validation Error", "All fields are required.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return messagebox.showerror("Validation Error", "Invalid email format.")
        if not (mobile.isdigit() and len(mobile) == 10):
            return messagebox.showerror("Validation Error", "Mobile number must be exactly 10 digits.")

        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE users SET name=%s, username=%s, email=%s, mobile=%s, 
                department=%s, password=%s, role=%s WHERE id=%s
            """, (name, username, email, mobile, department, password, role, self.user_id))
            db.commit()
            self.back()
            messagebox.showinfo("Success", "User updated successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def back(self):
        from view_users import ViewUsers
        ViewUsers(self.root)
