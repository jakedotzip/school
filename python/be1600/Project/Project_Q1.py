# function to load morse code into a dictionary
def load_dict(morse_dict):
  morse_dict = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 
                'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 
                'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 
                'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', 
                '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.','0':'-----'}
  return morse_dict

# encode text to morse code
def encode(old_text, morse_dict):
  new_text = ""   # variable to store output
  for letter in old_text:   # loop thru the input
    if letter != ' ':
      new_text += morse_dict[letter] + ' '    # single space between each morse code to indicate different text characters
    else:
      new_text += '  '    # three-character space to indicate space between each words
  return new_text

# decode morse code to text
def decode(old_text, morse_dict): 
  word = ''               # variable to store morse code of a word, which will be translated later
  new_text = ''             # variable to store output
  for letter in old_text:
    if (letter == ' '):     # check for space
      space = space + 1     # keep track of space
      if space == 3:        # if space = 3, there's a new word
        new_text += ' '
      elif space < 2:       # if space < 2, translate the morse code to corresponding character
        new_text += list(morse_dict.keys())[list(morse_dict.values()).index(word)]
        word = ''    
    else:
      space = 0
      word += letter      # store morse code 
  return new_text

# function to print menu
def print_menu():
  print("Hello, this program allows you to translate text to morse code or translate morse code to text.\n")
  print("Please, select one of the below options:\n")
  print("*** Enter 't' for encoding text")
  print("*** Enter 'm' for encoding text")
  print("*** Enter 'e' for encoding text")
  opt = input("\nMy input is: ")
  while True: 
    if opt == 't' or opt == 'm' or opt == 'e':
      return opt
    else:
      print("***invalid option***")
      opt = input("Please enter a valid option: ")

# main function
def main():
  morse_dict = {}
  morse_dict = load_dict(morse_dict)
  while True:
    opt = print_menu()
    if opt == 't':
      text = input("\nPlease enter text to translate:\n")
      morse = encode(text.upper(), morse_dict)
      print(morse)
      print()
    elif opt == 'm':
      morse = input("\nPlease enter morse to translate:\n")
      text = decode(morse, morse_dict)
      print(text)
      print()
    else:
      print("\nThanks for using this program!")
      break

main()
  

