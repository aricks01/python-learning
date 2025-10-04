import re

def format_receipt(items, prices, quantities):
    """
    Create a formatted receipt using string methods.
    Example:
    >>> items = ["Coffee", "Sandwich", "Cookie"]
    >>> prices = [3.50, 8.99, 2.00]
    >>> quantities = [2, 1, 3]
    >>> print(format_receipt(items, prices, quantities))
    """
    #Header Content
    print("="*35)
    print(f"{'Item':<20} {'Qty':>5} {'Price':>8}")
    print("="*35)
    
    #Display items and total in appropriate format
    for item, price, quantity in zip(items, prices, quantities):
        total = price * quantity
        print(f"{item:<20} {quantity:^5} ${total:>8.2f}")
    print("="*35)
    total_amount = sum(price * quantity for price, quantity in zip(prices, quantities))
    print(f"{'TOTAL':<26} ${total_amount:>8.2f}")
    print("="*35)

def process_user_data(raw_data):
    """
    Clean and validate user data using string methods.    
    Example:
    >>> data = {
    ... 'name': ' john DOE ',
    ... 'email': ' JOHN.DOE @EXAMPLE.COM ',
    ... 'phone': '(555) 123-4567',
    ... 'address': '123 main street, apt 5'
    ... }
    """
    
    cleaned_data = {}
    # Clean name
    name = raw_data.get('name', '').strip().title()
    cleaned_data['name'] = name
    # Clean email
    email = raw_data.get('email', '').strip().lower().replace(' ', '')
    cleaned_data['email'] = email
    # Clean phone
    phone = raw_data.get('phone', '').strip().replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    cleaned_data['phone'] = phone
    #Clean address
    address = ' '.join(raw_data.get('address', '').strip().title().split())
    cleaned_data['address'] = address
    # Generate username
    if name:
        first_last = cleaned_data['name'].split()
        username = f"{first_last[0].lower()}_{first_last[-1].lower()}"
    else:
        username = ''
    cleaned_data['username'] = username
    
    #Validation
    validation = {}
    email_suffixes = ['.com', '.org', '.net', '.edu']
    if cleaned_data['email'].find('@') and any(cleaned_data['email'].endswith(suffix) for suffix in email_suffixes):
        validation['email'] = True
    else:
        validation['email'] = False
    if cleaned_data['phone'].isdigit() and len(cleaned_data['phone']) == 10:
        validation['phone'] = True
    else:
        validation['phone'] = False
    if all(char.isalpha() or char.isspace() for char in cleaned_data['name']) and cleaned_data['name']:
        validation['name'] = True
    else:
        validation['name'] = False
    if cleaned_data['address']:
        validation['address'] = True
    else:
        validation['address'] = False
    cleaned_data['validation'] = validation
        
    return cleaned_data #(f"Cleaned Data:\nName: {cleaned_data['name']}\nEmail: {cleaned_data['email']}\nPhone: {cleaned_data['phone']}\nAddress: {cleaned_data['address']}\nUsername: {cleaned_data['username']}\nValidation Results: {cleaned_data["validation"]}")

def analyze_text(text):
    """
    Perform comprehensive text analysis using string methods.
    Example:
    >>> text = '''Hello world! How are you?
    ... This is a test. Another line here!'''
    >>> result = analyze_text(text)
    >>> result['total_words']
    11
    >>> result['questions']
    1
    """

    results = {}
    # Basic counts
    chars = " ".join(text.split())
    total_chars = len(chars)
    results['total_chars'] = total_chars
    words = text.split()
    results['total_words'] = len(words)
    lines = text.splitlines()
    results['total_lines'] = len(lines)
    avg_word_length = round(sum(len(word) for word in words) / len(words), 2)
    
    most_common_word = max((word.lower() for word in words), key=lambda x: sum(1 for word in words if word.lower() == x))
    results['most_common_word'] = most_common_word 
    
    results['avg_word_length'] = avg_word_length
    longest_word = max(words, key=len)
    results['longest_word'] = longest_word
    words_per_line = [len(line.split()) for line in lines]
    results['words_per_line'] = words_per_line
    longest_line = max(lines, key=len)
    results['longest_line'] = longest_line
    
    # Count capitalized sentences
    count = 0
    sentences = re.split(r'[.!?]', chars)
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence[0].isupper():
            count += 1
    capitalized_sentences = count
    results['capitalized_sentences'] = capitalized_sentences
    
    # Count questions and exclamations
    questions = sum(1 for char in chars if char == '?')
    results['questions'] = questions
    exclamations = sum(1 for char in chars if char == '!')
    results['exclamations'] = exclamations
    
    return results #(f"Total Characters: {results['total_chars']}\nTotal Words: {results['total_words']}\nTotal Lines: {results['total_lines']}\nMost Common Word: {results['most_common_word']}\nAverage Word Length: {results['avg_word_length']}\nLongest Word: {results['longest_word']}\nWords Per Line: {results['words_per_line']}\nLongest Line: {results['longest_line']}\nCapitalized Sentences: {results['capitalized_sentences']}\nQuestions: {results['questions']}\nExclamations: {results['exclamations']}")
 
