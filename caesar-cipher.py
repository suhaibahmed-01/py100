alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("\n\nType your message:\n").lower()
shift = int(input("\n\nType the shift number:\n"))
 

def caesar_cipher(input_text, shift_number, cipher_method):
  output_text = ""
  if cipher_method == "decode":
      shift_number *= -1
  for letter in input_text:
    index = alphabet.index(letter)
    new_index = index + shift_number
    output_text += alphabet[new_index]
  print(f"\n\nYour {method}d output message is : {output_text}")


caesar_cipher(input_text = text, shift_number = shift, cipher_method = method)
