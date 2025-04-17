# # def deleteReAuthenticate()
# from tkinter import *
# from tkinter import messagebox
# from database import connect_db

# class DeleteUser:
#     def __init__(self, root):
#         self.root = root
#         for widget in self.root.winfo_children():
#             widget.destroy()
#         self.root.title("Delete User") 
#         self.root.geometry("700x400")
#         self.root.configure(bg="#f8f9fa")

#         self.username_var = StringVar()

#         Label(self.root, text="Delete User", font=("Segoe UI", 20, "bold"), bg="#dc3545", fg="white", pady=10).pack(fill="x")

#         Label(self.root, text="Enter Username to Delete:", font=("Segoe UI", 12), bg="#f8f9fa").place(x=30, y=80)
#         self.username_entry = Entry(self.root, font=("Segoe UI", 12), textvariable=self.username_var)
#         self.username_entry.place(x=250, y=80, width=250)

#         Button(self.root, text="Search", font=("Segoe UI", 12), bg="#007bff", fg="white",
#                command=self.search_user).place(x=520, y=77)

#         # Labels for user info
#         self.info_label = Label(self.root, font=("Segoe UI", 12), bg="#f8f9fa", fg="#343a40", justify=LEFT)
#         self.info_label.place(x=30, y=150)

#         Button(self.root, text="Delete", font=("Segoe UI", 12), bg="#dc3545", fg="white",
#                command=self.delete_user).place(x=250, y=300)

#         Button(self.root, text="Back", font=("Segoe UI", 12), bg="#6c757d", fg="white",
#                command=self.back).place(x=360, y=300)

#         self.user_id = None

#     def search_user(self):
#         username = self.username_var.get().strip()
#         if not username:
#             messagebox.showerror("Error", "Please enter a username.")
#             return

#         try:
#             db = connect_db()
#             cursor = db.cursor()
#             cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#             user = cursor.fetchone()

#             if user:
#                 self.user_id = user[0]
#                 user_info = f"Name: {user[1]}\nUsername: {user[2]}\nEmail: {user[3]}\nMobile: {user[4]}\nDepartment: {user[5]}\nRole: {user[7]}"
#                 self.info_label.config(text=user_info)
#             else:
#                 self.user_id = None
#                 self.info_label.config(text="")
#                 messagebox.showerror("Not Found", "User not found.")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def delete_user(self):
#         if not self.user_id:
#             messagebox.showwarning("No User Selected", "Search and select a user first.")
#             return

#         confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this user?")
#         if confirm:
#             try:
#                 db = connect_db()
#                 cursor = db.cursor()
#                 cursor.execute("DELETE FROM users WHERE id = %s", (self.user_id,))
#                 db.commit()
#                 messagebox.showinfo("Success", "User deleted successfully.")
#                 self.info_label.config(text="")
#                 self.username_var.set("")
#                 self.user_id = None
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))

#     def back(self):
#         from view_users import ViewUsers
#         ViewUsers(self.root)

from tkinter import *
from tkinter import messagebox, simpledialog
from database_connectivity import connect_db

class DeleteUser:
    def __init__(self, root, user_id):
        self.root = root
        self.user_id = user_id
        self.confirm_delete()

    def confirm_delete(self):
        if not self.two_way_auth():
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this user?")
        if confirm:
            try:
                db = connect_db()
                cursor = db.cursor()
                cursor.execute("DELETE FROM users WHERE id = %s", (self.user_id,))
                db.commit()
                messagebox.showinfo("Success", "User deleted successfully.")
                from view_users import ViewUsers
                ViewUsers(self.root)
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

    def two_way_auth(self):
        admin_password = simpledialog.askstring("Authentication", "Enter Admin Password:", show="*")
        if not admin_password:
            return False

        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE role = 'Admin' AND password = %s", (admin_password,))
            if cursor.fetchone():
                return True
            else:
                messagebox.showerror("Authentication Failed", "Incorrect admin password.")
                return False
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            return False
