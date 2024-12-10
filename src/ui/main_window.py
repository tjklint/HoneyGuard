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
        self.root.geometry("960x540")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Add Navbar
        self.navbar = Navbar(self.root)

        # Create the sidebar
        self.sidebar = Sidebar(self.root)  
        self.sidebar.pack(side="left", fill="y")

        self.password_checker = PasswordChecker(self.root, self.sidebar)  
        self.password_checker.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
