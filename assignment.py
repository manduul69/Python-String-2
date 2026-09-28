# You can remove 'pass' if you written code in the function 

# Exercise 1
def is_valid_email(text):
    count = 0
    for c in text:
        if c == "@" or c == ".":
            count += 1
    if count == 2:
        return("valid")
    else:
        return("invalid")
print(is_valid_email("manduul@gmail.com"))

# Exercise 2
def remove_vowels(text):
    b = ""
    count=0
    vowels="aouieAOUIE"
    for c in text:
        if c in vowels:
            b+= ""
        else:
            b+=c
    return b
print(remove_vowels("please call me tomorrow"))

# Exercise 3
def get_initials(text):
    a=""
    b=""
    c=""
    d=""
    a,b = text.split()
    c=a[0]
    d=b[0]
    return c.upper()+"."+ d.upper()+"."
print(get_initials("elon musk"))

# Exercise 4
def extract_year(text):
    string=text.split()
    b="1234567890"
    for word in string:
        if word[0] in b:
            if int(word)<2026 and int(word)>1700:
                return word
    return false
print(extract_year("i was born in 2010"))

# Exercise 5
def is_palindrome(text):
    cleaned = ""

    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False
print(is_palindrome("Never odd or even"))
