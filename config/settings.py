import os

# Colors
NAVBAR_COLOR = "#C89425"
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#000000"

SIDEBAR_BG_COLOR = "#C89425"  # Background color of the sidebar
ICON_COLOR = "#E6920A"  # Icon color
HIVEGRADE_BG_COLOR = "#F3AF32"  # Background of the HiveGrade circle
HIVEGRADE_FILL_COLOR = "#E6920A"  # Fill color of the HiveGrade
TEXT_COLOR = "#5C4033"  # Text color for labels

# Fonts
TITLE_FONT = ("Koulen", 18, "bold")
NORMAL_FONT = ("Arial", 12)

# Paths
LOGO_PATH = os.path.join(os.path.dirname(__file__), "../assets/icons/icon.png")

# Brute Force Constants
CHARACTER_SETS = {
    "simple": "abcdefghijklmnopqrstuvwxyz",
    "moderate": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "complex": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    "very_complex": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",.<>?/`~"
}

HACKER_SPEEDS = {
    "amateur": 1_000,            # 1,000 guesses per second
    "intermediate": 100_000,      # 100,000 guesses per second
    "organization": 10_000_000    # 10 million guesses per second
}

# Legacy Styling Constants (keeping these here during development for reference)
HONEY_BG_COLOR = "#FFF3B0"
FRAME_BG_COLOR = "#FFD966"
BUTTON_COLOR = "#FFC107"
TEXT_COLOR = "#5C4033"
TITLE_COLOR = "#F5A623"