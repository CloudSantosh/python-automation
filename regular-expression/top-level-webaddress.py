#The check_web_address function checks if the text passed qualifies
#as a top-level web address, meaning that it contains alphanumeric characters
#(which includes letters, numbers, and underscores), as well as periods, dashes,
#and a plus sign, followed by a period and a character-only
#top-level domain such as ".com", ".info", ".edu", etc. Fill in
#the regular expression to do that, using escape characters, wildcards, repetition qualifiers,
#beginning and end-of-line characters, and character classes

import re

def check_web_address(text):
    pattern = r"^[a-zA-Z0-9_\-+.]+[.][a-zA-Z]+$"
    result = re.search(pattern, text)
    return result is not None

# Test cases
print(check_web_address("gmail.com"))           # True
print(check_web_address("www@google"))           # False
print(check_web_address("www.Coursera.org"))     # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True


#Here's an explanation of the changes made to your regular expression:

# ^[a-zA-Z0-9_\-+.]+ ==== This part matches the start of the string (^) and then matches one or more occurrences (+) of
#alphanumeric characters (including letters, numbers, and underscores), periods, dashes, and a plus sign.

# [.]=== This matches a literal period.

# [a-zA-Z]+$===This matches one or more occurrences of alphabetic characters (letters) at the end of the string ($),
# representing the top-level domain.

# With these changes, the regular expression should correctly check if the text qualifies as a top-level web address.
