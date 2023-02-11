from string import ascii_lowercase


def substitutionDecrypt(cipher, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz "
  plain = ""
  cipher = cipher.lower()
  for ch in cipher:
    idx = alphabet.find(ch)
    plain += key[idx]
  return plain

testKey = "zyxwvutsrqponmlkjihgfedcba "
cipher = 'gsv jfrxp yildm ulc'
print("CipherText:", cipher)
print("PlainText:", substitutionDecrypt(cipher, testKey))