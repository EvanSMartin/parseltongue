import string
def remove_punctuations(word):
    return "".join(i.lower() for i in word if i in string.ascii_letters)

def reverse (text):
    return textg[::-1]

def is_Palidrome(text):# Calling reverse function
    text = remove_punctuations(text)
    return text == reverse(text)

something = input "A man, a plan, a canal: Panama."

    #Checking if both string are equal or not
    if (is_Palidrome(something)):
        print("So cool! This text IS a palindrome.")
    else:
        print("No, it is not a palindrome, try again!")
