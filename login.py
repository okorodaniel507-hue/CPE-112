# Name: OKORO DANIEL
# Mat No: ENG2504619

import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check login details
    if username == "OKORO DANIEL" and password == "ENG2504619":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x180")

# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

root.mainloop()