def find_patterns(text):
    """
    Find basic patterns in text using regex.
    Example:
    >>> text = "I have 25 apples and 3.14 pies. HELLO W0RLD!"
    >>> result = find_patterns(text)
    >>> result['integers']
    ['25']
    >>> result['decimals']
    ['3.14']
    >>> result['all_caps_words']
    ['HELLO']
    >>> result['words_with_digits']
    ['W0RLD']
    """
    patterns = {
    'integers': r'\b\d+\b', # Fill in pattern
    'decimals': r'\d*\.\d+', # Fill in pattern
    'words_with_digits': r'\w+\d\w+', # Fill in pattern
    'capitalized_words': r'\b[A-Z][a-z]*\b', # Fill in pattern
    'all_caps_words': r'\b[A-Z][A-Z]+\b', # Fill in pattern
    'repeated_chars': r'(\w)\1+' # Fill in pattern
    }
    
    results = {}
    #Find all pattern matches and add to results dictionary
    for key, pattern in patterns.items():
            results[key] = re.findall(pattern, text)
    return results #(f"Found Patterns:\nIntegers: {results['integers']}\nDecimals: {results['decimals']}\nWords with Digits: {results['words_with_digits']}\nCapitalized Words: {results['capitalized_words']}\nAll Caps Words: {results['all_caps_words']}\nRepeated Characters: {results['repeated_chars']}")

def validate_format(input_string, format_type):
    """
    Validate if input matches specified format using regex.
    Example:
    >>> validate_format("(555) 123-4567", "phone")
    (True, {'area_code': '555', 'prefix': '123', 'line': '4567'})
    >>> validate_format("13/45/2024", "date")
    (False, None)
    """
    # Define patterns for each format type
    patterns = {
    'phone': r'((\D?\d{3}\D?)\s*-*(\d{3})-(\d{4}))', 
    'date': r'(\d{2})/(\d{2})/(\d{4})',
    'time': r'(\d{1,2}):(\d{2})(\s*\w{2})?', 
    'email': r'(\w+\@\w+\.\w+)',
    'url': r'(https?://)([\w.-]+\.\w+[/\w.-]*)', 
    'ssn': r'(\d{3})-(\d{2})-(\d{4})' 
    }
        
    #Retrieve pattern from dictionary with validaton
    pattern = patterns.get(format_type)
    if not pattern:
        return (False, None)
    extracted_parts = {}
    match = re.findall(pattern, input_string)
    #iterate through matches and extract results with indexing
    if match:
        if format_type == 'phone':
            extracted_parts = {
                'area_code': match[0][1],
                'prefix': match[0][2],
                'line': match[0][3]
            }
            return (True, extracted_parts)
        elif format_type == 'date':
            month, day, year = match[0]
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                extracted_parts = {
                    'month': month,
                    'day': day,
                    'year': year
                }
            else:
                pass
        elif format_type == 'time':
            hour, minute, period = match[0]
            if period:
                if 1 <= int(hour) <= 12 and 0 <= int(minute) < 60:
                    extracted_parts = {
                        'hour': hour,
                        'minute': minute,
                        'period': period
                    }
                else:
                    return (False, None)
            else:
                if 0 <= int(hour) < 24 and 0 <= int(minute) < 60:
                    extracted_parts = {
                        'hour': hour,
                        'minute': minute
                    }
                else:
                    return (False, None)
        elif format_type == 'email':
            extracted_parts = {
                'email': match[0]
            }
        elif format_type == 'url':
            extracted_parts = {
                'protocol': match[0][0],
                'domain': match[0][1]
            }
        elif format_type == 'ssn':
            extracted_parts = {
                'part1': match[0][0],
                'part2': match[0][1],
                'part3': match[0][2]
            }
        return (True, extracted_parts)
    else:
        return (False, None)

