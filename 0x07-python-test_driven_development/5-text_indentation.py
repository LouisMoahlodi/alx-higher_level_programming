# #!/usr/bin/python3
# """
# This module prints text with two new lines after each occurrence 
# of ".", "?", and ":" characters.

# """

# def text_indentation(text):
#     """
#     Prints text with two new lines after each occurrence of ".", "?", and ":" characters.

#     Args:
#         text (str): The text to be printed.

#     Returns:
#         None

#     Raises:
#         TypeError: If text is not a string.

#     Example:
#         >>> text_indentation("Hello. How are you?")
#         Hello.
#         How are you?

#     """
#     # Check if text is a string
#     if not isinstance(text, str):
#         raise TypeError("text must be a string")
    
#     # Define punctuation marks to look for
#     punctuation_marks = ['.', '?', ':']

#     # Split text into lines
#     lines = text.splitlines()

#     # Iterate through each line of the text
#     for line in lines:
#         # Flag to check if the previous character was a punctuation mark
#         previous_punctuation = False

#         # Iterate through each character in the line
#         for char in line:
#             # Print the character without new line
#             print(char, end='')

#             # If the character is a punctuation mark, print two new lines
#             if char in punctuation_marks:
#                 # Check if the previous character was also a punctuation mark
#                 if previous_punctuation:
#                     print("\n", end="")
#                 print("\n", end="")
#                 previous_punctuation = True
#             else:
#                 previous_punctuation = False
        
#         # If the previous character was a punctuation mark, print a new line
#         if previous_punctuation:
#             print()
#         else:
#             print()
