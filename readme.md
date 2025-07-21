Custom Hash Function Project

Project Overview

This project implements a custom hashing algorithm in Python to understand the fundamentals of hashing, including:

Character manipulation (ASCII conversions and shifts)

Modular arithmetic

Compression to a fixed-length hash value

The custom hash function is tested and compared against the standard SHA-256 cryptographic hash function from Python's hashlib library.

Algorithm Description

The custom hashing algorithm works as follows:

Input Handling: Accepts any string, including empty strings (which default to a predefined value).

ASCII Conversion: Each character in the input string is converted to its ASCII value and shifted by its position index.

Modular Arithmetic: The shifted values are multiplied by their (index + 1) and taken modulo a prime number (997) to spread the values uniformly.

Compression: The results are combined into a single string, then compressed using a rolling XOR to create a fixed-length array.

Hex Encoding: The final array is converted into a hexadecimal string representing the hash output, truncated or padded to a fixed length (default 32 characters).

How to Run

Make sure you have Python 3 installed.

Run the script using:
python hash.py

The script outputs the custom hash and the truncated SHA-256 hash for several test inputs.

Sample Output

Input: 'hello'
Custom Hash : 9a6d8f3b0c4e2f17a9b6c4d8e0f2a3b1
SHA-256 (cut): 2cf24dba5fb0a30e26e83b2ac5b9e29e

Input: 'Hello'
Custom Hash : 8f3c6a1b2d9e0c7f5a3b4d8e1f2a7c6b
SHA-256 (cut): 185f8db32271fe25f561a6fc938b2e26

...

(Note: The actual hash values will vary based on your implementation.)

Observations

The custom hash function produces consistent outputs for the same inputs.

Small changes in input strings result in significantly different hashes, demonstrating the avalanche effect.

While this custom hash provides a good learning tool, it lacks cryptographic security features such as collision resistance, unlike SHA-256.

Conclusion

This project helped in understanding the principles behind hashing algorithms by implementing a simple hash function from scratch and comparing it to a standard cryptographic hash function. While custom hashes can be educational, secure applications require established cryptographic algorithms like SHA-256.

References

Python hashlib Documentation: https://docs.python.org/3/library/hashlib.html

Cryptographic Hash Functions (Wikipedia): https://en.wikipedia.org/wiki/Cryptographic_hash_function

