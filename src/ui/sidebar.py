import customtkinter as ctk
from PIL import Image, ImageTk, ImageEnhance
from tkinter import Canvas
from config.settings import HIVEGRADE_BG_COLOR, HIVEGRADE_FILL_COLOR, TEXT_COLOR

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#F0F0F0", corner_radius=0)  
        self.pack(side="left", fill="y")

        # Navigation Buttons
        self.create_nav_button("Home", "assets/icons/Home.png")
        self.create_nav_button("HoneyCrack", "assets/icons/HoneyCrack.png")
        self.create_nav_button("HiveBreach", "assets/icons/HiveBreach.png")

        # Spacer
        ctk.CTkLabel(self, text="")  

        # HiveGrade Circle
        self.hivegrade_label = ctk.CTkLabel(self, text="HiveGrade:", font=("Arial", 16, "bold"), text_color=TEXT_COLOR)
        self.hivegrade_label.pack(pady=(20, 5))
        self.hivegrade_canvas = Canvas(self, width=120, height=120, bg="#F0F0F0", highlightthickness=0)
        self.hivegrade_canvas.pack()

        # Initial HiveGrade settings
        self.hivegrade_percentage = 0
        self.hivegrade_text = self.hivegrade_canvas.create_text(60, 60, text="N/A", font=("Arial", 18, "bold"), fill=TEXT_COLOR)
        self.draw_hivegrade_circle()

    def create_nav_button(self, text, icon_path):
        # Load and recolor PNG image to yellow
        icon_image = Image.open(icon_path).resize((30, 30))
        icon_image = self.recolor_image(icon_image, "#E6920A") 
        icon_image_tk = ImageTk.PhotoImage(icon_image)

        # Create button with icon
        button = ctk.CTkButton(self, text=text, image=icon_image_tk, compound="left", font=("Arial", 14),
                               text_color=TEXT_COLOR, fg_color="transparent", hover_color="#E6920A", anchor="w")
        button.image = icon_image_tk  # Keep a reference to avoid garbage collection
        button.pack(fill="x", padx=10, pady=5)

    def recolor_image(self, image, color):
        # Convert the image to grayscale
        grayscale_image = image.convert("L")
        # Convert grayscale image to RGB and apply color
        colored_image = ImageEnhance.Color(grayscale_image).enhance(0).convert("RGBA")
        for x in range(colored_image.width):
            for y in range(colored_image.height):
                pixel = colored_image.getpixel((x, y))
                if pixel[3] > 0:  # Only change non-transparent pixels
                    colored_image.putpixel((x, y), tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) + (pixel[3],))
        return colored_image

    def draw_hivegrade_circle(self):
        # Draw the background circle
        self.hivegrade_canvas.create_oval(10, 10, 110, 110, outline=HIVEGRADE_BG_COLOR, width=15)
        # Draw the progress/fill circle based on the current percentage
        if self.hivegrade_percentage > 0:
            self.hivegrade_canvas.create_arc(10, 10, 110, 110, start=90, extent=-3.6 * self.hivegrade_percentage,
                                             outline=HIVEGRADE_FILL_COLOR, style="arc", width=15)

    def update_hivegrade(self, percentage):
        # Update the HiveGrade percentage and redraw
        self.hivegrade_percentage = percentage
        self.hivegrade_canvas.delete("all")  
        self.draw_hivegrade_circle()
        self.hivegrade_canvas.itemconfig(self.hivegrade_text, text=f"{self.hivegrade_percentage}%")
