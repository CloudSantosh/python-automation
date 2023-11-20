# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.

import re
def multi_vowel_words(text):
  pattern = r'\b\w*[aeiou]{3,}\w*\b'
  result = re.findall(pattern, text, re.IGNORECASE)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []

# Explanation of the regular expression:
#
# \b: Word boundary to ensure we match whole words.
# \w*: Zero or more word characters (letters, digits, or underscores) before and after the consecutive vowels.
# [aeiou]{3,}: Matches 3 or more consecutive vowels (a, e, i, o, u) case-insensitively.
# \w*: Zero or more word characters after the consecutive vowels.
# \b: Word boundary to ensure we match whole words.
# The re.IGNORECASE flag is used to make the pattern case-insensitive.