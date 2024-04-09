
import string

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet = list(string.ascii_lowercase)


def encrypt(plain_text, shift_amount):

	new_word = []

    for i in plain_text:

        # Keep spaces
        if i == ' ':
            new_word += ' '

        else:

            original_index = alphabet.index(i)
            next_index = (original_index + shift_amount)

            if (next_index >= 26):
                next_index -= 26

            new_word += alphabet[next_index]

    cipher_text = "".join(new_word)
    print(f"The encoded text is: {cipher_text}")


encrypt(plain_text=text, shift_amount=shift)
