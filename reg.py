import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    
    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Here you could add code to save the data or process it further
    messagebox.showinfo("Success", f"Registration Successful!\nName: {name}\nEmail: {email}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the labels and entries
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Register", command=submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
