import customtkinter as ctk
from tkinter import messagebox

class PasswordChecker:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, fg_color="#FFE5B4")
        self.frame.pack(pady=10, padx=20, fill="x")

        password_label = ctk.CTkLabel(self.frame, text="Enter Password for Hive Check:", font=("Arial", 14))
        password_label.pack(anchor="w", padx=10, pady=5)

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter password", show="*", width=300)
        self.password_entry.pack(pady=5, padx=10)

        brute_force_button = ctk.CTkButton(self.frame, text="Brute Force Check 🐝", command=self.brute_force_check)
        brute_force_button.pack(side="left", padx=10, pady=10)

        dictionary_check_button = ctk.CTkButton(self.frame, text="Dictionary Check 🍯", command=self.dictionary_check)
        dictionary_check_button.pack(side="right", padx=10, pady=10)

    def brute_force_check(self):
        password = self.password_entry.get()
        messagebox.showinfo("Brute Force", f"Brute forcing password '{password}' with our bee squad...")

    def dictionary_check(self):
        password = self.password_entry.get()
        messagebox.showinfo("Dictionary Check", f"Searching password '{password}' in the honey dictionary...")
