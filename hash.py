import hashlib
import tkinter as tk
from tkinter import scrolledtext

def custom_hash(input_str, hash_len=32):
    if not input_str:
        input_str = "default"  # Handle empty input

    ascii_values = [ord(c) + i for i, c in enumerate(input_str)]
    mod_prime = 997
    mixed_values = [(val * (i+1)) % mod_prime for i, val in enumerate(ascii_values)]
    combined = ''.join(str(v) for v in mixed_values)
    result = [0] * hash_len
    for i, ch in enumerate(combined):
        result[i % hash_len] ^= ord(ch)
    final_hash = ''.join(f"{b:02x}" for b in result)
    return final_hash[:hash_len]

def on_hash_click():
    text = input_text.get("1.0", "end-1c")  # Get input text from Text widget
    if text.strip() == "":
        output_custom.delete("1.0", tk.END)
        output_sha256.delete("1.0", tk.END)
        output_custom.insert(tk.END, "Please enter some text.")
        return

    c_hash = custom_hash(text)
    sha_hash = hashlib.sha256(text.encode()).hexdigest()

    output_custom.delete("1.0", tk.END)
    output_sha256.delete("1.0", tk.END)

    output_custom.insert(tk.END, c_hash)
    output_sha256.insert(tk.END, sha_hash)

# Setup GUI window
root = tk.Tk()
root.title("Custom Hash Function vs SHA-256")

# Input Label and Text Box
tk.Label(root, text="Enter text to hash:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_text = scrolledtext.ScrolledText(root, width=60, height=5)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Hash Button
hash_btn = tk.Button(root, text="Generate Hashes", command=on_hash_click)
hash_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Output Labels and Text Boxes
tk.Label(root, text="Custom Hash (32 chars):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
output_custom = scrolledtext.ScrolledText(root, width=60, height=2)
output_custom.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="SHA-256 Hash (64 chars):").grid(row=5, column=0, padx=10, pady=5, sticky="w")
output_sha256 = scrolledtext.ScrolledText(root, width=60, height=2)
output_sha256.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
