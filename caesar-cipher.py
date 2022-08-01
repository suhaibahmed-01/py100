alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(input_text, shift_number, cipher_method):
  output_text = ""
  if cipher_method == "decode":
    shift_number *= -1
  for char in input_text:

    
    if char in alphabet:
      index = alphabet.index(char)
      new_index = index + shift_number
      output_text += alphabet[new_index]
    else:
      output_text += char
  print(f"\n\nYour {cipher_method}d text message is : {output_text}")


from caesar_cipher_logo import logo
print("\n\t",logo)


rerun = False
while not rerun:
  method = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("\n\nType your message:\n").lower()
  shift = int(input("\n\nType the shift number:\n"))

  
  shift = shift % 26
  caesar_cipher(input_text = text, shift_number = shift, cipher_method = method)
  

  restart = input("\n\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    rerun = True
    print("Goodbye then!")
