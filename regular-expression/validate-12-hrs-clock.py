#The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12,
# with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM,
# in upper or lower case. Fill in the regular expression to do that.
# How many of the concepts that you just learned can you use here?


import re

def check_time(text):
    pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9] ?[APMapm]{2}$"
    result = re.search(pattern, text)
    return result is not None

# Test cases
print(check_time("12:45pm"))    # True
print(check_time("9:59 AM"))    # True
print(check_time("6:60am"))     # False
print(check_time("five o'clock"))  # False

#Here's an explanation of the regular expression:
# ^ === Anchors the pattern to the beginning of the string.
# (1[0-2]|0?[1-9]): Matches the hour, which can be a number from 1 to 12. It allows for single-digit hours
# and disallows leading zeros for double-digit hours.
# : === Matches the colon that separates the hours and minutes.
# [0-5][0-9] === Matches the minutes, which range from 00 to 59.
# ? === Matches an optional space.
# [APMapm]{2} === Matches AM, am, PM, or pm, regardless of case.
# $ === Anchors the pattern to the end of the string.
