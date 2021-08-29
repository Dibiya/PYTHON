str = input('Enter the value:')
str = str.casefold()
rev = reversed(str)
if list(str) == list(rev):
    print("THIS IS A PALINDROME")
else:
    print("THIS NOT A PALINDROME")


'''txt='HELLO MY Friends'
print(list((txt)))'''

