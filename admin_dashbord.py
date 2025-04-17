from tkinter import *
from add_user import AddUser
from manual_mode import ManualMode
from auto_mode import AutoMode
from view_report import ViewReport

class AdminDashboard:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.create_dashboard()

    def create_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="#f0f2f5")
        self.root.title("Admin Dashboard")

        Label(self.root, text="Admin Dashboard", font=("Arial", 20, "bold"),
              bg="#343A40", fg="white", pady=10).pack(fill="x")

        Label(self.root, text=f"Welcome Admin: {self.username}", font=("Arial", 15, "bold"),
              fg="#007bff", bg="#f0f2f5").pack(pady=30)

        button_frame = Frame(self.root, bg="#f0f2f5")
        button_frame.pack()

        self.create_button(button_frame, "Manual Mode", "#007BFF", "white", 0, 0, self.open_manual_mode)
        self.create_button(button_frame, "Auto Mode", "#28A745", "white", 0, 1, self.open_auto_mode)
        self.create_button(button_frame, "Add Users", "#FFC107", "black", 1, 0, self.open_add_users)
        self.create_button(button_frame, "View Report", "#DC3545", "white", 1, 1, self.open_view_report)

        Button(self.root, text="Logout", font=("Arial", 14, "bold"), bg="red", fg="white",
               padx=20, pady=10, width=20, command=self.logout).pack(pady=40)

    def create_button(self, parent, text, bg_color, fg_color, row, col, command=None):
        Button(parent, text=text, font=("Arial", 14, "bold"), bg=bg_color, fg=fg_color,
               padx=10, pady=10, width=20, height=2, command=command).grid(row=row, column=col, padx=20, pady=20)

    def open_manual_mode(self):
        ManualMode(self.root)

    def open_auto_mode(self):
        AutoMode(self.root)

    def open_add_users(self):
        AddUser(self.root)

    def open_view_report(self):
        ViewReport(self.root)

    def logout(self):
        from login_system import Login
        Login(self.root)

