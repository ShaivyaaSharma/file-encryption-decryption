import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import simpledialog

#PASSWORD
PASSWORD = "quagmire"

def verify_master_password():
    root = tk.Tk()
    root.withdraw()
    tries = 3
    while tries > 0:
        password = simpledialog.askstring(" Password", "Enter  Password:", show="*")
        if password == PASSWORD:
            root.destroy()
            return True
        else:
            tries -= 1
            messagebox.showerror("Error", f"Incorrect password! {tries} tries left.")
    root.destroy()
    return False

if not verify_master_password():
    exit()

# ENCRYPTION LOGIC
def generate_key():
    return Fernet.generate_key()

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(output_file, 'wb') as f:
        f.write(decrypted)

# GUI 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Premium File Encrypter")
app.geometry("500x400")

key = None
selected_file = None

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        file_label.configure(text=f"Selected: {os.path.basename(selected_file)}")

def save_as_encrypt():
    global key, selected_file
    if not selected_file:
        messagebox.showwarning("Warning", "Select a file first!")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc")])
    if save_path:
        key = generate_key()
        encrypt_file(selected_file, save_path, key)
        with open(save_path + ".key", 'wb') as key_file:
            key_file.write(key)
        messagebox.showinfo("Success", f"File encrypted!\nKey saved as: {save_path}.key")

def save_as_decrypt():
    global selected_file
    if not selected_file:
        messagebox.showwarning("Warning", "Select a file first!")
        return
    key_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
    if not key_path:
        return
    with open(key_path, 'rb') as kf:
        key = kf.read()
    save_path = filedialog.asksaveasfilename(defaultextension=".dec", filetypes=[("Decrypted Files", "*.dec"), ("All Files", "*.*")])
    if save_path:
        try:
            decrypt_file(selected_file, save_path, key)
            messagebox.showinfo("Success", f"File decrypted!\nSaved as: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")

# UI ELEMENTS 
title_label = ctk.CTkLabel(app, text="File Encrypter", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

file_label = ctk.CTkLabel(app, text="No file selected", font=("Arial", 14))
file_label.pack(pady=10)

select_btn = ctk.CTkButton(app, text="Select File", command=select_file)
select_btn.pack(pady=10)

encrypt_btn = ctk.CTkButton(app, text="Encrypt & Save As", command=save_as_encrypt)
encrypt_btn.pack(pady=10)

decrypt_btn = ctk.CTkButton(app, text="Decrypt & Save As", command=save_as_decrypt)
decrypt_btn.pack(pady=10)

exit_btn = ctk.CTkButton(app, text="Exit", fg_color="red", command=app.destroy)
exit_btn.pack(pady=20)

app.mainloop()
