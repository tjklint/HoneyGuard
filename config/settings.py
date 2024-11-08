
# Styling Constants
HONEY_BG_COLOR = "#FFF3B0"
FRAME_BG_COLOR = "#FFD966"
BUTTON_COLOR = "#FFC107"
TEXT_COLOR = "#5C4033"
TITLE_COLOR = "#F5A623"

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