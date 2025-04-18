from tkinter import *
from datetime import datetime

class OperatorDashboard:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.create_dashboard()

    def create_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text=f"Welcome Operator: {self.username}", font=("Arial", 20, "bold"), fg="#007bff").pack(pady=10)

        main_frame = Frame(self.root, bg='white', bd=2, relief='ridge')
        main_frame.pack(padx=30, pady=5, fill='both', expand=True)

        header = Frame(main_frame, bg='gray')
        header.place(x=30, y=10, width=805, height=50)
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

         # # Connection Status Section
        connection_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        connection_frame.place(x=840, y=10, width=350, height=60)
        status_inner = Frame(connection_frame, bg='white')
        status_inner.place(relx=0.5, rely=0.5, anchor='center')

        Label(status_inner, text="PLC: ", bg='white', font=("Arial", 11, "bold")).pack(side='left')
        Label(status_inner, text="Connected", bg='white', fg='green', font=("Arial", 11, "bold")).pack(side='left')
        Label(status_inner, text="  |  Camera: ", bg='white', font=("Arial", 11, "bold")).pack(side='left')
        Label(status_inner, text="Connected", bg='white', fg='green', font=("Arial", 11, "bold")).pack(side='left')


       # Date and Time Section (LIVE)
        datetime_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        datetime_frame.place(x=840, y=70, width=350, height=50)
        self.datetime_label = Label(datetime_frame, text="", bg='white', font=("Arial", 10, "bold"))
        self.datetime_label.pack()

        self.update_datetime()  # Start auto update

        # Status Information Section
        status_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        status_frame.place(x=840, y=120, width=350, height=380)
        Label(status_frame, text="Machine Status", bg='white', font=("Arial", 10, "bold")).pack()
        Label(status_frame, text="NG PART Press Reset Button", bg='white', fg='red', font=("Arial", 10)).pack()

        # Result Section
        result_frame = Frame(main_frame, bg='red', bd=2, relief='ridge')
        result_frame.place(x=30, y=420, width=805, height=50)
        Label(result_frame, text="Result : WRONG Part/ NG PART", bg='red', fg='white', font=("Arial", 12, "bold")).pack()

        # Parts Count Section
        count_frame = Frame(main_frame, bg='white', bd=2, relief='ridge')
        count_frame.place(x=30, y=480, width=805, height=80)  

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
    def update_datetime(self):
        now = datetime.now()
        datetime_text = now.strftime("Date: %d - %B - %Y  |  Time: %I:%M:%S %p")
        self.datetime_label.config(text=datetime_text)
        self.datetime_label.after(1000, self.update_datetime)
    
    def logout(self):
        from login_system import Login
        Login(self.root)
