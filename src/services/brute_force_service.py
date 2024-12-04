from config.settings import CHARACTER_SETS, HACKER_SPEEDS


def estimate_crack_time(password: str, hacker_skill: str) -> dict:
    """
    Estimate the time required to crack a password using brute force
    based on the hacker's skill level and password complexity.
    
    :param password: The password to analyze
    :param hacker_skill: Hacker skill level (e.g., "amateur", "organization")
    :return: Dictionary containing the estimated time in readable format
    """
    # Determine password complexity level based on characters used
    if all(c in CHARACTER_SETS["simple"] for c in password):
        complexity_level = "simple"
    elif all(c in CHARACTER_SETS["moderate"] for c in password):
        complexity_level = "moderate"
    elif all(c in CHARACTER_SETS["complex"] for c in password):
        complexity_level = "complex"
    else:
        complexity_level = "very_complex"
    
    # Calculate total possible combinations
    charset_size = len(CHARACTER_SETS[complexity_level])
    combinations = charset_size ** len(password)
    
    # Get guesses per second based on hacker skill
    guesses_per_second = HACKER_SPEEDS.get(hacker_skill, 1_000)
    
    # Calculate time to crack in seconds
    time_to_crack_seconds = combinations / guesses_per_second
    
    # Convert to readable time format
    days = time_to_crack_seconds // (24 * 3600)
    time_to_crack_seconds %= (24 * 3600)
    hours = time_to_crack_seconds // 3600
    time_to_crack_seconds %= 3600
    minutes = time_to_crack_seconds // 60
    seconds = time_to_crack_seconds % 60
    
    return {
        "password": password,
        "complexity_level": complexity_level,
        "days": int(days),
        "hours": int(hours),
        "minutes": int(minutes),
        "seconds": int(seconds),
    }
