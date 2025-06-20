# Requirements for Numerology Calculator App

## Overview
Develop a simple Python application using Streamlit that calculates the numerology value of any given name.

## Functional Requirements
- The app must provide a text input for users to enter a name.
- On submission, the app should calculate the numerology value based on the entered name.
- Display the calculated numerology value clearly to the user.
- Support both uppercase and lowercase letters.
- Ignore whitespace characters (spaces, tabs) in the name input during calculation.
- Handle invalid or empty input gracefully with appropriate error messages.

## Technical Requirements
- Use Python 3.7 or higher.
- Use Streamlit for the user interface.
- Implement a standard numerology calculation method (e.g., Pythagorean system).
- The app should be runnable locally with a single command (e.g., `streamlit run app.py`).

## Non-Functional Requirements
- The UI should be simple and user-friendly.
- The code should be well-documented and modular.
- All dependencies must be listed in a `requirements.txt` file.

``` python
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
```