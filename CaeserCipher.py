#caesar cipher cracking
#jangan lupa pip install colorama 
from colorama import Fore, Style, init

init()

print(Fore.CYAN + "=" * 55)
print("=" * 55 + Style.RESET_ALL)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(plaintext, shift):
    encoded_text = ''
    for letter in plaintext:
        if letter in alphabet:
            index = alphabet.index(letter)
            encoded_text += alphabet[(index + shift) % len(alphabet)]
        else:
            encoded_text += letter
    return encoded_text

def decode(ciphertext, shift):
    plaintext = ''
    for letter in ciphertext:
        if letter in alphabet:
            index = alphabet.index(letter)
            plaintext += alphabet[(index - shift) % len(alphabet)]
        else:
            plaintext += letter
    return plaintext

print(Fore.YELLOW + "=" * 21)
print("ini adalah decode nya")
print("=" * 21 + Style.RESET_ALL)

ciphertext = 'suYORFCe94AhOx27vqFH/UlTO66CcDq/E9Ke3C2JTmII+HoBjGfbzxYK0+fT3ApEG8jpSy5bhbAtCRBSLUbR9YlUQu7SlZhD15a6qxjvu3owyydidquVN4VmvZFx5DU6yDfuTzTdN2t1dM1w4LIPSMR5NyYTVSFXKbjS2OASz8SQ58MUt+Cd9IFxTCqGMtmA7A+sYMYmCYtiIGDd5wFFsqef5X4ku8m17OOwdD4jJO6TdkCgcOKCaZWJNxCkzs06Yf8ySFMehNTxHpWjPpm9k1iqb5P3dljEMuT5INYTRoxvxuxEvhLBLFgLFNXN67d6rtHMIdy4U7YDvmSqSqfxWQ=='
for shift in range(26):
    plaintext = decode(ciphertext, shift)
    print(Fore.GREEN + f'Shift {shift}: {plaintext}' + Style.RESET_ALL)

print(Fore.YELLOW + "=" * 21)
print("ini adalah encode nya")
print("=" * 21 + Style.RESET_ALL)

plaintext = 'suYORFCe94AhOx27vqFH/UlTO66CcDq/E9Ke3C2JTmII+HoBjGfbzxYK0+fT3ApEG8jpSy5bhbAtCRBSLUbR9YlUQu7SlZhD15a6qxjvu3owyydidquVN4VmvZFx5DU6yDfuTzTdN2t1dM1w4LIPSMR5NyYTVSFXKbjS2OASz8SQ58MUt+Cd9IFxTCqGMtmA7A+sYMYmCYtiIGDd5wFFsqef5X4ku8m17OOwdD4jJO6TdkCgcOKCaZWJNxCkzs06Yf8ySFMehNTxHpWjPpm9k1iqb5P3dljEMuT5INYTRoxvxuxEvhLBLFgLFNXN67d6rtHMIdy4U7YDvmSqSqfxWQ=='
for shift in range(26):
    ciphertext = encode(plaintext, shift)
    print(Fore.RED + f'Shift {shift}: {ciphertext}' + Style.RESET_ALL)
