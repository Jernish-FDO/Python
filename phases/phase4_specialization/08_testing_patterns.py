# Testing Patterns Buddy-Guide

import pytest

# The "Arrange-Act-Assert" Pattern
def test_buddy_logic():
    # Arrange
    buddy_name = "Jernish"
    
    # Act
    upper_name = buddy_name.upper()
    
    # Assert
    assert upper_name == "JERNISH"

# Mocking Example (Conceptual)
# def test_api_call(mocker):
#     mocker.patch('requests.get', return_value={'status': 'ok'})
#     ...

if __name__ == "__main__":
    print("Run this with: pytest 08_testing_patterns.py")
