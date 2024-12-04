import re

def check_dictionary(password):
    # Load common passwords
    with open("./data/passwords/common.txt", "r") as common_file, open("./data/passwords/500worst.txt", "r") as worst_file:
        common_passwords = set(common_file.read().splitlines())
        worst_passwords = set(worst_file.read().splitlines())

    # Exact match
    if password in worst_passwords:
        return "In 500 Worst Passwords"
    elif password in common_passwords:
        return "In Common Passwords"

    # Transformations
    base_password = remove_common_patterns(password)
    if base_password in worst_passwords or base_password in common_passwords:
        return f"Matches base pattern of '{base_password}'"

    # Fuzzy matching
    for word in worst_passwords.union(common_passwords):
        if is_fuzzy_match(password, word):
            return f"Similar to '{word}' in dictionary"

    return "Not Found in Dictionary"

def remove_common_patterns(password):
    # Remove common suffixes like numbers or symbols
    return re.sub(r"[\d!@#$%^&*()_+={}\[\]:;'\"<>,.?/~`-]+$", "", password)

def is_fuzzy_match(password, word):
    # Check for case-insensitive match or leet substitutions
    password = password.lower()
    word = word.lower()

    # Replace common leet speak substitutions
    leet_subs = {
        "4": "a", "@": "a", "$": "s", "5": "s", "0": "o", "1": "l", "!": "i", "3": "e"
    }
    for leet, char in leet_subs.items():
        password = password.replace(leet, char)

    # Check if transformed password matches the word
    return password == word