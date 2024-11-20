import customtkinter as ctk
from tkinter import messagebox
from config.settings import NORMAL_FONT, TEXT_COLOR

from src.services.brute_force_service import estimate_crack_time

class PasswordChecker:
    def __init__(self, parent):
        # Set background to white and remove corner radius
        self.frame = ctk.CTkFrame(parent, fg_color="#FFFFFF", corner_radius=0)
        self.frame.pack(fill="both", expand=True)

        # Title
        title_label = ctk.CTkLabel(self.frame, text="Password Strength Checker", font=NORMAL_FONT, text_color=TEXT_COLOR)
        title_label.pack(pady=(10, 20))

        # Password Entry
        password_label = ctk.CTkLabel(self.frame, text="Enter Password:", font=NORMAL_FONT, text_color=TEXT_COLOR)
        password_label.pack(anchor="w", padx=20)

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter password", show="*", width=300)
        self.password_entry.pack(pady=10, padx=20)

        # Hacker Skill Dropdown
        skill_label = ctk.CTkLabel(self.frame, text="Select Hacker Skill Level:", font=NORMAL_FONT, text_color=TEXT_COLOR)
        skill_label.pack(anchor="w", padx=20)

        self.skill_level_var = ctk.StringVar(value="organization")
        self.skill_level_dropdown = ctk.CTkOptionMenu(
            self.frame,
            variable=self.skill_level_var,
            values=["amateur", "intermediate", "organization"]
        )
        self.skill_level_dropdown.pack(pady=10, padx=20)

        # Submit Button
        submit_button = ctk.CTkButton(
            self.frame,
            text="Check Password Strength",
            command=self.brute_force_check,
            font=NORMAL_FONT,
            width=200
        )
        submit_button.pack(pady=(20, 10))

    def brute_force_check(self):
        password = self.password_entry.get()
        hacker_skill = self.skill_level_var.get()
        result = estimate_crack_time(password, hacker_skill)
        messagebox.showinfo("Brute Force Time Estimate", result)