def extract_information(text):
    """    
    Example:
    >>> text = 'The price is $19.99 (20% off). "Great deal!" she said.'
    >>> result = extract_information(text)
    """
    patterns = {
    'prices': r'(\$(\d{1,3},)*\d{1,3}+\.\d{2})', # Fill in pattern
    'percentages': r'(\d+(\.\d+)?\%)', # Fill in pattern
    'years': r'(\b(19|20)\d{2}\b)', # Fill in pattern
    'sentences': r'([A-Z][^.?!]*(?:\.\d+)*[^.?!]*[.?!])', # Fill in pattern
    'questions': r'([A-Z][^.?!]*\?)', # Fill in pattern
    'quoted_text': r'"(.*?)"' # Fill in pattern
    }
    
    results = {}
    for key, pattern in patterns.items():
            results[key] = re.findall(pattern, text)
            if key in ['prices', 'percentages', 'years']:
                results[key] = [match[0] for match in results[key]]
            elif key == ['quoted_text', 'questions', 'sentences']:
                results[key] = [match for match in results[key]]   
                
    return results #(f"Extracted Information:\nPrices: {results['prices']}\nPercentages: {results['percentages']}\nYears: {results['years']}\nSentences: {results['sentences']}\nQuestions: {results['questions']}\nQuoted Text: {results['quoted_text']}")
    
def clean_text_pipeline(text, operations):
    """
    >>> text = " Hello WORLD! Visit https://example.com "
    >>> ops = ['trim', 'lowercase', 'remove_urls', 'remove_extra_spaces']
    >>> result = clean_text_pipeline(text, ops)
    >>> result['cleaned']
    'hello world! visit'
    """         
    steps = []
    cleaned = text
    
    #Iterate through operations
    for op in operations:
                
        if op == "trim":
            cleaned = cleaned.strip()
        
        elif op == "lowercase":
            cleaned = cleaned.lower()
            
        elif op == "remove_emails":
            cleaned = re.sub(r"\b[\w\.+-]+@[\w\.-]+\.\w+\b", "", cleaned)
        
        elif op == "remove_punctuation":
            cleaned = re.sub(r'[.!?]', '', cleaned)
        
        elif op == "remove_digits":
            cleaned = re.sub(r"\d", "", cleaned)
        
        elif op == "remove_extra_spaces":
            cleaned = " ".join(cleaned.split())
                    
        elif op == "remove_urls":
            cleaned = re.sub(r"http[s]?://\S+", "", cleaned)    
        
        elif op == "capitalize_sentences":
            # Capitalize first letter of each sentence
            cleaned = re.sub(
                r'(^|[.!?]\s+)([a-z])',
                lambda m: m.group(1) + m.group(2).upper(),
                cleaned
            )
        steps.append((op, cleaned))
    return {
        'original' : text,
        'cleaned' : cleaned,
        'steps' : steps
    }
        
def smart_replace(text, replacements):
    """
    text = "Call me at (555) 123-4567.    I'm busy. email@example.com I have 2 dogs! "
    rules = {'censor_phone', 'expand_contractions', 'fix_spacing', 'number_to_word', 'censor_email'}
    print(smart_replace(text, rules))
    """
    # Define contractions dictionary
    contractions = {
    "don't": "do not",
    "won't": "will not",
    "can't": "cannot",
    "I'm": "I am",
    "you're": "you are",
    "it's": "it is",
    "he's": "he is",
    "she's": "she is",
    "we're": "we are",
    "they're": "they are",
    "I've": "I have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have"
    }

    # Apply replacements based on rules
    if replacements.get('censor_phone'):
        text = re.sub(r'(\d{3}-|\(\d{3}\)\s?)\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
    if replacements.get('censor_email'):
        text = re.sub(r'\b[\w\.+-]+@[\w\.-]+\.\w+\b', '[EMAIL]', text)
    if replacements.get('fix_spacing'):
        text = re.sub(r'\s*([\.!?,;:])\s*', r'\1 ', text).strip()
    if replacements.get('expand_contractions'):
        text = re.sub(r'\b(' + '|'.join(re.escape(key) for key in contractions.keys()) + r')\b', lambda match: contractions[match.group(0)], text)
    if replacements.get('number_to_word'):
        text = re.sub(r'\b([0-9])\b', lambda match: ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][int(match.group(0))], text)
    return text
    
