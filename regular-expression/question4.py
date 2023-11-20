# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded
# by parentheses, with at least the first character in uppercase (if it's a letter), returning True if
# the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies
# used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the
# regular expression in this function:
import re

def contains_acronym(text):
    pattern = r"\([A-Z0-9][A-Za-z0-9]*\)"
    result = re.search(pattern, text)
    return result is not None

# Test cases
print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True

# Here's an explanation of the changes made to your regular expression:
#
# \( and \) === Match the opening and closing parentheses.
# [A-Z0-9] === Match an uppercase letter or a digit for the first character inside the parentheses.
# [A-Za-z0-9]* === Match zero or more occurrences of uppercase letters, lowercase letters, or digits after the first character.