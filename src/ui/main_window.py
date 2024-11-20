import customtkinter as ctk
from config.settings import BACKGROUND_COLOR
from .navbar import Navbar
from .sidebar import Sidebar
from .password_checker import PasswordChecker

class HoneyGuard:
    def __init__(self):
        ctk.set_appearance_mode("light")
        self.root = ctk.CTk()
        self.root.title("HoneyGuard")
        self.root.geometry("800x600")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Add Navbar
        self.navbar = Navbar(self.root)

        # Add Sidebar
        self.sidebar = Sidebar(self.root)

        # Main Content Frame
        self.content_frame = ctk.CTkFrame(self.root, fg_color=BACKGROUND_COLOR)
        self.content_frame.pack(fill="both", expand=True, side="right")

        self.password_checker = PasswordChecker(self.content_frame)

    def run(self):
        self.root.mainloop()
