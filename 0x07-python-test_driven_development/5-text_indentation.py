#!/usr/bin/python3
"""
This module prints text with two new lines after each occurrence 
of ".", "?", and ":" characters.
"""

def text_indentation(text):
    """
    Prints text with two new lines after each occurrence of ".", "?", and ":" characters.

    Args:
        text (str): The text to be printed.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you?")
        Hello.
        How are you?

    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Define punctuation marks to look for
    punctuation_marks = ['.', '?', ':']

    # Iterate through each character in the text
    for char in text:
        # Print the character without new line
        print(char, end='')

        # If the character is a punctuation mark, print two new lines
        if char in punctuation_marks:
            print("\n\n", end="")
        
    # Print a new line if the last character is not a punctuation mark
    if text[-1] not in punctuation_marks:
        print()
