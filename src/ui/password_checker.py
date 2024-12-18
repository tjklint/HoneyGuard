import customtkinter as ctk
from tkinter import Canvas
from config.settings import CHARACTER_SETS, HACKER_SPEEDS
from src.services.brute_force_service import estimate_crack_time
from src.services.dictionary_attack_service import check_dictionary

class PasswordChecker(ctk.CTkFrame):
    def __init__(self, parent, sidebar):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=0)
        self.sidebar = sidebar  # Store the reference to the Sidebar
        self.pack(fill="both", expand=True)

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
            height=200  # Increased height to accommodate dropdown
        )
        options_frame.pack_propagate(False)
        options_frame.pack(side="left", anchor="n", padx=(0, 10), pady=10)

        # Hacker Level Dropdown
        hacker_label = ctk.CTkLabel(
            options_frame,
            text="Hacker Skill Level:",
            font=("Arial", 14),
            text_color="#5C4033"
        )
        hacker_label.pack(anchor="w", padx=10, pady=(10, 5))

        self.hacker_skill_var = ctk.StringVar(value="amateur")
        hacker_dropdown = ctk.CTkOptionMenu(
            options_frame,
            values=["amateur", "professional", "organization"],
            variable=self.hacker_skill_var,
            font=("Arial", 14),
            fg_color="#FFFFFF",
            button_color="#E6920A",
            dropdown_hover_color="#F3AF32"
        )
        hacker_dropdown.pack(anchor="w", padx=10, pady=(0, 10))

        # Checkboxes
        self.entropy_var = ctk.StringVar(value="on")
        entropy_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Entropy Check",
            variable=self.entropy_var,
            onvalue="on",
            offvalue="off",
            font=("Arial", 14),
            text_color="#5C4033",
            fg_color="#FFFFFF",
            hover_color="#E6920A"
        )
        entropy_checkbox.pack(anchor="w", padx=10, pady=(5, 0))

        self.brute_force_var = ctk.StringVar(value="on")
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
        brute_force_checkbox.pack(anchor="w", padx=10, pady=(5, 0))

        self.dictionary_attack_var = ctk.StringVar(value="off")
        dictionary_attack_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Dictionary Attack",
            variable=self.dictionary_attack_var,
            onvalue="on",
            offvalue="off",
            font=("Arial", 14),
            text_color="#5C4033",
            fg_color="#FFFFFF",
            hover_color="#E6920A"
        )
        dictionary_attack_checkbox.pack(anchor="w", padx=10, pady=(5, 0))

        # Console Output Section
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
        score_advice_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        score_advice_frame.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        # Password Score Section
        self.hivegrade_canvas = Canvas(
            score_advice_frame,
            width=150,
            height=150,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.hivegrade_canvas.pack(side="left", anchor="n", padx=20, pady=(0, 10))

        self.hivegrade_circle = self.hivegrade_canvas.create_oval(
            10, 10, 140, 140, outline="#CCCCCC", width=15
        )
        self.hivegrade_text = self.hivegrade_canvas.create_text(
            75, 75, text="N/A", font=("Arial", 20, "bold"), fill="#5C4033"
        )

        # Advice Section
        advice_frame = ctk.CTkFrame(score_advice_frame, fg_color="#FFFFFF", corner_radius=0)
        advice_frame.pack(side="left", fill="both", expand=True, padx=20, pady=(0, 10))

        advice_label = ctk.CTkLabel(
            advice_frame,
            text="Password Advice:",
            font=("Arial", 16, "bold"),
            text_color="#5C4033"
        )
        advice_label.pack(anchor="nw", pady=(0, 10))

        self.advice_dynamic_label = ctk.CTkLabel(
            advice_frame,
            text="",  # Dynamic advice updates here
            font=("Arial", 14),
            text_color="#5C4033",
            justify="left"
        )
        self.advice_dynamic_label.pack(anchor="nw")

    def process_password(self):
        password = self.password_entry.get()
        hacker_skill = self.hacker_skill_var.get()
        entropy_enabled = self.entropy_var.get() == "on"
        brute_force_enabled = self.brute_force_var.get() == "on"
        dictionary_attack_enabled = self.dictionary_attack_var.get() == "on"

        results = []
        advice = []

        # Entropy Check
        entropy_score = 0  # Default entropy score
        if entropy_enabled:
            char_types = {
                "uppercase": any(char.isupper() for char in password),
                "lowercase": any(char.islower() for char in password),
                "numbers": any(char.isdigit() for char in password),
                "symbols": any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password),
            }
            char_variety = sum(char_types.values())
            entropy = len(password) * char_variety
            entropy_score = min(int((entropy / 100) * 100), 100)
            results.append(f"Entropy Score: {entropy_score}%")

            # Generate advice
            if len(password) < 12:
                advice.append("Use at least 12 characters.")
            if not char_types["uppercase"]:
                advice.append("Include uppercase letters.")
            if not char_types["lowercase"]:
                advice.append("Include lowercase letters.")
            if not char_types["numbers"]:
                advice.append("Add numbers for better security.")
            if not char_types["symbols"]:
                advice.append("Include symbols for added complexity.")
            if "123" in password or password.lower() in ["password", "admin"]:
                advice.append("Avoid common patterns like '123' or dictionary words.")

        # Brute Force Check
        if brute_force_enabled:
            brute_force_result = estimate_crack_time(password, hacker_skill)
            results.append(
                f"Brute Force Crack Time: {brute_force_result['days']}d "
                f"{brute_force_result['hours']}h {brute_force_result['minutes']}m"
            )

        # Dictionary Attack
        if dictionary_attack_enabled:
            dictionary_result = check_dictionary(password)
            results.append(f"Dictionary Attack: {dictionary_result}")

        # Update HiveGrade in the Sidebar
        self.sidebar.update_hivegrade(
            entropy_score=entropy_score,
            dictionary_score=100,  # Use dictionary_score if relevant
            api_score=0  # Placeholder for API score
        )

        # Update the HiveGrade circle
        self.update_hivegrade(entropy_score)

        # Update advice label
        advice_text = "\n".join([f"{i + 1}. {line}" for i, line in enumerate(advice)])
        self.advice_dynamic_label.configure(text=advice_text)

        # Display results in console
        self.console_textbox.configure(state="normal")
        self.console_textbox.delete("1.0", "end")
        self.console_textbox.insert("end", "\n".join(results))
        self.console_textbox.configure(state="disabled")

    def update_hivegrade(self, entropy_score):
        self.hivegrade_canvas.delete("all")
        self.hivegrade_circle = self.hivegrade_canvas.create_oval(
            10, 10, 110, 110, outline="#CCCCCC", width=15
        )
        self.hivegrade_canvas.create_arc(
            10, 10, 110, 110, start=90, extent=-3.6 * entropy_score,
            outline="#F3AF32", style="arc", width=15
        )
        self.hivegrade_canvas.create_text(
            60, 60, text=f"{entropy_score}%", font=("Arial", 20, "bold"), fill="#5C4033"
        )
