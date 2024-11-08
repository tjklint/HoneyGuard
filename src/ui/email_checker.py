import customtkinter as ctk
from tkinter import messagebox
from config.settings import FRAME_BG_COLOR, BUTTON_COLOR, TEXT_COLOR

class EmailChecker:
    def __init__(self, parent):
        self.frame = ctk.CTkFrame(parent, fg_color=FRAME_BG_COLOR)
        self.frame.pack(pady=10, padx=20, fill="x")

        email_label = ctk.CTkLabel(self.frame, text="Enter Email for Honey Check:", font=("Arial", 14), text_color=TEXT_COLOR)
        email_label.pack(anchor="w", padx=10, pady=5)

        self.email_entry = ctk.CTkEntry(self.frame, placeholder_text="example@example.com", width=300)
        self.email_entry.pack(pady=5, padx=10)

        check_email_button = ctk.CTkButton(self.frame, text="Check Email 🍯", fg_color=BUTTON_COLOR, command=self.check_email)
        check_email_button.pack(pady=10)

    def check_email(self):
        email = self.email_entry.get()
        messagebox.showinfo("Checking Email", f"Checking email '{email}' in the honeycombs...")
