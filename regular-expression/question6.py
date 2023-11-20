# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
import re

def extract_pid(log_line):
    regex = r"\[(\d+)\].*?([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result.group(1), result.group(2))

# Test cases
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)

# Changes made to the regular expression:
#
# \[ === Matches the opening square bracket.
# (\d+) === Captures one or more digits (process ID).
# \] === Matches the closing square bracket.
# .*? === Matches any characters (non-greedy).
# ([A-Z]+) === Captures one or more uppercase letters (the messa