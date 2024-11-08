import customtkinter as ctk
from config.settings import HONEY_BG_COLOR, TITLE_COLOR
from .email_checker import EmailChecker
from .password_checker import PasswordChecker

class HoneyGuard:
    def __init__(self):
        ctk.set_appearance_mode("light")  

        self.root = ctk.CTk()  # Use CustomTkinter's CTk for modern look
        self.root.title("HoneyGuard")
        self.root.geometry("500x400")
        self.root.configure(bg=HONEY_BG_COLOR)  

        title_label = ctk.CTkLabel(self.root, text="🐝 HoneyGuard 🐝", font=("Helvetica", 24, "bold"), text_color=TITLE_COLOR)
        title_label.pack(pady=20)

        # Create and pack the Email and Password Checker frames
        self.email_checker = EmailChecker(self.root)
        self.password_checker = PasswordChecker(self.root)

    def run(self):
        self.root.mainloop()
