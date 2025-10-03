import re

'''
practice 1_a
'''

# Match years (exactly 4 digits)
text = "Born in 1995, graduated 2017, now it's 24"
pattern = r"\d{4}"  # Fill in the repetition

matches = re.findall(pattern, text)
print(f"Years found: {matches}")

'''
practice 1_b
'''
# Validate hex color codes (#RGB or #RRGGBB)
colors = ["#FFF", "#FFFFFF", "#12AB56", "#GGG", "#12"]
# Write pattern for 3 or 6 hex digits after #
pattern = r"#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})"  
# Hint: [0-9A-Fa-f]{3} or {6}

results = re.findall(pattern, " ".join(colors))
print(f"Valid colors: {results}")

'''
practice 1_c
'''
# Extract and validate US Social Security Numbers
# Format: XXX-XX-XXXX where X is a digit
text = "SSN: 123-45-6789, Invalid: 12-345-6789, 123-4-5678"
# Write pattern using {n} for each section
pattern = r"\b\d{3}-\d{2}-\d{4}\b"  # Fill in the pattern
matches = re.findall(pattern, text)
print(f"Valid SSNs: {matches}")

'''
practice 2_a
'''
# Match repeated words like "very very" or "really really"
text = "It's very very important and really really cool"
pattern = r"(\w+) \1"  # Fill in to match repeated words

matches = re.findall(pattern, text)
print(f"Repeated words: {matches}")

'''
practice 2_b
'''
# Extract date components (MM/DD/YYYY)
dates = ["12/25/2024", "01/01/2025", "13/40/2024"]
# Write pattern with groups for month, day, year
pattern = r'(\d{2})/(\d{2})/(\d{4})'
# Validate and extract each component
results = []
for date in dates:
    match = re.match(pattern, date)
    if int(match.group(1)) <= 12 and int(match.group(2)) <= 31:
        date = match.group(0)
        results.append(date)
print(f"Valid dates: {results}")

'''
practice 2_c
'''
# Parse URLs: protocol://domain/path
urls = ["http://example.com/page", "https://site.org/path/to/file"]
# Create groups for protocol, domain, and path
pattern = r"(https?)://([^/]+)(/.*)?"
# Print each component separately
for url in urls:
    match = re.search(pattern, url)
    if match:
        protocol = match.group(1)
        domain = match.group(2)
        path = match.group(3)
        print(f"URL: {url}, Protocol: {protocol}, Domain: {domain}, Path: {path}")


'''
practice 3_a
'''
# Extract name and age from text
text = "My name is Alice and I am 25 years old"
pattern = r"name is (\w+) and I am (\d+)"


# Complete the code to print name and age separately
match = re.search(pattern, text)
if match:
    # Print the captured groups
    name = match.group(1)
    age = match.group(2)
    print(f"Name: {name}")
    print(f"Age: {age}")

'''
practice 3_b
'''
# Parse email addresses with named groups
emails = ["john.doe@company.com", "alice_smith@university.edu"]
# Write pattern with named groups for username and domain
pattern = r"(?P<username>[\w.]+)@(?P<domain>[\w.]+\.\w+)"
# Pattern: (?P<user>...) @ (?P<domain>...)
results = []
for email in emails:
    match = re.search(pattern, email)
    if match:
        results.append(f"Email: {match.group('username')}")
        results.append(f"Domain: {match.group('domain')}")
print(results)

'''
practice 3_c
'''
# Extract and validate time in HH:MM:SS format
times = ["12:30:45", "25:00:00", "10:65:30", "09:15:22"]
# Write pattern with groups for hours, minutes, seconds
pattern = r'(\d{2}):(\d{2}):(\d{2})'
# Validate each component (hours: 00-23, minutes/seconds: 00-59)
valid_times = []
for time in times:
    match = re.match(pattern, time)
    if match.group(1) < '24' and match.group(2) < '60' and match.group(3) < '60':
        valid_times.append(time)
print(f"Valid times: {valid_times}")

'''
practice 4_a
'''
text = "Hello there! Hi everyone. Hey you. Goodbye."
pattern = r"\b(Hi|Hello|Hey)\b"  # Fill in: Match Hello, Hi, or Hey

matches = re.findall(pattern, text)
print(f"Greetings: {matches}")

'''
practice 4_b
'''
# Validate file extensions for documents
files = ["report.doc", "essay.docx", "data.xlsx", "notes.txt", "summary.pdf", "aniya_.pdf"]
# Match .doc, .docx, .pdf, or .txt files
pattern = r"\S*\.(docx?|pdf|txt)$"  # Fill in: Use $ to assert end of string
# Use alternation with proper grouping
matches = [f for f in files if re.findall(pattern, f)]
print(f"Valid document files: {matches}")

