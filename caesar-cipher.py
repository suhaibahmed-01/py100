alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
 

def caesar_cipher(input_text, shift_number, cipher_method):
  output_text = ""
  if cipher_method == "decode":
      shift_number *= -1
  for letter in input_text:
    index = alphabet.index(letter)
    new_index = index + shift_number
    output_text += alphabet[new_index]
  print(f"Your {method}d output message is : {output_text}")


caesar_cipher(input_text = text, shift_number = shift, cipher_method = method)
