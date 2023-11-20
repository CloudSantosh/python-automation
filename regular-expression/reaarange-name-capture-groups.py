# Fix the regular expression used in the rearrange_name function so that it can match middle names,
# middle initials, as well as double surnames.

import re

def rearrange_name(name):
    result = re.search(r"^([\w\s'-]*),\s([\w\s'.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result.group(2), result.group(1))

name = rearrange_name("Kennedy, John F.")
print(name)
# Changes made to the regular expression:
#
# ([\w\s'-]*) === This captures the first part of the name (last name) and allows for word characters, whitespace, single quotes, hyphens, and periods.
# ,\s === This part matches the comma and any following whitespace after the last name.
# ([\w\s'.-]*) === This captures the second part of the name (first name, middle name, etc.) and allows for word characters, whitespace, single quotes, periods, hyphens, and dots.