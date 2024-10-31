#!/usr/bin/python3
"""
This module contains a function to validate UTF-8 encoding.
"""

def validUTF8(data):
    """
    Validate if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        # Only the least significant 8 bits are relevant for UTF-8
        byte &= 0xFF

        if num_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check if this byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # Ensure no unclosed multibyte sequence remains
    return num_bytes == 0