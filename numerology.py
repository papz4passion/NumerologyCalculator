"""
Numerology Calculator Module

This module implements the Pythagorean numerology system for calculating
the numerological value of names.
"""

def calculate_numerology_value(name: str) -> int:
    """
    Calculate the numerology value of a name using the Pythagorean system.
    
    In the Pythagorean system, each letter is assigned a number:
    A, J, S = 1    B, K, T = 2    C, L, U = 3
    D, M, V = 4    E, N, W = 5    F, O, X = 6
    G, P, Y = 7    H, Q, Z = 8    I, R = 9
    
    Args:
        name (str): The name to calculate numerology value for
        
    Returns:
        int: The final numerology value (reduced to a single digit 1-9, or master numbers 11, 22, 33)
        
    Raises:
        ValueError: If the name is empty or contains no valid letters
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    
    # Pythagorean numerology letter-to-number mapping
    letter_values = {
        'A': 1, 'J': 1, 'S': 3,
        'B': 2, 'K': 2, 'T': 4,
        'C': 3, 'L': 3, 'U': 6,
        'D': 4, 'M': 4, 'V': 6,
        'E': 5, 'N': 5, 'W': 6,
        'F': 8, 'O': 7, 'X': 5,
        'G': 3, 'P': 8, 'Y': 1,
        'H': 5, 'Q': 1, 'Z': 7,
        'I': 1, 'R': 2
    }
    
    # Convert to uppercase and calculate sum
    total = 0
    valid_chars = 0
    
    for char in name.upper():
        if char in letter_values:
            total += letter_values[char]
            valid_chars += 1
    
    if valid_chars == 0:
        raise ValueError("Name must contain at least one valid letter")
    
    # Reduce to single digit or master number
    return reduce_to_final_number(total)


def reduce_to_final_number(number: int) -> int:
    """
    Reduce a number to a single digit (1-9) or master number (11, 22, 33).
    
    Args:
        number (int): The number to reduce
        
    Returns:
        int: The reduced number
    """
    while number > 9:
        # Check for master numbers before reducing
        if number in [11, 22, 33]:
            return number
        
        # Sum the digits
        digit_sum = 0
        temp = number
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        
        number = digit_sum
    
    return number


def get_numerology_meaning(number: int) -> str:
    """
    Get the meaning of a numerology number.
    
    Args:
        number (int): The numerology number
        
    Returns:
        str: The meaning of the number
    """
    meanings = {
        1: "Leadership, independence, pioneering spirit",
        2: "Cooperation, balance, diplomacy",
        3: "Creativity, communication, optimism",
        4: "Stability, hard work, practicality",
        5: "Freedom, adventure, versatility",
        6: "Nurturing, responsibility, compassion",
        7: "Spirituality, introspection, analysis",
        8: "Material success, ambition, authority",
        9: "Humanitarian, generous, completion",
        11: "Intuition, inspiration, enlightenment (Master Number)",
        22: "Master builder, practical idealism (Master Number)",
        33: "Master teacher, compassion, healing (Master Number)"
    }
    
    return meanings.get(number, "Unknown number")


def validate_name_input(name: str) -> tuple[bool, str]:
    """
    Validate the name input.
    
    Args:
        name (str): The name to validate
        
    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Please enter a name"
    
    # Check if name contains at least one letter
    has_letter = any(char.isalpha() for char in name)
    if not has_letter:
        return False, "Name must contain at least one letter"
    
    return True, ""
