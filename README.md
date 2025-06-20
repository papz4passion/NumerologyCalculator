# Nu## Features

- 🔢 **Pythagorean Numerology System**: Uses the traditional letter-to-number mapping
- 📝 **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- ✅ **Input Validation**: Handles empty inputs and invalid characters gracefully
- 🎯 **Master Numbers**: Correctly identifies and handles master numbers (11, 22, 33)
- 🚀 **Whitespace Handling**: Automatically ignores spaces, tabs, and other whitespace in names
- 📊 **Step-by-Step Calculation**: Shows how the numerology value is calculated
- 💡 **Meanings**: Provides interpretations for each numerology number
- 📜 **Calculation History**: Saves all calculations to a JSON file and displays history in the appCalculator

A simple and elegant Python web application built with Streamlit that calculates the numerological value of names using the Pythagorean numerology system.

## Features

- 🔢 **Pythagorean Numerology System**: Uses the traditional letter-to-number mapping
- 📝 **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- ✅ **Input Validation**: Handles empty inputs and invalid characters gracefully
- 🎯 **Master Numbers**: Correctly identifies and handles master numbers (11, 22, 33)
- � **Whitespace Handling**: Automatically ignores spaces, tabs, and other whitespace in names
- �📊 **Step-by-Step Calculation**: Shows how the numerology value is calculated
- 💡 **Meanings**: Provides interpretations for each numerology number

## Installation

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

To start the Streamlit web application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Running Tests

To run the test suite:

```bash
python test_numerology.py
```

## How It Works

The Pythagorean numerology system assigns each letter a number from 1-9:

| Letters | Value |
|---------|-------|
| A, J, S | 1     |
| B, K, T | 2     |
| C, L, U | 3     |
| D, M, V | 4     |
| E, N, W | 5     |
| F, O, X | 6     |
| G, P, Y | 7     |
| H, Q, Z | 8     |
| I, R    | 9     |

### Calculation Process

1. Convert each letter in the name to its corresponding number (whitespace is ignored)
2. Sum all the numbers
3. Reduce to a single digit (1-9) by repeatedly adding the digits together
4. Exception: Master numbers 11, 22, and 33 are not reduced further

### Example

For the name "JOHN" (or "J O H N" - spaces are ignored):
- J = 1
- O = 6  
- H = 8
- N = 5

Total: 1 + 6 + 8 + 5 = 20
Reduced: 2 + 0 = 2

Therefore, "JOHN" has a numerology value of 2.

**Note**: The calculator automatically ignores all whitespace characters (spaces, tabs, etc.), so "John Doe", "JOHN DOE", and "J O H N  D O E" will all be calculated the same way.

## Numerology Meanings

- **1**: Leadership, independence, pioneering spirit
- **2**: Cooperation, balance, diplomacy
- **3**: Creativity, communication, optimism
- **4**: Stability, hard work, practicality
- **5**: Freedom, adventure, versatility
- **6**: Nurturing, responsibility, compassion
- **7**: Spirituality, introspection, analysis
- **8**: Material success, ambition, authority
- **9**: Humanitarian, generous, completion
- **11**: Intuition, inspiration, enlightenment (Master Number)
- **22**: Master builder, practical idealism (Master Number)
- **33**: Master teacher, compassion, healing (Master Number)

## File Structure

```
NumerologyCalculator/
├── app.py              # Main Streamlit application
├── numerology.py       # Core numerology calculation logic
├── test_numerology.py  # Test suite
├── requirements.txt    # Python dependencies
├── Requirements.md     # Original project requirements
└── README.md          # This file
```

## Requirements Met

✅ Text input for users to enter a name  
✅ Calculates numerology value on submission  
✅ Displays calculated value clearly  
✅ Supports both uppercase and lowercase letters  
✅ Ignores whitespace characters (spaces, tabs) in name input  
✅ Handles invalid/empty input with error messages  
✅ Saves calculation history and displays it in the app  
✅ Uses Python 3.7+ compatible code  
✅ Built with Streamlit for the user interface  
✅ Implements Pythagorean numerology system  
✅ Runnable with single command (`streamlit run app.py`)  
✅ Simple and user-friendly UI  
✅ Well-documented and modular code  
✅ Dependencies listed in requirements.txt  

## Technical Details

- **Python Version**: 3.7+
- **Framework**: Streamlit
- **Numerology System**: Pythagorean
- **Testing**: Custom test suite included
- **Code Quality**: Modular design with separate concerns

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## License

This project is open source and available under the MIT License.
