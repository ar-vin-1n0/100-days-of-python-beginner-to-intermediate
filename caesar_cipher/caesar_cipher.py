from alphabets import alphabets

def caesar_cipher(text,shift,encode_or_decode):
    changed_text = ""

    if encode_or_decode == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabets:
            changed_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift
            shifted_position %= len(alphabets)
            changed_text += alphabets[shifted_position]
    print(f" your {encode_or_decode}ed text  {changed_text.lower()}")

stay = True
while stay:

    text = input("Enter your text : ").lower()

    shift = int(input("Enter your shift : "))

    encode_or_decode = input("Enter ur choice encode or decode : ").lower()

    print(caesar_cipher(text,shift,encode_or_decode))

    to_stay = input("Do you want to stay or not? [Y/N] : ").lower()

    if to_stay == "n":
       stay = False