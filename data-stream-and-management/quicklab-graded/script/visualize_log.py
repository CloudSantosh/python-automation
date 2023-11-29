import re
from datetime import datetime
import matplotlib.pyplot as plt

# Sample log file format: "2023-01-01 12:34:56 : INFO : Log message"
log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) : (\w+) : (.+)')

# Sample log file name
log_file_path = '../data/log.txt'

# Dictionary to store log level counts
log_level_counts = {}

# Read and process the log file
with open(log_file_path, 'r') as file:
    for line in file:
        # print(f"{line}")
        match = log_pattern.match(line)
        print(f'{match}')
        if match:
            timestamp_str, log_level, _ = match.groups()

            # Convert timestamp string to a datetime object
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

            # Increment log level count
            log_level_counts[log_level] = log_level_counts.get(log_level, 0) + 1

# Extract data for plotting
log_levels = list(log_level_counts.keys())
counts = list(log_level_counts.values())

# Plotting the bar chart
plt.bar(log_levels, counts, color=['blue', 'green', 'yellow', 'orange', 'red'])
plt.title('Log Level Frequency Over Time')
plt.xlabel('Log Level')
plt.ylabel('Frequency')
plt.show()
