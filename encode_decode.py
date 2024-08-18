alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = 0
while answer == 0:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        def encrypt(original_text, shift_amount):
            new_text_list = []
            for letter in original_text:
                new_letter = alphabet.index(letter) + shift_amount
                #Always in the range 0, 25. What happens if you try to shift z forwards by 9? Can you fix the code?
                new_letter %= len(alphabet)
                new_text_list.append(new_letter)
            print(new_text_list)

            new_text = ''
            for element in new_text_list:
                new_text = new_text + alphabet[element]

            print(f"Here's the encode result: {new_text}")
            
        encrypt(text, shift)

    elif direction == 'decode':
        def decrypt(original_text, shift_amount):
            new_text_list = []
            for letter in original_text:
                new_letter = alphabet.index(letter) - shift_amount
                # Always in the range 0, 25
                new_letter %= len(alphabet)
                new_text_list.append(new_letter)

            new_text = ''
            for element in new_text_list:
                new_text = new_text + alphabet[element]

            print(f"Here's the decode result: {new_text}")
        decrypt(text, shift)

    else:
        print("You must put the right word: encode or decode.")


    answer = input("Type 'yes' if you want to go again, if not type 'no'. :P \n").lower()
    if answer == "yes" or answer == "y":
        answer = 0
    elif answer == "no" or answer == "n":
        answer = 1
    else:
        print("You must type the correct word")





