import re
from collections import defaultdict

def count_red_flags(content, red_flags):
    # Convert content to lowercase
    content = content.lower()
    
    #If redFlags array is empty
    if not red_flags:
        return {}
    
    # Create a dictionary to hold the counts of each red flag
    red_flag_counts = defaultdict(int)
    
    # Normalize the red flags to lowercase and remove special characters for the search
    normalized_red_flags = [re.escape(flag.lower()) for flag in red_flags]
    
    # Define the regular expression pattern to match the whole word ignoring special characters
    pattern = re.compile(r'\b(' + '|'.join(normalized_red_flags) + r')\b', re.IGNORECASE)
    
    # Find all matches in the content
    matches = pattern.findall(content)
    
    # Count each match
    for match in matches:
        red_flag_counts[match] += 1
    
    # Fill in zeros for red flags that were not found
    for flag in red_flags:
        if flag.lower() not in red_flag_counts:
            red_flag_counts[flag.lower()] = 0
    
    return dict(red_flag_counts)

