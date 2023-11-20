import re

def check_character_groups(text):
    result = re.search(r"\w+\s+\w+", text)
    return result is not None

# Test cases
print(check_character_groups("One"))                                # False
print(check_character_groups("123  Ready Set GO"))                   # True
print(check_character_groups("username user_01"))                   # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

# In this code, \w+ matches one or more word characters, \s+ matches one or more whitespace characters, and
# the pattern \w+\s+\w+ looks for the occurrence of two alphanumeric character groups separated by whitespace.
# The function should return True if such character groups are found in the input text, and False otherwise.