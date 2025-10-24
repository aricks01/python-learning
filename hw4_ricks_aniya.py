import re
import time

def problem1():
    """
    Extract information using regex groups.
    """
    # a) Extract date components from various date formats
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    # TODO: Write a pattern that captures dates in format YYYY-MM-DD
    pattern_iso = r"\d{4}-\d{2}-\d{2}" # Your pattern here
    # TODO: Extract all ISO format dates (YYYY-MM-DD)
    iso_dates = re.findall(pattern_iso, dates_text) # Use re.findall
    # b) Parse email addresses and extract username and domain
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    # TODO: Write pattern with named groups for username and domain
    pattern_email = r"(?P<email>\S+\@\w+\.\w+)" # Use (?P<name>...) syntax
    # TODO: Extract all emails with their components
    email_parts = [] # List of dictionaries with 'username' and 'domain' keys
    for match in re.finditer(pattern_email, emails_text):
        email = match.group('email')
        username, domain = email.split('@')
        email_parts.append({'username': username, 'domain': domain})
    # c) Extract phone numbers with area codes
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    # TODO: Write pattern to capture area code and number separately
    pattern_phone = r"(\(?\d{3}\)?)\s*-*(\d{3}-\d{4})" # Capture area code in group 1, rest in group 2
    # TODO: Extract all phone numbers as tuples (area_code, number)
    phone_numbers = [] # List of tuples
    for match in re.finditer(pattern_phone, phones_text):
        area_code = match.group(1).replace('(', '').replace(')', '')
        number = match.group(2)
        phone_numbers.append((area_code, number))
    # d) Find repeated words in text
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    # TODO: Write pattern to find consecutive repeated words
    pattern_repeated = r"\b(\w+)\b\s+\b\1\b" # Hint: Use backreference \1
    # TODO: Find all repeated words
    repeated_words = [] # List of repeated words (just the word, not the duplicate)
    for match in re.finditer(pattern_repeated, repeated_text, re.IGNORECASE):
        repeated_words.append(match.group(1).lower())
    return {
    'iso_dates': iso_dates,
    'email_parts': email_parts,
    'phone_numbers': phone_numbers,
    'repeated_words': repeated_words
    }
def problem2():
    """
    Use alternation to create flexible patterns.
    """
    # a) Match different file extensions
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    # TODO: Pattern to match image files (jpg, jpeg, png, gif)
    pattern_images = r"\b\w+\.(jpg|jpeg|png|gif)\b" # Use alternation
    # TODO: Find all image filenames
    image_files = [] # Complete filenames with extensions
    for match in re.finditer(pattern_images, files_text):
        image_files.append(match.group(0))
    # b) Match different date formats
    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    # TODO: Pattern to match all three date formats using alternation
    pattern_dates = r"\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\w+ \d{2}, \d{4}" # Match ISO, US, and text formats
    # TODO: Find all dates regardless of format
    all_dates = []
    for match in re.finditer(pattern_dates, mixed_dates):
        all_dates.append(match.group(0))
    # c) Extract prices in different formats
    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    # TODO: Pattern to match prices with different currency symbols
    pattern_prices = r"($|USD |€|£)?\d+\.\d+" # Match $, USD, dollars, €, £
    # TODO: Extract all prices with their currency indicators
    prices = [] # List of matched price strings
    for match in re.finditer(pattern_prices, prices_text):
        prices.append(match.group(0))
    # d) Match programming language mentions
    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    # TODO: Pattern to match language names and their abbreviations
    pattern_langs = r"Python|Java|JavaScript|JS|C++|CPP" # Match full names and common abbreviations
    # TODO: Find all programming language mentions
    languages = [] # Include both full names and abbreviations
    for match in re.finditer(pattern_langs, code_text):
        languages.append(match.group(0))
    return {
    'image_files': image_files,
    'all_dates': all_dates,
    'prices': prices,
    'languages': languages
    }
