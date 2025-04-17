from tkinter import *
from tkinter import ttk, messagebox
from database_connectivity import connect_db
from delete_user import DeleteUser
from update_user import UpdateUser

class ViewUserscls:
    def __init__(self, root):
        self.root = root
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("View Users")
        self.root.state("zoomed")
        self.root.configure(bg="#f8f9fa")

        Label(self.root, text="View All Users", font=("Segoe UI", 22, "bold"),
              bg="#343A40", fg="white", pady=15).pack(fill="x")

        main_frame = Frame(self.root, bg="#ffffff", bd=2, relief=RIDGE)
        main_frame.place(x=30, y=80, relwidth=0.94, relheight=0.84)

        Button(main_frame, text="Update User", font=("Segoe UI", 11, "bold"), bg="#17a2b8", fg="white",
               cursor="hand2", bd=0, activebackground="#138496", activeforeground="white",
               command=self.open_update_user).place(x=30, y=15, width=120, height=35)

        Button(main_frame, text="Delete User", font=("Segoe UI", 11, "bold"), bg="#dc3545", fg="white",
               cursor="hand2", bd=0, activebackground="#bd2130", activeforeground="white",
               command=self.open_delete_user).place(x=170, y=15, width=120, height=35)

        Button(main_frame, text="Back", font=("Segoe UI", 11, "bold"), bg="#6c757d", fg="white",
               cursor="hand2", bd=0, activebackground="#5a6268", activeforeground="white",
               command=self.back).place(x=310, y=15, width=100, height=35)

        # Treeview Frame
        frame = Frame(main_frame, bg="#ffffff", bd=2, relief=RIDGE)
        frame.place(x=10, y=70, relwidth=0.975, relheight=0.87)

        columns = ("ID", "Name", "Username", "Email", "Mobile", "Department", "Role")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")

        vsb = Scrollbar(frame, orient=VERTICAL, command=self.tree.yview)
        hsb = Scrollbar(frame, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side=RIGHT, fill=Y)
        hsb.pack(side=BOTTOM, fill=X)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=130)

        self.tree.pack(fill=BOTH, expand=True)

        self.load_users()

    def load_users(self):
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT id, name, username, email, mobile, department, role FROM users")
            rows = cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def get_selected_user_id(self):
        selected = self.tree.selection()
        if selected:
            return self.tree.item(selected[0], "values")[0]
        return None

    def open_update_user(self):
        user_id = self.get_selected_user_id()
        if user_id:
            UpdateUser(self.root, user_id)
        else:
            messagebox.showwarning("Warning", "Please select a user to update.")

    def open_delete_user(self):
        user_id = self.get_selected_user_id()
        if user_id:
            DeleteUser(self.root, user_id)
        else:
            messagebox.showwarning("Warning", "Please select a user to delete.")

    def back(self):
        from add_user import AddUser
        AddUser(self.root)
