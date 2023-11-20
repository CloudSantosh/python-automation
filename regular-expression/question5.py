# The long_words function returns all words that are at least 7 characters.
# Fill in the regular expression to complete this function.

import re

def long_words(text):
    pattern = r"\b\w{7,}\b"
    result = re.findall(pattern, text)
    return result

# Test cases
print(long_words("I like to drink coffee in the morning."))  # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon."))  # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night."))  # []

# Changes made:
#
# \b === Word boundaries are added to ensure that the pattern matches whole words.
# \w{7,} === This matches seven or more word characters (letters, digits, or underscores).
# With these changes, the regular expression correctly matches words that are at least 7 characters long. The findall function returns a list of all non-overlapping matches in the input text.