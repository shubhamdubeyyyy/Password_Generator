import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string
def get_strength(password):
    length = len(password)
    strength = 0
    if any(c.islower() for c in password): strength += 1
    if any(c.isupper() for c in password): strength += 1
    if any(c.isdigit() for c in password): strength += 1
    if any(c in string.punctuation for c in password): strength += 1
    if length >= 12: strength += 1

    if strength <= 2:
        return "Weak", "red"
    elif strength == 3:
        return "Medium", "orange"
    else:
        return "Strong", "green"
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return̥
        selected_chars = ""
        if var_upper.get():
            selected_chars += string.ascii_uppercase
        if var_lower.get():
            selected_chars += string.ascii_lowercase
        if var_digits.get():
            selected_chars += string.digits
        if var_symbols.get():
            selected_chars += string.punctuation
        if not selected_chars:
            messagebox.showwarning("Warning", "Select at least one character type.")
            return
        password = ''.join(random.choice(selected_chars) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        strength, color = get_strength(password)
        strength_label.config(text=f"Strength: {strength}", fg=color)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
def save_to_file():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Warning", "No password to save.")
        return
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'w') as f:
            f.write(password)
        messagebox.showinfo("Saved", f"Password saved to {filepath}")
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("450x350")
root.resizable(False, False)
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
entry_length = tk.Entry(root, font=("Arial", 12), justify="center", width=10)
entry_length.pack()
frame_options = tk.Frame(root)
frame_options.pack(pady=5)
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)
tk.Checkbutton(frame_options, text="Uppercase", variable=var_upper).grid(row=0, column=0)
tk.Checkbutton(frame_options, text="Lowercase", variable=var_lower).grid(row=0, column=1)
tk.Checkbutton(frame_options, text="Numbers", variable=var_digits).grid(row=1, column=0)
tk.Checkbutton(frame_options, text="Symbols", variable=var_symbols).grid(row=1, column=1)
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=10)
entry_password = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
entry_password.pack()
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 10))
strength_label.pack(pady=2)
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Save to File", command=save_to_file).grid(row=0, column=1, padx=5)
root.mainloop()