def problem3():
    """
    Practice with findall() and finditer() methods.
    """
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
    # a) Use findall() to extract all timestamps
    # TODO: Pattern for timestamp [YYYY-MM-DD HH:MM:SS]
    pattern_timestamp = r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2}:\d{2})"
    # TODO: Extract all timestamps
    timestamps = [] # Using findall()
    timestamps = re.findall(pattern_timestamp, log_text)
    # b) Use findall() with groups to extract log levels and messages
    # TODO: Pattern with groups for log level and message
    pattern_log = r"(\w+): (.*)" # Capture level and message separately
    # TODO: Extract tuples of (level, message)
    log_entries = [] # List of tuples using findall()
    log_entries = re.findall(pattern_log, log_text, re.MULTILINE)
    # c) Use finditer() to get positions of all IP addresses
    # TODO: Pattern for IP addresses
    pattern_ip = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" # Match IPv4 addresses
    # TODO: Find all IP addresses with their positions
    ip_addresses = [] # List of dicts with 'ip', 'start', 'end' keys
    for match in re.finditer(pattern_ip, log_text):
        ip_addresses.append({
            'ip': match.group(1),
            'start': match.start(),
            'end': match.end()
        })
    # d) Use finditer() to create a highlighted version of errors
    # TODO: Replace ERROR entries with **ERROR** (highlighted)
    highlighted_log = log_text # Modified version with highlighted errors
    # TODO: Create function to highlight all ERROR entries
    def highlight_errors(text):
        """
        Surround all ERROR log entries with ** markers.
        Return modified text.
        """
        # Your implementation here
        return re.sub(r'ERROR', r'**ERROR**', text)
    highlighted_log = highlight_errors(log_text)
    return {
    'timestamps': timestamps,
    'log_entries': log_entries,
    'ip_addresses': ip_addresses,
    'highlighted_log': highlighted_log
    }
