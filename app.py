"""
Numerology Calculator Streamlit App

A simple web application for calculating numerology values of names
using the Pythagorean numerology system.
"""

import streamlit as st
import json
import os
from datetime import datetime
from numerology import (
    calculate_numerology_value, 
    get_numerology_meaning, 
    validate_name_input
)

# Constants
HISTORY_FILE = "calculation_history.json"

def setup_page():
    """Set up the page configuration and display header."""
    st.set_page_config(
        page_title="Numerology Calculator",
        page_icon="🔢",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state variables
    if "history_filter" not in st.session_state:
        st.session_state["history_filter"] = []
    
    # Initialize name variables
    if "first_name" not in st.session_state:
        st.session_state["first_name"] = ""
    if "last_name" not in st.session_state:
        st.session_state["last_name"] = ""
    
    st.title("🔢 Numerology Calculator")
    st.markdown("---")
    st.markdown(
        """
        Discover the numerological value of any name using the **Pythagorean Numerology System**.
        
        Simply enter a name below and get its numerological meaning! 
        *(Spaces and other whitespace characters are automatically ignored)*
        """
    )


def display_results(name: str, numerology_value: int, meaning: str):
    """Display the calculation results."""
    st.success("✅ Calculation Complete!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric(
            label="Numerology Value",
            value=numerology_value
        )
    
    with col2:
        st.info(f"**Meaning:** {meaning}")
    
    st.markdown("---")
    with st.expander("🔍 How is this calculated?"):
        st.markdown(
            """
            The **Pythagorean Numerology System** assigns each letter a number:
            
            - **A, J, S** = 1
            - **B, K, T** = 2  
            - **C, L, U** = 3
            - **D, M, V** = 4
            - **E, N, W** = 5
            - **F, O, X** = 6
            - **G, P, Y** = 7
            - **H, Q, Z** = 8
            - **I, R** = 9
            
            The letters in your name are converted to numbers, summed up, 
            and then reduced to a single digit (1-9) or master number (11, 22, 33).
            
            **Note:** Whitespace characters (spaces, tabs) are automatically ignored during calculation.
            """
        )


def process_calculation(full_name: str):
    """Process the numerology calculation for the full name."""
    is_valid, error_message = validate_name_input(full_name)
    
    if not is_valid:
        st.error(f"❌ {error_message}")
        return
    
    try:
        # Calculate based on the combined name
        numerology_value = calculate_numerology_value(full_name)
        meaning = get_numerology_meaning(numerology_value)
        
        # Display the calculation results
        display_results(full_name, numerology_value, meaning)
        
        # Show calculation steps and get the details
        st.markdown("**Step-by-step Calculation:**")
        calculation_details = show_calculation_steps(full_name, numerology_value)
        
        # Save to history (only if name is unique)
        was_saved = save_to_history(full_name, numerology_value, meaning, calculation_details)
        if was_saved:
            st.success("✅ Calculation saved to history!")
    except ValueError as e:
        st.error(f"❌ Error: {str(e)}")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")


def main():
    """Main function to run the Streamlit app."""
    setup_page()
    
    # Display success message if history was just cleared
    if 'history_cleared' in st.session_state and st.session_state['history_cleared']:
        st.success("✅ History has been cleared successfully!")
        st.session_state['history_cleared'] = False
    
    # Input section
    st.subheader("Enter a Name")
    
    # Create two columns for first and last name inputs
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input(
            label="First Name",
            placeholder="Enter first name (e.g., John)...",
            help="Enter the first name to calculate its numerology value."
        )
    
    with col2:
        last_name = st.text_input(
            label="Last Name",
            placeholder="Enter last name (e.g., Doe)...",
            help="Enter the last name to calculate its numerology value."
        )
    
    # Concatenate names for calculation and display
    full_name = f"{first_name} {last_name}".strip()
    
    # Store the name parts in session state for later use
    if 'first_name' not in st.session_state:
        st.session_state['first_name'] = ''
    if 'last_name' not in st.session_state:
        st.session_state['last_name'] = ''
        
    st.session_state['first_name'] = first_name
    st.session_state['last_name'] = last_name
    
    if st.button("Calculate Numerology Value", type="primary", key="calculate_button"):
        if not full_name:
            st.warning("⚠️ Please enter at least one name field to calculate the numerology value.")
            return
            
        # Check if name is a duplicate
        if handle_duplicate_name(full_name):
            # Name exists and was handled (either viewed or ignored)
            return
        else:
            # Process the calculation for new name
            process_calculation(full_name)
    
    st.markdown("---")
    
    # History section
    display_history()
    
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; font-size: 0.8em;'>
            Built with ❤️ using Streamlit | Pythagorean Numerology System
        </div>
        """,
        unsafe_allow_html=True
    )


def show_calculation_steps(name: str, final_value: int):
    """
    Display the step-by-step calculation process and return the calculation details.
    
    Args:
        name (str): The input name
        final_value (int): The final numerology value
        
    Returns:
        dict: Dictionary containing the calculation details
    """
    letter_values = get_letter_values()
    
    st.markdown("**Calculation Steps:**")
    
    breakdown, total, ignored_chars = process_name_for_display(name, letter_values)
    
    calculation_details = {
        "breakdown": breakdown,
        "total": total,
        "ignored_chars": ignored_chars,
        "final_value": final_value
    }
    
    if breakdown:
        display_calculation_breakdown(breakdown, total, ignored_chars, final_value)
        
    return calculation_details


def get_letter_values() -> dict:
    """Get the Pythagorean letter to number mapping."""
    return {
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
    # Note: This maps the letters exactly as defined in numerology.py

def process_name_for_display(name: str, letter_values: dict) -> tuple:
    """Process name and return breakdown components."""
    breakdown = []
    total = 0
    ignored_chars = []
    
    for char in name.upper():
        if char in letter_values:
            value = letter_values[char]
            breakdown.append(f"{char} = {value}")
            total += value
        elif char.isspace():
            ignored_chars.append(char)
        elif char.isalpha():
            breakdown.append(f"{char} = ?")
    
    return breakdown, total, ignored_chars


def display_calculation_breakdown(breakdown: list, total: int, ignored_chars: list, final_value: int):
    """Display the calculation breakdown with ignored characters info."""
    st.code(" + ".join(breakdown) + f" = {total}")
    
    if ignored_chars:
        space_count = len([c for c in ignored_chars if c == ' '])
        other_count = len(ignored_chars) - space_count
        ignored_msg = []
        if space_count > 0:
            ignored_msg.append(f"{space_count} space(s)")
        if other_count > 0:
            ignored_msg.append(f"{other_count} other whitespace character(s)")
        st.caption(f"Ignored: {', '.join(ignored_msg)}")
    
    if total != final_value:
        st.write(f"Reduced: {total} → {final_value}")


def save_to_history(name: str, numerology_value: int, meaning: str, calculation_details: dict = None):
    """
    Save the calculation to history JSON file.
    
    Args:
        name (str): The full name that was calculated
        numerology_value (int): The calculated numerology value
        meaning (str): The meaning of the value
        calculation_details (dict, optional): Details of how the calculation was performed
        
    Returns:
        bool: True if entry was saved, False if name already exists
    """
    # Check if name already exists in history
    if is_name_in_history(name):
        st.warning(f"⚠️ '{name}' is already in your calculation history. Duplicate entry not saved.")
        return False
    
    # Load existing history or create new if not exists
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    else:
        history = []
        
    # Get first and last name components
    # First try from session state, then fall back to parsing the full name
    first_name = st.session_state.get('first_name', '')
    last_name = st.session_state.get('last_name', '')
    
    # If we don't have first/last name from session state, parse them from the full name
    if not first_name and not last_name and name:
        first_name, last_name = parse_name_components(name)
    
    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create new entry
    new_entry = {
        "timestamp": timestamp,
        "name": name,
        "first_name": first_name,
        "last_name": last_name,
        "numerology_value": numerology_value,
        "meaning": meaning
    }
    
    # Add calculation details if provided
    if calculation_details:
        # Convert the breakdown list to a string for better storage
        calculation_summary = {
            "breakdown": " + ".join(calculation_details["breakdown"]) if calculation_details.get("breakdown") else "",
            "total": calculation_details.get("total", 0),
            "final_value": calculation_details.get("final_value", 0),
            "ignored_chars_count": len(calculation_details.get("ignored_chars", []))
        }
        new_entry["calculation"] = calculation_summary
    
    # Add new entry
    history.append(new_entry)
    
    # Save back to file
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
    
    return True


def load_history():
    """
    Load calculation history from JSON file.
    
    Returns:
        list: List of calculation history entries
    """
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []


def display_history_entry(entry):
    """
    Display a single history entry as a card.
    Compatible with both new format (first_name/last_name) and old format entries.
    """
    # Create a local copy to avoid modifying the original entry
    display_entry = entry.copy()
    
    # For backward compatibility: parse first and last names if not present
    if "first_name" not in display_entry or "last_name" not in display_entry:
        if "name" in display_entry:
            first, last = parse_name_components(display_entry["name"])
            display_entry["first_name"] = first
            display_entry["last_name"] = last
    
    with st.container():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"**Date:** {display_entry['timestamp']}")
            
            # Display names based on what's available
            first = display_entry.get("first_name", "").strip()
            last = display_entry.get("last_name", "").strip()
            
            if first and last:
                st.markdown(f"**First Name:** {first}")
                st.markdown(f"**Last Name:** {last}")
            elif first:
                st.markdown(f"**First Name:** {first}")
            elif last:
                st.markdown(f"**Last Name:** {last}")
            else:
                st.markdown(f"**Name:** {display_entry['name']}")
                
            st.markdown(f"**Value:** {display_entry['numerology_value']}")
        
        with col2:
            st.markdown(f"**Meaning:** {display_entry['meaning']}")
            
            # Display calculation details if available
            if "calculation" in display_entry:
                display_calculation_history(display_entry["calculation"])
        
        st.markdown("---")


def display_calculation_history(calc):
    """Display calculation details from history."""
    with st.expander("Show calculation"):
        if calc.get("breakdown"):
            st.code(f"{calc['breakdown']} = {calc['total']}")
        
        if calc["total"] != calc["final_value"]:
            st.write(f"Reduced: {calc['total']} → {calc['final_value']}")
            
        if calc.get("ignored_chars_count", 0) > 0:
            st.caption(f"Ignored: {calc['ignored_chars_count']} whitespace character(s)")


def display_history():
    """Display the calculation history in the app."""
    history = load_history()
    
    if not history:
        st.info("No calculation history yet.")
        return
    
    st.subheader("Calculation History")
    
    # Create an expander for history
    with st.expander("View Previous Calculations"):
        # Show newest entries first
        history.reverse()
        
        # Get all available numerology values for filtering (sorted list of unique values)
        numerology_values = sorted(list({entry["numerology_value"] for entry in history}))
        
        # Add filter controls
        st.write("**Filter by Numerology Value:**")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            selected_values = st.multiselect(
                label="Select values to display:",
                options=numerology_values,
                default=[],
                key="history_filter"
            )
        
        with col2:
            if st.button("Clear Filter", key="clear_filter_button"):
                # Reset the filter
                st.session_state["history_filter"] = []
                selected_values = []
        
        # Apply filter if selections were made
        filtered_history = history
        if selected_values:
            filtered_history = [entry for entry in history if entry["numerology_value"] in selected_values]
            st.write(f"Showing {len(filtered_history)} of {len(history)} entries")
        
        # Display message if no entries match the filter
        if selected_values and not filtered_history:
            st.info("No entries match your filter criteria.")
            
        # Display each history entry
        for entry in filtered_history:
            display_history_entry(entry)
        
        st.markdown("---")
        
        # Option to clear history
        col1, _ = st.columns([1, 4])
        with col1:
            if st.button("Clear History", key="clear_history_button"):
                if os.path.exists(HISTORY_FILE):
                    os.remove(HISTORY_FILE)
                    st.session_state['history_cleared'] = True
                    st.rerun()


def is_name_in_history(name: str) -> bool:
    """
    Check if a name already exists in the calculation history.
    
    Args:
        name (str): The name to check
        
    Returns:
        bool: True if name exists in history, False otherwise
    """
    history = load_history()
    name = name.lower().strip()
    
    # Case-insensitive search
    for entry in history:
        # Check against full name
        if entry["name"].lower().strip() == name:
            return True
            
        # Check against combined first and last name if they exist separately
        if "first_name" in entry and "last_name" in entry:
            combined = f"{entry.get('first_name', '')} {entry.get('last_name', '')}".lower().strip()
            if combined == name:
                return True
    
    return False


def get_display_name(entry):
    """
    Helper function to get the appropriate display name from an entry.
    Works with both new format (first_name/last_name) and old format entries.
    """
    # For entries with separated first and last name fields
    if "first_name" in entry and "last_name" in entry:
        first = entry.get("first_name", "").strip()
        last = entry.get("last_name", "").strip()
        
        if first and last:
            return f"{first} {last}"
        elif first:
            return first
        elif last:
            return last
            
    # For entries with only the full name
    if "name" in entry and entry["name"]:
        return entry["name"].strip()
        
    # Fallback
    return "Unknown"

def display_existing_calculation(entry):
    """
    Display an existing calculation entry.
    Compatible with both new format (first_name/last_name) and old format entries.
    """
    # Create a local copy to avoid modifying the original entry
    display_entry = entry.copy()
    
    # For backward compatibility: parse first and last names if not present
    if "first_name" not in display_entry or "last_name" not in display_entry:
        if "name" in display_entry:
            first, last = parse_name_components(display_entry["name"])
            display_entry["first_name"] = first
            display_entry["last_name"] = last
    
    display_name = get_display_name(display_entry)
    st.subheader(f"Existing calculation for '{display_name}'")
    
    # Display the first and last name separately if both exist
    if display_entry.get("first_name") and display_entry.get("last_name"):
        st.markdown(f"**First Name:** {display_entry['first_name']}")
        st.markdown(f"**Last Name:** {display_entry['last_name']}")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Numerology Value", display_entry["numerology_value"])
    with col2:
        st.info(f"**Meaning:** {display_entry['meaning']}")
    
    # Show calculation details if available
    if "calculation" in display_entry:
        st.markdown("**Calculation Details:**")
        display_calculation_history(display_entry["calculation"])

def handle_duplicate_name(name: str) -> bool:
    """
    Handle the case when a name already exists in history.
    
    Args:
        name (str): The name to check
        
    Returns:
        bool: True if the name exists and was handled, False otherwise
    """
    if not is_name_in_history(name):
        return False
    
    name = name.strip()
    st.warning(f"⚠️ '{name}' is already in your calculation history.")
    
    # Ask the user if they want to view the existing calculation
    if st.button("View Existing Calculation", key="view_existing"):
        # Find and display the existing entry
        history = load_history()
        name_lower = name.lower()
        
        for entry in history:
            # Check if the entry matches by full name (case-insensitive)
            if entry["name"].lower() == name_lower:
                display_existing_calculation(entry)
                break
            
            # Check if the entry matches by combined first name and last name
            if "first_name" in entry and "last_name" in entry:
                combined = f"{entry.get('first_name', '')} {entry.get('last_name', '')}".strip().lower()
                if combined == name_lower:
                    display_existing_calculation(entry)
                    break
    
    return True


def parse_name_components(full_name: str) -> tuple:
    """
    Parse a full name into first name and last name components.
    
    Args:
        full_name (str): The full name string
        
    Returns:
        tuple: (first_name, last_name)
    """
    parts = full_name.strip().split(' ', 1)
    
    if len(parts) == 1:
        # Only one name provided
        return parts[0], ""
    else:
        # First name and last name(s)
        return parts[0], parts[1]


if __name__ == "__main__":
    main()
