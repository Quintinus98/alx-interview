#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    count_bytes = 0

    # Masks for checking the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # The data set can contain multiple characters
    for byte in data:
        # Handling the 8 least significant bits of each integer (byte)
        byte = byte & 0xFF

        if count_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 | mask2)) == mask1:
                # Invalid 10xxxxxx byte in start
                return False
            else:
                # Count the number of leading 1s to determine the length
                mask = mask1
                while byte & mask:
                    count_bytes += 1
                    mask >>= 1

                # A character in UTF-8 can only be 1 to 4 bytes long
                if count_bytes == 1 or count_bytes > 4:
                    return False
        else:
            # Check that the byte is of form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        count_bytes -= 1

    # All characters should be completely processed
    return count_bytes == 0