def problem4():
    """
    Practice text transformation using re.sub().
    """
    # a) Clean and format phone numbers
    messy_phones = """
    Contact list:
    - John: 555.123.4567
    - Jane: (555) 234-5678
    - Bob: 555 345 6789
    - Alice: 5554567890
    """
    # TODO: Standardize all phone numbers to format: (555) 123-4567
    def standardize_phones(text):
        """
        Convert all phone number formats to (XXX) XXX-XXXX.
        """
        # Your pattern and substitution here
        pattern = r"\(?\d{3}\)?[.\s-]?\d{3}[.\s-]?\d{4}"
        replacement = r"(XXX) XXX-XXXX"
        return re.sub(pattern, replacement, text)
    cleaned_phones = standardize_phones(messy_phones)
    # b) Redact sensitive information
    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """
    # TODO: Redact SSN and Credit Card numbers
    def redact_sensitive(text):
        """
        Replace SSN with XXX-XX-XXXX and
        Credit Card with XXXX-XXXX-XXXX-XXXX.
        """
        # Your implementation here
        pattern_ssn = r"\b\d{3}-\d{2}-\d{4}\b"
        pattern_cc = r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
        text = re.sub(pattern_ssn, "XXX-XX-XXXX", text)
        text = re.sub(pattern_cc, "XXXX-XXXX-XXXX-XXXX", text)
        return text # Modified text
    redacted_text = redact_sensitive(sensitive_text)
    # c) Convert markdown links to HTML
    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    # TODO: Convert [text](url) to <a href="url">text</a>
    def markdown_to_html(text):
        """
        Convert markdown links to HTML anchor tags.
        """
        # Your pattern and substitution here
        pattern = r'(\[\w+\])\((https?://\w+\.\w{3})\)'
        text = re.sub(pattern, r'<a href="\2">\1</a>', text)
        return text # Modified text
    html_text = markdown_to_html(markdown_text)
    # d) Implement a simple template system
    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values = {
    'name': 'John Smith',
    'order_id': '12345',
    'product': 'Python Book',
    'tracking': 'TRK789XYZ'
    }
    # TODO: Replace {key} with corresponding values
    def fill_template(template, values):
        """
        Replace all {key} placeholders with values from dictionary.
        """
        # Your implementation here
        for key, val in values.items():
            template = re.sub(r'\{' + key + r'\}', val, template)
        return template # Filled template
    filled_template = fill_template(template, values)
    return {
    'cleaned_phones': cleaned_phones,
    'redacted_text': redacted_text,
    'html_text': html_text,
    'filled_template': filled_template
    }

def problem5():
    """
    Use compiled patterns for efficiency and clarity.
    """
    # Create a class to hold compiled patterns
    class PatternLibrary:
        """
        Library of compiled regex patterns for common use cases.
        """
        # TODO: Compile these patterns
        # Use re.IGNORECASE, re.MULTILINE, re.VERBOSE as appropriate
        # a) Email validation pattern (case insensitive)
        EMAIL = re.compile(r"[\w.-]+@[\w.-]+\.\w+", re.IGNORECASE) # re.compile(...)
        # b) URL pattern (with optional protocol)
        URL = re.compile(r"""
                    ^                              # start of string
                    (?:https?://)?                 # optional protocol (http or https)
                    (?:www\.)?                     # optional www.
                    [a-zA-Z0-9.-]+                 # domain name
                    \.[a-zA-Z]{2,}                 # top-level domain
                    $                              # end of string
                """, re.VERBOSE) # re.compile(...)
        # c) US ZIP code (5 digits or 5+4 format)
        ZIP_CODE = re.compile(r"\b\d{5}\b|\b\d{5}-\d{4}\b") # re.compile(...)
        # d) Strong password (verbose pattern with comments)
        # Requirements: 8+ chars, uppercase, lowercase, digit, special char
        PASSWORD =re.compile(r"""
                    ^                      # start of string
                    (?=.*[A-Z])            # at least one uppercase letter
                    (?=.*[a-z])            # at least one lowercase letter
                    (?=.*\d)               # at least one digit
                    (?=.*[!@#$%^&*(),.?":{}|<>_\-\[\]\\;'/+=`~])  # at least one special character
                    .{8,}                  # at least 8 characters long
                    $                      # end of string
                """, re.VERBOSE) # re.compile(..., re.VERBOSE)
        # e) Credit card number (with spaces or dashes optional)
        CREDIT_CARD = re.compile(r"\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?") # re.compile(...)
        # Test your patterns
    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456',
        '1234567890123456']
    }
    # TODO: Validate each item using your compiled patterns
    validation_results = {
        'emails': [], # List of booleans
        'urls': [], # List of booleans
        'zips': [], # List of booleans
        'passwords': [], # List of booleans
        'cards': [] # List of booleans
    }
    # TODO: Implement validation logic
    # For each category, check if pattern matches
    for email in test_data['emails']:
        validation_results['emails'].append(bool(PatternLibrary.EMAIL.fullmatch(email)))
    for url in test_data['urls']:
        validation_results['urls'].append(bool(PatternLibrary.URL.fullmatch(url)))
    for zip_code in test_data['zips']:
        validation_results['zips'].append(bool(PatternLibrary.ZIP_CODE.fullmatch(zip_code)))
    for password in test_data['passwords']:
        validation_results['passwords'].append(bool(PatternLibrary.PASSWORD.fullmatch(password)))
    for card in test_data['cards']:
        validation_results['cards'].append(bool(PatternLibrary.CREDIT_CARD.fullmatch(card)))
       
    return validation_results

def problem6():
    """
    Create a log file analyzer using regex.
    """
    # Sample web server log (Apache/Nginx format)
    log_data = """
        192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 5234
        192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401 234
        192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
        192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
        192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200 1234
        192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200 15234
        192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """
    # TODO: Parse log entries to extract:
    # - IP address
    # - Timestamp
    # - HTTP method (GET, POST, etc.)
    # - URL path
    # - Status code
    # - Response size
    # a) Create pattern to parse log lines
    log_pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) - - \[(.*?)\] "(.*?) (.*? HTTP/1\.\d)" (\d{3}) (\d+)' # Your comprehensive pattern here
    # b) Extract all log entries as structured data
    parsed_logs = [] # List of dictionaries
    for line in log_data.strip().split("\n"):
        match = re.match(log_pattern, line.strip())
        if match:
            ip = match.group(1)
            timestamp = match.group(2)
            method = match.group(3)
            path = match.group(4)
            status = int(match.group(5))
            size = int(match.group(6))
            parsed_logs.append({
                'ip': ip,
                'timestamp': timestamp,
                'method': method,
                'path': path,
                'status': status,
                'size': size
            })
    # c) Analyze the logs
    analysis = {
        'total_requests': 0,
        'unique_ips': [],
        'error_count': 0, # 4xx and 5xx status codes
        'total_bytes': 0,
        'most_requested_path': '',
        'methods_used': [] # Unique HTTP methods
    }
    # TODO: Implement log parsing and analysis
    for log in parsed_logs:
        analysis['total_requests'] += 1
        if log['ip'] not in analysis['unique_ips']:
            analysis['unique_ips'].append(log['ip'])
        if log['status'] >= 400 and log['status'] < 600:
            analysis['error_count'] += 1
        analysis['total_bytes'] = sum([entry['size'] for entry in parsed_logs])
        analysis['methods_used'] = list(set([entry['method'] for entry in parsed_logs]))
    path_counts = {}
    for log in parsed_logs:
        path = log['path']
        if path not in path_counts:
            path_counts[path] = 0
        path_counts[path] += 1
    most_requested = max(path_counts, key=path_counts.get)
    analysis['most_requested_path'] = most_requested
    return {
        'parsed_logs': parsed_logs,
        'analysis': analysis
    }
    
if __name__ == "__main__":
    print("Problem 1 Results:")
    print(problem1())
    print("\nProblem 2 Results:")
    print(problem2())
    print("\nProblem 3 Results:")
    print(problem3())
    print("\nProblem 4 Results:")
    print(problem4())
    print("\nProblem 5 Results:")
    print(problem5())
    print("\nProblem 6 Results:")
    print(problem6())

