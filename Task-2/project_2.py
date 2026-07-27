def shift_letter(char, shift):
    # determine the ASCII base on whether its uppercase or lowercase
    if "A" <= char <= "Z":
        base = ord("A")  # base 65 for uppercase
    elif "a" <= char <= "z":
        base = ord("a")  # base 97 for lowercase
    else:
        # edge case: If it's a space or punctuation, don't change it
        return char

    # applying the core formula: E(x) = (x + n) % 26
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt_caesar(plaintext, shift):
    # keep the shift within the 0-25 range to avoid errors
    shift = shift % 26
    
    # loop through each character to build the ciphertext string
    ciphertext = ""
    for char in plaintext:
        ciphertext += shift_letter(char, shift)
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    # to decrypt, we run the same logic but shift in the negative direction
    shift = shift % 26
    return encrypt_caesar(ciphertext, -shift)


def main():
    print("=== DECODELABS CRYPTOGRAPHIC ENGINE ===")

    # step 1: Gather User Inputs (IPO Cycle - Input)
    user_text = input("Enter the plaintext message to encrypt: ")
    shift_key = int(input("Enter the shift key (e.g., 3): "))

    # step 2: Processing data through our functions (IPO Cycle - Process)
    encrypted_msg = encrypt_caesar(user_text, shift_key)
    decrypted_msg = decrypt_caesar(encrypted_msg, shift_key)

    # step 3: Display results to verify it works (IPO Cycle - Output)
    print("\n== SYSTEM VERIFICATION OUTPUT ==")
    print(f"Original Input:  {user_text}")
    print(f"Ciphertext:      {encrypted_msg}")
    print(f"Decrypted Test:  {decrypted_msg}")
    print("==================================")


if __name__ == "__main__":
    main()
