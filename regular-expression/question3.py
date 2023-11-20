# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with
# an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period,
# question mark, or exclamation point.
import re

def check_sentence(text):
    result = re.search(r"^[A-Z][a-z\s]*[.?!]$", text)
    return result is not None

# Test cases
print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True

#  In the corrected regular expression:

# ^[A-Z] === Asserts that the sentence starts with an uppercase letter.
# [a-z\s]* === Matches zero or more lowercase letters or spaces.
# [.?!]$ === Asserts that the sentence ends with a period, question mark, or exclamation point.
# Now, the function should correctly return True if the text looks like a standard sentence and False otherwise.