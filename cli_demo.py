#!/usr/bin/env python3
"""
Numerology Calculator - Command Line Demo

A simple command-line demonstration of the numerology calculator functionality.
"""

from numerology import (
    calculate_numerology_value,
    get_numerology_meaning,
    validate_name_input
)


def main():
    """Main function for the command line demo."""
    print("🔢 Numerology Calculator - Command Line Demo")
    print("=" * 50)
    print("Enter names to calculate their numerology values.")
    print("Type 'quit' or 'exit' to stop.\n")
    
    while True:
        try:
            # Get user input
            name = input("Enter a name: ").strip()
            
            # Check for exit commands
            if name.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using the Numerology Calculator! 👋")
                break
            
            # Validate input
            is_valid, error_message = validate_name_input(name)
            if not is_valid:
                print(f"❌ Error: {error_message}\n")
                continue
            
            # Calculate numerology value
            numerology_value = calculate_numerology_value(name)
            meaning = get_numerology_meaning(numerology_value)
            
            # Display results
            print(f"\n📊 Results for '{name}':")
            print(f"   Numerology Value: {numerology_value}")
            print(f"   Meaning: {meaning}")
            
            # Show calculation breakdown
            show_calculation_breakdown(name)
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}\n")


def show_calculation_breakdown(name: str):
    """Show the step-by-step calculation breakdown."""
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
    
    breakdown = []
    total = 0
    
    for char in name.upper():
        if char in letter_values:
            value = letter_values[char]
            breakdown.append(f"{char}={value}")
            total += value
    
    if breakdown:
        print(f"   Calculation: {' + '.join(breakdown)} = {total}")


if __name__ == "__main__":
    main()
