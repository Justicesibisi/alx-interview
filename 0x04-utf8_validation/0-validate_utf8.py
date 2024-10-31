#!/usr/bin/python3
"""
Masking and Shifting: We use byte & 0xFF to ensure only the last 8 bits are considered.
"""
def validUTF8(data):
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

    return num_bytes == 0
