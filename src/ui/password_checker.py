import customtkinter as ctk
from tkinter import messagebox
from src.services.brute_force_service import estimate_crack_time

class PasswordChecker:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(pady=10, padx=20, fill="x")

        password_label = ctk.CTkLabel(self.frame, text="Enter Password for Hive Check:", font=("Arial", 14))
        password_label.pack(anchor="w", padx=10, pady=5)

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter password", show="*", width=300)
        self.password_entry.pack(pady=5, padx=10)

        brute_force_button = ctk.CTkButton(self.frame, text="Estimate Brute Force Time", command=self.brute_force_check)
        brute_force_button.pack(pady=10)

    def brute_force_check(self):
        password = self.password_entry.get()
        # TODO: Get hacker skill level from user input
        hacker_skill = "organization"  
        result = estimate_crack_time(password, hacker_skill)
        messagebox.showinfo("Brute Force Time Estimate", result)