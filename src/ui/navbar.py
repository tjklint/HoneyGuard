import customtkinter as ctk
from PIL import Image
from config.settings import NAVBAR_COLOR, TITLE_FONT, LOGO_PATH, TEXT_COLOR

class Navbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=NAVBAR_COLOR, corner_radius=0)  # Remove rounded edges
        self.pack(fill="x")

        # Logo Image
        logo_image = Image.open(LOGO_PATH)
        self.logo_image = ctk.CTkImage(logo_image, size=(40, 40))
        self.logo_label = ctk.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.pack(side="left", padx=10, pady=5)

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="HoneyGuard", font=TITLE_FONT, text_color=TEXT_COLOR)
        self.title_label.pack(side="left", padx=10)
