import re

def extract_pid(text):
    # Match a sequence of one or more digits
    pid_pattern = r'\b\d+\b'

    # Search for the pattern in the text
    match = re.findall(pid_pattern, text)
    #print(match)
    #print(match[1])

    # Check if a match is found
    if match:
        # Extract the matched PID
        pid = match
        #print(pid)
        return pid
    else:
        return None

# Example usage:
text_with_pid = "The process ID is 12345. Another process has ID 6789."
result = extract_pid(text_with_pid)

if result:
    for each_data in result:
        print(f"Found PID: {each_data}")
else:
    print("No PID found.")
