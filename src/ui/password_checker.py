import customtkinter as ctk
from tkinter import Canvas
from config.settings import CHARACTER_SETS, HACKER_SPEEDS
from src.services.brute_force_service import estimate_crack_time

class PasswordChecker(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=0)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        title_label = ctk.CTkLabel(
            self,
            text="Let the Hive check your password:",
            font=("Arial", 18, "bold"),
            text_color="#5C4033"
        )
        title_label.pack(pady=(5, 10))

        # Password Entry Section
        entry_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        entry_frame.pack(pady=(5, 10))

        self.password_entry = ctk.CTkEntry(
            entry_frame,
            placeholder_text="Enter your password",
            font=("Arial", 14),
            height=40,
            width=300,
            border_width=2,
            border_color="#CCCCCC",
            fg_color="#FFFFFF",
            text_color="#000000"
        )
        self.password_entry.pack(side="left", padx=(0, 0))

        enter_button = ctk.CTkButton(
            entry_frame,
            text="→",
            font=("Arial", 20, "bold"),
            width=50,
            height=40,
            fg_color="#F3AF32",
            text_color="#FFFFFF",
            command=self.process_password
        )
        enter_button.pack(side="left", padx=(5, 0))

        # Options and Console Section
        options_console_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        options_console_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Options Panel
        options_frame = ctk.CTkFrame(
            options_console_frame,
            fg_color="#F3AF32",
            corner_radius=10,
            width=350,
            height=150
        )
        options_frame.pack_propagate(False)
        options_frame.pack(side="left", anchor="n", padx=(0, 10), pady=10)

        self.brute_force_var = ctk.StringVar(value="off")

        brute_force_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Brute Force Attack",
            variable=self.brute_force_var,
            onvalue="on",
            offvalue="off",
            font=("Arial", 14),
            text_color="#5C4033",
            fg_color="#FFFFFF",
            hover_color="#E6920A"
        )
        brute_force_checkbox.pack(anchor="w", padx=10, pady=5)

        skill_label = ctk.CTkLabel(
            options_frame,
            text="Select Hacker Skill Level:",
            font=("Arial", 14),
            text_color="#5C4033"
        )
        skill_label.pack(anchor="w", padx=10, pady=(10, 5))

        self.skill_level_var = ctk.StringVar(value="organization")
        self.skill_level_dropdown = ctk.CTkOptionMenu(
            options_frame,
            variable=self.skill_level_var,
            values=["amateur", "intermediate", "organization"],
            font=("Arial", 14),
            fg_color="#FFFFFF",
            button_color="#E6920A",
            button_hover_color="#D08008"
        )
        self.skill_level_dropdown.pack(anchor="w", padx=10, pady=(0, 10))

        # Console Output
        console_frame = ctk.CTkFrame(
            options_console_frame,
            fg_color="#E0E0E0",
            corner_radius=10,
            width=350,
            height=150
        )
        console_frame.pack_propagate(False)
        console_frame.pack(side="left", anchor="n", padx=(10, 0), pady=10)

        console_label = ctk.CTkLabel(
            console_frame,
            text="Console Output:",
            font=("Arial", 14),
            text_color="#5C4033"
        )
        console_label.pack(anchor="w", padx=10, pady=(10, 5))

        self.console_textbox = ctk.CTkTextbox(
            console_frame,
            height=100,
            fg_color="#F5F5F5",
            text_color="#000000",
            font=("Arial", 12),
            state="disabled"
        )
        self.console_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Password Score and Advice Section
        bottom_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        bottom_frame.pack(fill="x", pady=(20, 0), padx=20)

        # Password Score Section
        self.hivegrade_canvas = Canvas(
            bottom_frame,
            width=120,
            height=120,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.hivegrade_canvas.pack(side="left", anchor="w", padx=10)
        self.hivegrade_circle = self.hivegrade_canvas.create_oval(10, 10, 110, 110, outline="#CCCCCC", width=15)
        self.hivegrade_text = self.hivegrade_canvas.create_text(60, 60, text="N/A", font=("Arial", 16, "bold"), fill="#5C4033")

        # Advice Section
        advice_label = ctk.CTkLabel(
            bottom_frame,
            text=(
                "Advice:\n"
                "1. Use at least 12 characters.\n"
                "2. Include uppercase, lowercase, numbers, and symbols.\n"
                "3. Avoid using common patterns.\n"
                "4. Change passwords regularly."
            ),
            font=("Arial", 14),
            text_color="#5C4033",
            justify="left"
        )
        advice_label.pack(side="left", fill="both", expand=True, padx=(20, 10))

    


    def process_password(self):
        password = self.password_entry.get()
        hacker_skill = self.skill_level_var.get()

        # Estimate crack time using HoneyCrack backend
        result = estimate_crack_time(password, hacker_skill)

        # Update HiveGrade (simple formula: 100 - complexity score)
        complexity_to_score = {
            "simple": 20,
            "moderate": 40,
            "complex": 60,
            "very_complex": 80,
        }
        hivegrade_score = complexity_to_score.get(result["complexity_level"], 100)
        self.hivegrade_canvas.itemconfig(self.hivegrade_text, text=f"{hivegrade_score}%")
        self.hivegrade_canvas.delete(self.hivegrade_circle)
        self.hivegrade_circle = self.hivegrade_canvas.create_arc(
            10, 10, 110, 110,
            start=90,
            extent=-3.6 * hivegrade_score,
            outline="#F3AF32",
            style="arc",
            width=15
        )

        # Display result in the console
        self.console_textbox.configure(state="normal")
        self.console_textbox.delete("1.0", "end")
        self.console_textbox.insert(
            "end",
            (f"Password: {result['password']}\n"
            f"Complexity: {result['complexity_level']}\n"
            f"Estimated Time to Crack:\n"
            f"{result['days']} days, {result['hours']} hours, {result['minutes']} minutes, {result['seconds']} seconds\n")
        )
        self.console_textbox.configure(state="disabled")