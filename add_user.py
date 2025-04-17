from tkinter import *
from tkinter import messagebox
from database_connectivity import connect_db
from view_users import ViewUsers
import re
import random


class AddUser:
    def __init__(self, root):
        self.root = root
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("User Management ")
        self.root.state("zoomed")
        self.root.configure(bg="#f8f9fa")

        # Variables
        self.name_var = StringVar()
        self.username_var = StringVar()
        self.email_var = StringVar()
        self.mobile_var = StringVar()
        self.password_var = StringVar()
        self.department_var = StringVar()
        self.role_var = StringVar(value="Operator")

        # Department options
        self.department_options = ["HR", "IT", "Sales", "Marketing", "Production", "Finance", "R&D"]
        self.department_var.set("Select Department")

        # --- Main Frame ---
        main_frame = Frame(self.root, bg="#ffffff", bd=2, relief=RIDGE)
        main_frame.place(x=30, y=80, relwidth=0.94, relheight=0.84)

        Label(main_frame, text="Add New User", font=("Segoe UI", 16, "bold"),
              bg="#007bff", fg="white").pack(fill=X)

        # --- Form Fields ---
        Label(main_frame, text="Name:", font=("Segoe UI", 12), bg="#ffffff").place(x=30, y=50)
        Entry(main_frame, textvariable=self.name_var, font=("Segoe UI", 12), width=25).place(x=130, y=50)

        Label(main_frame, text="Username:", font=("Segoe UI", 12), bg="#ffffff").place(x=480, y=50)
        Entry(main_frame, textvariable=self.username_var, font=("Segoe UI", 12), width=25, state='readonly').place(x=580, y=50)

        Label(main_frame, text="Email:", font=("Segoe UI", 12), bg="#ffffff").place(x=30, y=100)
        email_entry = Entry(main_frame, textvariable=self.email_var, font=("Segoe UI", 12), width=25)
        email_entry.place(x=130, y=100)
        email_entry.bind("<FocusOut>", self.generate_username_from_email)

        Label(main_frame, text="Mobile:", font=("Segoe UI", 12), bg="#ffffff").place(x=480, y=100)
        Entry(main_frame, textvariable=self.mobile_var, font=("Segoe UI", 12), width=25).place(x=580, y=100)

        Label(main_frame, text="Password:", font=("Segoe UI", 12), bg="#ffffff").place(x=30, y=150)
        Entry(main_frame, textvariable=self.password_var, font=("Segoe UI", 12), width=25, show="*").place(x=130, y=150)

        Label(main_frame, text="Department:", font=("Segoe UI", 12), bg="#ffffff").place(x=480, y=150)
        OptionMenu(main_frame, self.department_var, *self.department_options).place(x=580, y=150)

        Label(main_frame, text="Role:", font=("Segoe UI", 12), bg="#ffffff").place(x=30, y=200)
        OptionMenu(main_frame, self.role_var, "Admin", "Operator").place(x=130, y=200)

        # --- Buttons ---
        Button(main_frame, text="Add User", font=("Segoe UI", 12), bg="#28a745", fg="white",
               command=self.add_user).place(x=420, y=270)

        Button(main_frame, text="View Users", font=("Segoe UI", 12), bg="#007bff", fg="white",
               command=self.open_view_users).place(x=270, y=270)

        Button(main_frame, text="Back", font=("Segoe UI", 12), bg="#6c757d", fg="white",
               command=self.back).place(x=570, y=270)

    def clear_fields(self):
        self.name_var.set("")
        self.username_var.set("")
        self.email_var.set("")
        self.mobile_var.set("")
        self.password_var.set("")
        self.department_var.set("Select Department")
        self.role_var.set("Operator")

    def generate_username_from_email(self, event=None):
        email = self.email_var.get().strip()
        if not email or '@' not in email:
            return

        base_username = re.sub(r'\W+', '', email[:5].lower())

        try:
            db = connect_db()
            cursor = db.cursor()

            attempts = 0
            while attempts < 50:
                rand_num = random.randint(100, 999)
                new_username = f"{base_username}{rand_num}"

                cursor.execute("SELECT * FROM users WHERE username = %s", (new_username,))
                if not cursor.fetchone():
                    self.username_var.set(new_username)
                    return

                attempts += 1

            self.username_var.set(f"{base_username}{random.randint(1000, 9999)}")

        except Exception as e:
            print("Username generation error:", e)
            self.username_var.set(f"{base_username}{random.randint(100, 999)}")

    def add_user(self):
        name = self.name_var.get().strip()
        username = self.username_var.get().strip()
        email = self.email_var.get().strip()
        mobile = self.mobile_var.get().strip()
        password = self.password_var.get().strip()
        department = self.department_var.get().strip()
        role = self.role_var.get().strip()

        if not all([name, username, email, mobile, department, password, role]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if department == "Select Department":
            messagebox.showerror("Error", "Please select a valid department.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        if not (mobile.isdigit() and len(mobile) == 10):
            messagebox.showerror("Error", "Mobile must be exactly 10 digits.")
            return

        try:
            db = connect_db()
            cursor = db.cursor()

            cursor.execute("SELECT * FROM users WHERE username=%s OR email=%s", (username, email))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username or Email already exists!")
                return

            cursor.execute("INSERT INTO users (name, username, email, mobile, department, password, role) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (name, username, email, mobile, department, password, role))
            db.commit()
            self.clear_fields()
            self.open_view_users()
            messagebox.showinfo("Success", f"User added successfully.\nUsername: {username}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_view_users(self):
        ViewUsers(self.root)

    def back(self):
        from admin_dashbord import AdminDashboard
        AdminDashboard(self.root, username="Admin")
