from redflagextraction import count_red_flags

# Test cases
# Test Case 1: Basic Test Case 
content1 = "This is a critical error. There is a major issue that needs to be addressed immediately." 
red_flags1 = ["critical", "major", "immediately"]
print(count_red_flags(content1, red_flags1))  # Expected output: {"critical": 1, "major": 1, "immediately": 1}

# Test Case 2: Case Insensitivity
content2 = "There are some critical issues. A CRITICAL error occurred. CRITICAL measures are needed."
red_flags2 = ["critical"]
print(count_red_flags(content2, red_flags2))  # Expected output: {"critical": 3}

# Test Case 3: No Red Flags Present content3 = "All systems are operational. No issues detected." 
content3 = "All systems are operational. No issues detected."
red_flags3 = ["critical", "major", "error"]
print(count_red_flags(content3, red_flags3))  # Expected output: {"critical": 0, "major": 0, "error": 0}

# Test Case 4: Empty Content 
content4 = ""
red_flags4 = ["critical", "major", "error"]
print(count_red_flags(content4, red_flags4))  # Expected output: {"critical": 0, "major": 0, "error": 0}

# Test Case 4: Empty Red Flags List 
content5 = "This is a critical error."
red_flags5 = []
print(count_red_flags(content5, red_flags5))  # Expected output: {}

# Test Case 6: Red Flags with Special Characters (ignore all the special character)
content6 = "Warning: critical! System failure detected."
red_flags6 = ["critical"]
print(count_red_flags(content6, red_flags6))  # Expected output: {"critical": 1}

# Test Case 7: Red Flags as Substrings
content7 = "Critical thinking is essential. Critically, we must consider all options."
red_flags7 = ["critical"]
print(count_red_flags(content7, red_flags7))  # Expected output: {"critical": 1}

# Edge Case 1: Overlapping Red Flags
content8 = "This is a critically critical situation."
red_flags8 = ["critical", "critically"]
print(count_red_flags(content8, red_flags8))  # Expected output: {"critical": 1, "critically": 1}

# Edge Case 2: Red Flags with Different Cases
content9 = "CritiCal issues should be resolved. CRITICAL steps are required."
red_flags9 = ["critical"]
print(count_red_flags(content9, red_flags9))  # Expected output: {"critical": 2}

# Edge Case 3: Red Flags Contained within Other Words 
content10 = "This situation is uncritical. Critically speaking, it is a minor issue."
red_flags10 = ["critical"]
print(count_red_flags(content10, red_flags10))  # Expected output: {"critical": 0}
