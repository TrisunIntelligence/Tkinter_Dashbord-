from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin_dashbord import AdminDashboard
from operator_dashboard import OperatorDashboard
import mysql.connector

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1920x1080")
        self.root.configure(bg="#f4f4f4")
        self.create_login_ui()

    def create_login_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        try:
            self.side_img = Image.open("img/logo.png")
            self.side_img = self.side_img.resize((400, 450))
            self.side_img = ImageTk.PhotoImage(self.side_img)
            lbl_side_img = Label(self.root, image=self.side_img, bg="#1E2D3D")
            lbl_side_img.place(x=250, y=100)
        except:
            print("Warning: Logo image not found!")
            
        frame1 = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        frame1.place(x=620, y=100, width=400, height=450)

        Label(frame1, text="Login System", font=("Arial", 18, "bold"), fg="#007bff", bg="white").pack(pady=20)

        # Username
        Label(frame1, text="Username", font=("Arial", 12), bg="white", anchor="w").pack(pady=5, padx=30, fill="x")
        self.username_entry = Entry(frame1, font=("Arial", 12), width=30, bd=2, relief=SOLID)
        self.username_entry.pack(pady=5)

        # Password
        Label(frame1, text="Password", font=("Arial", 12), bg="white", anchor="w").pack(pady=5, padx=30, fill="x")
        self.password_entry = Entry(frame1, font=("Arial", 12), width=30, bd=2, relief=SOLID, show="*")
        self.password_entry.pack(pady=5)

        # Role Selection
        Label(frame1, text="Role:", font=("Arial", 12), bg="white").pack(pady=5)
        self.role_var = StringVar(value="operator")
        role_frame = Frame(frame1, bg="white")
        role_frame.pack(pady=5)
        Radiobutton(role_frame, text="Admin", variable=self.role_var, value="admin", bg="white", font=("Arial", 11)).pack(side="left", padx=10)
        Radiobutton(role_frame, text="Operator", variable=self.role_var, value="operator", bg="white", font=("Arial", 11)).pack(side="left", padx=10)

        # Login Button
        Button(frame1, text="Login", font=("Arial", 14, "bold"), bg="#007bff", fg="white", width=15, command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        role = self.role_var.get()

        if not username or not password:
            return

        try:
            conn = mysql.connector.connect( host="localhost", username="root", password="Joti@@1705", database="trisun")
            cursor = conn.cursor()
            query = "SELECT role FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            conn.close()

            if result !=None:
                if role == "admin":
                    AdminDashboard(self.root, username)
                else:
                    OperatorDashboard(self.root, username)
            else:
                messagebox.showerror("Login Failed", "Invalid credentials or role mismatch.")

        except mysql.Error as e:
            messagebox.showerror("Database Error", str(e))

# Run the app
if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
