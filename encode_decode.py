alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = 0
while answer == 0:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def ceasars_encode_decode(original_text,shift_amount, encode_decode):

        if encode_decode == 'decode':
            shift_amount = shift_amount * -1

        
        new_text_list = []
        for letter in original_text:
            new_letter = alphabet.index(letter) + shift_amount
            #Always in the range 0, 25. What happens if you try to shift z forwards by 9? Can you fix the code?
            new_letter %= len(alphabet)
            new_text_list.append(new_letter)

        new_text = ''
        for element in new_text_list:
            new_text = new_text + alphabet[element]

        print(f"Here's the {encode_decode} result: {new_text}")
                

    ceasars_encode_decode(original_text = text, shift_amount= shift, encode_decode=direction)

    answer = input("Type 'yes' if you want to go again, if not type 'no'. :P \n").lower()
    if answer == "yes" or answer == "y":
        answer = 0
    elif answer == "no" or answer == "n":
        answer = 1
    else:
        print("You must type the correct word")





