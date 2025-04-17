from tkinter import *
class ViewReport:
    def __init__(self, root):
        self.root = root
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("View Report")
        self.root.configure(bg="#f0f0f0")

        Label(root, text="View Report", font=("Arial", 20, "bold"), bg="#343A40", fg="white", pady=10).pack(fill="x")
        Button(root, text="Back to Dashboard", command=self.back, font=("Arial", 14)).pack(pady=50)

    def back(self):
        from admin_dashbord import AdminDashboard
        AdminDashboard(self.root, username="Admin")