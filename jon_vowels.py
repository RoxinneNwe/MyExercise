"""
def is_vowel(x):    # function to determine vowels in boolean
    while True:
        print("Enter '0' for exit.")
        ch = input("Enter any character: ")
        if ch == '0':
            break
        else:
            if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
                print(ch, "is a vowel.\n")

            else:
                print(ch,"is not a vowel.\n")

x = ''
print(is_vowel(x))
"""

def is_vowel(x):
    small_vowel=['a', 'e', 'i', 'o', 'u']
    big_vowel=['A', 'E', 'I', 'O', 'U']
    if(x in small_vowel) or (x in big_vowel):
        return True
    else:
        return False
import sys
print("Enter a character: ", end='')
character=sys.stdin.read(1)
if is_vowel(character):
    print(character, " is a Vowel")
else:
    print(character, " is a consonant")



