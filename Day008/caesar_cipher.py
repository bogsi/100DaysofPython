import art

print(art.logo)

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(original_text, shift_amount, encrypt_or_decrypt):
    """
    Encrypt text using Caesar cipher with given shift value.

    Args:
        text (str): The plaintext message to encrypt
        shift (int): Number of positions to shift (0-25)

    Returns:
        str: The encrypted ciphertext
    """
    output_text = ""
    if encrypt_or_decrypt == "decode":
        shift_amount *= -1
    else:
        shift_amount *= 1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encrypt_or_decrypt}d text: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type the 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(text, shift, direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