'''
practice 4_c
'''
# Parse different date formats
dates = ["2024-01-15", "15/01/2024", "Jan 15, 2024", "January 15, 2024", "2024 15 January"]
# Write pattern to match:
# - YYYY-MM-DD
# - DD/MM/YYYY
# - Mon DD, YYYY
# - YYYY DD Month
# Use alternation to handle all formats
pattern = r'(\d{4}-\d{2}-\d{2})|(\d{2}/\d{2}/\d{4})|(\b[A-Za-z]{3}\b \d{2}, \d{4}|\d{4} \d{2} [A-Za-z]{3,9})'
matches = [d for d in dates if re.match(pattern, d)]
print(f"Matched dates: {matches}")

'''
practice 5-a
'''
# Find a number and print its position
text = "The temperature is 72 degrees"
pattern = r"\d+"

match = re.search(pattern, text)
if match:
    # Print the number and where it was found
    print(f"Number '{match.group()}' found at position {match.span()}")
    # Use match.group() and match.span()


'''
practice 5_b
'''
# Extract URL components and their positions
url = "https://www.example.com/path/to/page"
pattern = r"(https?)://([^/]+)(.*)"

# Use the match object to extract:
# - Protocol (http or https)
# - Domain
# - Path
# - Position of each component
match = re.search(pattern, url)
if match: 
    protocol = match.group(1)
    domain = match.group(2)
    path = match.group(3)
    print(f"Protocol at position {match.span(1)}: {protocol}")
    print(f"Domain at position {match.span(2)}: {domain}")
    print(f"Path at position {match.span(3)}: {path}")
'''
practice 5_c
'''
# Build a function that returns match details as dictionary
def get_match_info(text, pattern):
    """
    Return dictionary with:
    - 'found': Boolean
    - 'match': The matched text
    - 'groups': All captured groups
    - 'position': (start, end) tuple
    - 'before': Text before match
    - 'after': Text after match
    """
    # Implement this function
    match = re.search(pattern, text)
    if match:
        start, end = match.span()
        return {
            'found': True,
            'match': match.group(0),
            'groups': match.groups(),
            'position': match.span(),
            'before': text[:start],
            'after': text[end:]
        }
        # print(f"Found: {True}\nMatch: {match.group(0)}\nGroups: {match.groups()}\nPosition: {match.span()}\nBefore: {text[:start]}\nAfter: {text[end:]}")
    else:
        return {
            'found': False,
        }
text = "Price: $19.99 (discounted)"
pattern = r"\$(\d+)\.(\d{2})"
info = get_match_info(text, pattern)
print(info)

'''
practice 6_a
'''
# Check if string starts with "Hello"
texts = ["Hello World", "Say Hello", "Hello", "HELLO"]
pattern = r"Hello"

for text in texts:
    # Use re.match to check if text starts with Hello
    match = re.match(pattern, text)
    # Print whether it matches or not
    if match:
        print(f"Matched Text: {text}")

'''
practice 6_b
'''
# Validate phone number format from start of string
# Format: (XXX) XXX-XXXX or XXX-XXX-XXXX
phones = ["(555) 123-4567", "555-123-4567", "Call 555-1234", "123-4567"]
# Write validation using re.match
pattern = r"(\d{3}-|\(\d{3}\)\s?)\d{3}-\d{4}"
for phone in phones:    
    match = re.match(pattern, phone)
    if match:
        print(f"{phone} is valid")
    

'''
practice 6_c
'''
# Parse variable assignments (var = value)
assignments = ["x = 10", "name = 'John'", "flag = True", "= invalid", "no equals"]
# Write pattern to match and extract variable name and value
pattern = r'(\w+) = (\S+)'
for assignment in assignments:
    match = re.match(pattern, assignment)
    if match:
        var_name = match.group(1)
        value = match.group(2)
        print(f"{var_name} = {value}")
        
# Pattern should match from start: variable_name = value


'''
using match to validate input formats or parsing structured data is often more efficient than search.
it is also used for command parsing and protocol detection.
match only matches at the start of the string.

findall finds all matches, not just first. non-overlapping only and returns empty list if no match.
used for extracting all emails from text finding all numbers in a string collecting all hastags or
parsing structured data.
no match position information no access to full match when using groups cannot get match object details
'''