def analyze_log_file(log_text):
    """
    Analyze a simplified log file format using string methods and regex.
    Log format: [YYYY-MM-DD HH:MM:SS] LEVEL: Message
    Example: [2024-01-15 10:30:45] ERROR: Database connection failed
    Example:
    >>> log = '''[2024-01-15 10:30:45] ERROR: Connection failed
    ... [2024-01-15 10:31:00] INFO: Retry attempt 1
    ... [2024-01-15 11:00:00] WARNING: High memory usage'''
    >>> result = analyze_log_file(log)
    >>> result['error_count']
    >>> result['dates']
    ['2024-01-15']
    """
    #Structure for future operations in results dictionary
    log_entries = log_text.splitlines()
    time_range = sorted(re.findall(r'\d{4}-\d{2}-\d{2} (\d{2}:\d{2}:\d{2})', log_text))
    if time_range:
        time_range = (time_range[0], time_range[-1])        
    else:
        time_range = (None, None)
    most_active_hour = re.findall(r'\d{4}-\d{2}-\d{2} (\d{2}):\d{2}:\d{2}', log_text)
    if most_active_hour:
        most_active_hour = max(set(most_active_hour), key=most_active_hour.count)
        most_active_hour = int(most_active_hour)        
    else:
        most_active_hour = None
    
    results = {
        'total_entries': len(log_entries),
        'error_count': sum(1 for entry in log_entries if 'ERROR' in entry),
        'warning_count': sum(1 for entry in log_entries if 'WARNING' in entry),
        'info_count': sum(1 for entry in log_entries if 'INFO' in entry),
        'dates': sorted(set(re.findall(r'(\d{4}-\d{2}-\d{2})', log_text))),
        'error_messages': [re.search(r'ERROR:\s*(.*)', entry).group(1) for entry in log_entries if 'ERROR' in entry],
        'time_range': time_range,
        'most_active_hour': most_active_hour
    }
    return results

def run_tests():
    """Test all functions with sample data."""
    print("="*50)
    print("Testing Part 1: String Methods")
    print("="*50)
    # Test 1.1: Receipt formatting
    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    receipt = format_receipt(items, prices, quantities)
    print("Receipt Test:")
    print(receipt)
    # Test 1.2: User data processing
    test_data = {
        'name': ' john DOE ',
        'email': ' JOHN@EXAMPLE.COM ',
        'phone': '(555) 123-4567',
        'address': '123 main street'
    }
    cleaned = process_user_data(test_data)
    print(f"\nCleaned name: {cleaned.get('name', 'ERROR')}")
    print(f"Cleaned email: {cleaned.get('email', 'ERROR')}")
    print("\n" + "="*50)
    print("Testing Part 2: Regular Expressions")
    print("="*50)
    # Test 2.1: Pattern finding
    test_text = "I have 25 apples and 3.14 pies"
    patterns = find_patterns(test_text)
    print(f"Found integers: {patterns.get('integers', [])}")
    print(f"Found decimals: {patterns.get('decimals', [])}")
    # Test 2.2: Format validation
    phone_valid, phone_parts = validate_format("(555) 123-4567", "phone")
    print(f"\nPhone validation: {phone_valid}")
    if phone_parts:
        print(f"Extracted parts: {phone_parts}")
    # Test 2.3: Information extraction
    info_text = 'The price is $19.99 (20% off).'
    info = extract_information(info_text)
    print(f"\nPrices found: {info.get('prices', [])}")
    print(f"Percentages found: {info.get('percentages', [])}")
    print("\n" + "="*50)
    print("Testing Part 3: Combined Operations")
    print("="*50)
    # Test 3.1: Cleaning pipeline
    dirty_text = " Hello WORLD! "
    operations = ['trim', 'lowercase', 'remove_extra_spaces']
    cleaned_result = clean_text_pipeline(dirty_text, operations)
    print(f"Original: '{cleaned_result.get('original', '')}'")
    print(f"Cleaned: '{cleaned_result.get('cleaned', '')}'")
    print("\n" + "="*50)
    print("Testing Part 4: Log Analysis")
    print("="*50)
    # Test 4.1: Log analysis
    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
    [2024-01-15 10:31:00] INFO: Retry attempt
    [2024-01-15 10:32:00] WARNING: Timeout warning"""
    log_analysis = analyze_log_file(sample_log)
    print(f"Total entries: {log_analysis.get('total_entries', 0)}")
    print(f"Error count: {log_analysis.get('error_count', 0)}")
    print(f"Unique dates: {log_analysis.get('dates', [])}")
    print("\n" + "="*50)
    print("All tests completed!")
    print("="*50)
if __name__ == "__main__":
    run_tests()