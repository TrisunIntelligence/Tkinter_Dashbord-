from tkinter import *
class AutoMode:
    def __init__(self, root):
        self.root = root
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("Auto Mode")
        self.root.configure(bg="#f0f0f0")
        
        Label(root, text="Auto Mode", font=("Arial", 20, "bold"), bg="#343A40", fg="white", pady=10).pack(fill="x")
        
        main_frame = Frame(self.root, bg='white', bd=2, relief='ridge')
        main_frame.pack(padx=30, pady=5, fill='both', expand=True)

        header = Frame(main_frame, bg='gray')
        header.place(x=30, y=10, width=780, height=50)
        Label(header, text="TRIM COMPUTER LOWER ASSEMBLY STATION VISION INSPECTION LH", bg='gray', fg='white', font=("Arial", 12, "bold")).pack()

        vision_frame = Frame(main_frame, bg='black')
        vision_frame.place(x=30, y=65, width=500, height=350)
        Label(vision_frame, text="Inspected Result", bg='black', fg='white', font=("Arial", 10, "bold")).pack()
   
        # Machine data status
        machine_frame = Frame(main_frame, bg='#f8f9fa', bd=2, relief='groove')
        machine_frame.place(x=535, y=65, width=300, height=350)

        
        Label(machine_frame, text="Machine Data Status", font=("Arial", 12, "bold"),
            bg='#343a40', fg='white', pady=10).pack(fill='x')

        # Field styling helper
        def labeled_entry(parent, label_text):
            Label(parent, text=label_text, bg='#f8f9fa', font=("Arial", 10, "bold")).pack(pady=(15, 2))
            Entry(parent, font=("Arial", 12), width=28, bd=1, relief="solid").pack(pady=(0, 5))

        # Fields
        
        labeled_entry(machine_frame, "Printed Data")
        labeled_entry(machine_frame, "Live Data")
        labeled_entry(machine_frame, "Scanned Data")

        # Connection Status Section
        connection_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        connection_frame.place(x=840, y=10, width=350, height=60)
        Label(connection_frame, text="PLC Status", bg='white', font=("Arial", 10, "bold")).grid(row=0, column=0, padx=20)
        Label(connection_frame, text="Connected", bg='black', fg='green', font=("Arial", 10)).grid(row=1, column=0)
        Label(connection_frame, text="Camera Status", bg='white', font=("Arial", 10, "bold")).grid(row=0, column=1, padx=20)
        Label(connection_frame, text="Connected", bg='black', fg='green', font=("Arial", 10)).grid(row=1, column=1)
        

        # Date and Time Section
        datetime_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        datetime_frame.place(x=840, y=80, width=350, height=50)
        Label(datetime_frame, text="Date : 25 - March - 2025", bg='white', font=("Arial", 10)).pack()
        Label(datetime_frame, text="Time : 02:54:31 pm", bg='white', font=("Arial", 10)).pack()

        # Status Information Section
        status_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        status_frame.place(x=840, y=120, width=350, height=380)
        Label(status_frame, text="Machine Status", bg='white', font=("Arial", 10, "bold")).pack()
        Label(status_frame, text="NG PART Press Reset Button", bg='white', fg='red', font=("Arial", 10)).pack()

        # Result Section
        result_frame = Frame(main_frame, bg='red', bd=2, relief='ridge')
        result_frame.place(x=30, y=420, width=780, height=50)
        Label(result_frame, text="Result : WRONG Part/ NG PART", bg='red', fg='white', font=("Arial", 12, "bold")).pack()

        # Parts Count Section
        count_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        count_frame.place(x=30, y=480, width=780, height=80)  

        # Configure grid columns to auto-expand and center
        count_frame.grid_columnconfigure(0, weight=1)
        count_frame.grid_columnconfigure(1, weight=1)
        count_frame.grid_columnconfigure(2, weight=1)

        # Row 0 - Labels
        Label(count_frame, text="OK PARTS COUNT", bg='white', font=("Arial", 10, "bold")).grid(row=0, column=0, pady=(10, 2))
        Label(count_frame, text="NG PARTS COUNT", bg='white', font=("Arial", 10, "bold")).grid(row=0, column=1, pady=(10, 2))
        Label(count_frame, text="TOTAL PARTS COUNT", bg='white', font=("Arial", 10, "bold")).grid(row=0, column=2, pady=(10, 2))

        # Row 1 - Values
        Label(count_frame, text="857", bg='white', font=("Arial", 12, "bold")).grid(row=1, column=0)
        Label(count_frame, text="19", bg='white', font=("Arial", 12, "bold")).grid(row=1, column=1)
        Label(count_frame, text="876", bg='white', font=("Arial", 12, "bold")).grid(row=1, column=2)


        
        logout_button = Button(main_frame, text="Log Out", bg='red', fg='white', font=("Arial", 12, "bold"),command=self.logout)
        logout_button.place(x=840, y=510, width=350, height=50)
    
    def logout(self):
        from login_system import Login
        Login(self.root)

        # Button(root, text="Back to Dashboard", command=self.back, font=("Arial", 14)).pack(pady=50)

    def back(self):
        from admin_dashbord import AdminDashboard
        AdminDashboard(self.root, username="Admin")