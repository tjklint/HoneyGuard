import customtkinter as ctk
from tkinter import messagebox
# Import necessary modules

# Define the PasswordChecker class
class PasswordChecker(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=0)
        self.pack(fill="both", expand=True, padx=20, pady=20)

        # Title label
        title_label = ctk.CTkLabel(
            self,
            text="Let the Hive check your password:",
            font=("Arial", 18, "bold"),
            text_color="#5C4033"
        )
        title_label.pack(pady=(5, 10))

        # Password entry section
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

        # Options and console section
        options_console_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        options_console_frame.pack(fill="both", expand=True, padx=20, pady=10)

        frame_width = 350  # Common width for both frames

        # Options panel
        options_frame = ctk.CTkFrame(
            options_console_frame,
            fg_color="#F3AF32",
            corner_radius=10,
            width=frame_width,
            height=150
        )
        options_frame.pack_propagate(False)
        options_frame.pack(side="left", anchor="n", padx=(0, 10), pady=10)

        # Checkboxes for tests
        self.brute_force_var = ctk.StringVar(value="off")
        self.dictionary_var = ctk.StringVar(value="off")

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

        dictionary_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Dictionary Attack",
            variable=self.dictionary_var,
            onvalue="on",
            offvalue="off",
            font=("Arial", 14),
            text_color="#5C4033",
            fg_color="#FFFFFF",
            hover_color="#E6920A"
        )
        dictionary_checkbox.pack(anchor="w", padx=10, pady=5)

        # Dropdown for hacker skill level
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

        # Console output
        console_frame = ctk.CTkFrame(
            options_console_frame,
            fg_color="#E0E0E0",
            corner_radius=10,
            width=frame_width,
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

    def process_password(self):
        password = self.password_entry.get()
        selected_tests = []
        if self.brute_force_var.get() == "on":
            selected_tests.append("Brute Force")
        if self.dictionary_var.get() == "on":
            selected_tests.append("Dictionary")
        hacker_skill = self.skill_level_var.get()

        # Simulate processing and update console
        self.console_textbox.configure(state="normal")
        self.console_textbox.insert("end", f"Checking password: {password}\n")
        self.console_textbox.insert("end", f"Selected tests: {', '.join(selected_tests)}\n")
        self.console_textbox.insert("end", f"Hacker skill level: {hacker_skill}\n")
        self.console_textbox.insert("end", "Processing...\n")
        self.console_textbox.configure(state="disabled")
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
        title_label.pack(pady=(5, 10))  # Reduced padding

        # Password Entry Section
        entry_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        entry_frame.pack(pady=(5, 10))  # Reduced padding

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
        options_console_frame.pack(fill="both", expand=True, padx=20, pady=10)  # Added padding

        # Set common width for both frames
        frame_width = 350

        # Options Panel
        options_frame = ctk.CTkFrame(
            options_console_frame,
            fg_color="#F3AF32",
            corner_radius=10,
            width=frame_width,  # Fixed width
            height=150  # Fixed height
        )
        options_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its content
        options_frame.pack(side="left", anchor="n", padx=(0, 10), pady=10)  # Adjusted padding and anchor

        # Checkboxes for Tests
        self.brute_force_var = ctk.StringVar(value="off")
        self.dictionary_var = ctk.StringVar(value="off")

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
        brute_force_checkbox.pack(anchor="w", padx=10, pady=5)  # Reduced padding

        dictionary_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Dictionary Attack",
            variable=self.dictionary_var,
            onvalue="on",
            offvalue="off",
            font=("Arial", 14),
            text_color="#5C4033",
            fg_color="#FFFFFF",
            hover_color="#E6920A"
        )
        dictionary_checkbox.pack(anchor="w", padx=10, pady=5)  # Reduced padding

        # Dropdown for Hacker Skill Level
        skill_label = ctk.CTkLabel(
            options_frame,
            text="Select Hacker Skill Level:",
            font=("Arial", 14),
            text_color="#5C4033"
        )
        skill_label.pack(anchor="w", padx=10, pady=(10, 5))  # Reduced padding

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
        self.skill_level_dropdown.pack(anchor="w", padx=10, pady=(0, 10))  # Align with checkboxes

        # Console Output
        console_frame = ctk.CTkFrame(
            options_console_frame,
            fg_color="#E0E0E0",
            corner_radius=10,
            width=frame_width,  # Fixed width
            height=150  # Fixed height
        )
        console_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its content
        console_frame.pack(side="left", anchor="n", padx=(10, 0), pady=10)  # Adjusted padding and anchor

        console_label = ctk.CTkLabel(
            console_frame,
            text="Console Output:",
            font=("Arial", 14),
            text_color="#5C4033"
        )
        console_label.pack(anchor="w", padx=10, pady=(10, 5))  # Reduced padding

        self.console_textbox = ctk.CTkTextbox(
            console_frame,
            height=100,
            fg_color="#F5F5F5",
            text_color="#000000",
            font=("Arial", 12),
            state="disabled"
        )
        self.console_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))  # Reduced padding

    def process_password(self):
        password = self.password_entry.get()
        selected_tests = []
        if self.brute_force_var.get() == "on":
            selected_tests.append("Brute Force")
        if self.dictionary_var.get() == "on":
            selected_tests.append("Dictionary")
        hacker_skill = self.skill_level_var.get()

        # Simulate processing and update console
        self.console_textbox.configure(state="normal")
        self.console_textbox.insert("end", f"Checking password: {password}\n")
        self.console_textbox.insert("end", f"Selected tests: {', '.join(selected_tests)}\n")
        self.console_textbox.insert("end", f"Hacker skill level: {hacker_skill}\n")
        self.console_textbox.insert("end", "Processing...\n")
        self.console_textbox.configure(state="disabled")