"""
Test module for the numerology calculator.

Simple tests to verify the numerology calculations work correctly.
"""

from numerology import (
    calculate_numerology_value,
    reduce_to_final_number,
    get_numerology_meaning,
    validate_name_input
)


def test_basic_calculations():
    """Test basic numerology calculations."""
    print("Testing basic calculations...")
    
    # Test simple name
    result = calculate_numerology_value("JOHN")
    print(f"JOHN = {result}")
    assert result in range(1, 34), "Result should be between 1-33"
    
    # Test case insensitivity
    result1 = calculate_numerology_value("john")
    result2 = calculate_numerology_value("JOHN")
    result3 = calculate_numerology_value("John")
    assert result1 == result2 == result3, "Case should not matter"
    
    print("✅ Basic calculations test passed!")


def test_number_reduction():
    """Test number reduction logic."""
    print("Testing number reduction...")
    
    # Test single digit
    assert reduce_to_final_number(5) == 5
    
    # Test reduction to single digit
    assert reduce_to_final_number(15) == 6
    assert reduce_to_final_number(29) == 11
    
    # Test master numbers
    assert reduce_to_final_number(11) == 11
    assert reduce_to_final_number(22) == 22
    assert reduce_to_final_number(33) == 33
    
    print("✅ Number reduction test passed!")


def test_validation():
    """Test input validation."""
    print("Testing input validation...")
    
    # Valid inputs
    valid, _ = validate_name_input("John")
    assert valid, "Valid name should pass validation"
    
    valid, _ = validate_name_input("John Doe")
    assert valid, "Name with space should pass validation"
    
    # Invalid inputs
    valid, _ = validate_name_input("")
    assert not valid, "Empty string should fail validation"
    
    valid, _ = validate_name_input("   ")
    assert not valid, "Whitespace only should fail validation"
    
    valid, _ = validate_name_input("123")
    assert not valid, "Numbers only should fail validation"
    
    print("✅ Validation test passed!")


def test_meanings():
    """Test that all numbers have meanings."""
    print("Testing number meanings...")
    
    # Test all single digits
    for i in range(1, 10):
        meaning = get_numerology_meaning(i)
        assert meaning != "Unknown number", f"Number {i} should have a meaning"
    
    # Test master numbers
    for num in [11, 22, 33]:
        meaning = get_numerology_meaning(num)
        assert meaning != "Unknown number", f"Master number {num} should have a meaning"
        assert "Master Number" in meaning, f"Master number {num} should be identified as such"
    
    print("✅ Meanings test passed!")


def test_whitespace_handling():
    """Test that whitespace characters are properly ignored in calculations."""
    print("Testing whitespace handling...")
    
    # Test that spaces don't affect calculation
    result1 = calculate_numerology_value("JOHN")
    result2 = calculate_numerology_value("J O H N")
    result3 = calculate_numerology_value(" JOHN ")
    result4 = calculate_numerology_value("JO HN")
    
    assert result1 == result2 == result3 == result4, "Whitespace should not affect calculation"
    
    # Test with tabs and multiple spaces
    result5 = calculate_numerology_value("J\tO\tH\tN")
    result6 = calculate_numerology_value("J   O   H   N")
    
    assert result1 == result5 == result6, "Tabs and multiple spaces should be ignored"
    
    # Test full names with various whitespace
    mary1 = calculate_numerology_value("MARY JANE")
    mary2 = calculate_numerology_value("MARYJANE")
    mary3 = calculate_numerology_value("M A R Y J A N E")
    
    assert mary1 == mary2 == mary3, "Full names should ignore whitespace consistently"
    
    print("✅ Whitespace handling test passed!")


def run_sample_calculations():
    """Run some sample calculations to demonstrate the system."""
    print("\n=== Sample Calculations ===")
    
    sample_names = ["JOHN", "MARY", "DAVID", "SARAH", "MICHAEL", "JENNIFER"]
    
    for name in sample_names:
        try:
            value = calculate_numerology_value(name)
            meaning = get_numerology_meaning(value)
            print(f"{name:10} = {value:2} | {meaning}")
        except Exception as e:
            print(f"Error calculating {name}: {e}")


if __name__ == "__main__":
    print("Running Numerology Calculator Tests...")
    print("=" * 40)
    
    try:
        test_basic_calculations()
        test_number_reduction()
        test_validation()
        test_meanings()
        test_whitespace_handling()
        
        print("\n🎉 All tests passed!")
        
        run_sample_calculations()
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
