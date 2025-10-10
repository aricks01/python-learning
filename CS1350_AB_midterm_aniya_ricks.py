import re
"""
Create a shopping cart with these functions:
1. add_item(cart, item_name, price, quantity)
- Add item to cart (or update quantity if exists)
- Price must be positive (> 0)
- Quantity must be positive integer
- Return True if added/updated, False if invalid
2. calculate_total(cart)
- Calculate total cost of all items
- Formula: sum of (price * quantity) for each item
- Return 0 if cart is empty
3. apply_discount(cart, discount_percent)
- Apply discount to all prices (0-100%)
- Example: 20% discount means multiply prices by 0.8
- Return True if valid discount, False otherwise
Example:
cart = {}
add_item(cart, "Apple", 0.50, 6)
add_item(cart, "Bread", 2.00, 2)
print(calculate_total(cart)) # Should print 7.00
apply_discount(cart, 10) # 10% off
print(calculate_total(cart)) # Should print 6.30
"""
    # Write your code here:
def add_item(cart, item_name, price, quantity):
# Your code here
    if quantity <= 0 or price <= 0:
        return False
    if item_name in cart:
        cart[item_name]['quantity'] += quantity
    else:
        cart[item_name] = {'quantity': quantity, 'price': price}
    return True
def calculate_total(cart):
# Your code here
    if cart:
        total = sum(item['quantity']*item['price']for item in cart.values())
        return total
    else:
        return 0
def apply_discount(cart, discount_percent):  
# Your code here
    if discount_percent < 0 or discount_percent > 100:
        return False
    discount = discount_percent / 100
    if cart:
        for item in cart.values():
            item['price'] *= (1.0 - discount)
    return True
# Test your functions
if __name__ == "__main__":
    cart = {}
    # Test adding items
    print(add_item(cart, "Milk", 3.50, 2)) # Should print True
    print(add_item(cart, "Eggs", -1.00, 1)) # Should print False (negative price)
    print(add_item(cart, "Bread", 2.00, 3)) # Should print True
    # Test total
    print(f"Total: ${calculate_total(cart):.2f}")
    # Test discount
    print(apply_discount(cart, 20)) # 20% off
    print(f"After discount: ${calculate_total(cart):.2f}")

"""
Clean and analyze text messages.
Write these functions:
1. clean_message(message)
- Convert to lowercase
- Remove extra spaces (use split and join)
- Remove punctuation at the end (. ! ?)
- Return cleaned message
2. expand_abbreviations(message)
- Replace common abbreviations:
"u" -> "you"
"ur" -> "your"
"r" -> "are"
"thx" -> "thanks"
- Return expanded message
3. count_words(message)
- Split message into words
- Return dictionary with word counts
- Example: "hello world hello" -> {"hello": 2, "world": 1}
4. censor_numbers(message)
- Replace any sequence of digits with "XXX"
- Example: "Call 1234567890" -> "Call XXX"
- Keep other text unchanged
Example:
msg = " Hello WORLD!!! "
clean = clean_message(msg)
print(clean) # "hello world"
msg2 = "thx u r great"
expanded = expand_abbreviations(msg2)
print(expanded) # "thanks you are great"
"""
# Write your code here:
def clean_message(message):
# Your code here
    message = message.lower().strip()
    message = ' '.join(message.split())
    if message and message[-1] in '.!?':
        message = message[:-1]
    return message
def expand_abbreviations(message):
# Your code here
    abbreviations = {
        "u":"you",
        "ur":"your",
        "r":"are",
        "thx":"thanks"
    }
    message = re.sub(r'\b(' + '|'.join(re.escape(key) for key in abbreviations.keys()) + r')\b', lambda match: abbreviations[match.group(0)], message)
    return message
def count_words(message):
# Your code here
    words = message.split()
    words_count = {}
    words_count['total_words'] = len(words)
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    return words_count

def censor_numbers(message):
# Your code here
    message = re.sub(r'\d+', 'XXX', message)
    return message

# Test your functions
if __name__ == "__main__":
    # Test cleaning
    msg1 = " Hello WORLD!!! "
    print(f"Original: '{msg1}'")
    print(f"Cleaned: '{clean_message(msg1)}'")
    # Test abbreviations
    msg2 = "thx for ur help u r awesome"
    print(f"\nOriginal: '{msg2}'")
    print(f"Expanded: '{expand_abbreviations(msg2)}'")
    # Test word count
    msg3 = "hello world hello python world"
    print(f"\nMessage: '{msg3}'")
    print(f"Word counts: {count_words(msg3)}")
    # Test number censoring
    msg4 = "Call me at 5551234567 or 999888777"
    print(f"\nOriginal: '{msg4}'")
    print(f"Censored: '{censor_numbers(msg4)}'")

"""
Validate and extract information using regular expressions.
Write these functions:
1. validate_password(password)
- Must be 8-20 characters long 
- Must contain at least one digit
- Must contain at least one uppercase letter
- Return True if valid, False otherwise
2. extract_hashtags(text)
- Find all hashtags (start with # followed by word characters)
- Example: "#python #coding123" -> ["#python", "#coding123"]
- Return list of hashtags
3. *Bonus* validate_time(time_string)
- Valid format: HH:MM (24-hour format)
- Hours: 00-23, Minutes: 00-59
CS1350_Midterm_v2.md 2025-10-08
12 / 14
- Examples: "14:30" valid, "25:00" invalid
- Return True if valid, False otherwise
4. *Bonus* find_dates(text)
- Find dates in format: MM/DD/YYYY or MM-DD-YYYY
- Example: "Born 01/15/2000" -> ["01/15/2000"]
- Return list of dates found
Example:
print(validate_password("Pass123word")) # True
print(validate_password("weak")) # False
text = "Learning #Python and #DataScience is fun!"
print(extract_hashtags(text)) # ["#Python", "#DataScience"]
"""
import re
# Write your code here:
def validate_password(password):
# Your code here
    if len(password) < 8 or len(password) > 20:
        return False
    pattern = r'\b(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,20}\b'
    return bool(re.match(pattern,password))
    
def extract_hashtags(text):
# Your code here
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    return hashtags
# Bonus
def validate_time(time_string):
# Your code here
    pattern = r'(\d{1,2}):(\d{2})'
    match = re.match(pattern, time_string)
    if match:
        hours, minutes = int(match.group(1)), int(match.group(2))
        if 0<= hours <= 23 and 0 <= minutes <= 59:
            return True
    return False
# Bonus
def find_dates(text):
# Your code here
    pattern = r'\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}'
    match = re.findall(pattern, text)
    return match
    
# Test your functions
if __name__ == "__main__":
    # Test password validation
    passwords = ["Pass1234", "weakpass", "NoDigits!", "12345678", "GoodPass99"]
    for pwd in passwords:
        print(f"Password '{pwd}': {validate_password(pwd)}")
    print()
    # Test hashtag extraction
    text = "Check out #Python3 and #MachineLearning tutorials! #AI #100DaysOfCode"
    hashtags = extract_hashtags(text)
    print(f"Hashtags found: {hashtags}")
    print()
    # Bonus
    # Test time validation
    times = ["14:30", "09:45", "25:00", "12:60", "00:00"]
    for t in times:
        print(f"Time '{t}': {validate_time(t)}")
    print()
    # Bonus
    # Test date finding
    text = "I was born on 12/25/1999 and graduated on 06-15-2021."
    dates = find_dates(text)
    print(f"Dates found: {dates}")
    
"""
Analyze student test scores across multiple exams.
Write functions to:
1. create_score_array(num_students, num_exams)
- Create array of random scores between 60-100
- Shape should be (num_students, num_exams)
- Use np.random.randint(60, 101, size=...)
2. find_struggling_students(scores, threshold)
- Find students whose average is below threshold
- Return array of boolean variables
3. curve_scores(scores, bonus_points)
- Add bonus points to all scores
- Cap maximum score at 100 (use np.minimum)
- Return curved scores array
4. get_exam_statistics(scores)
- Return dictionary with statistics for each exam:
- {"exam_0": {"mean": x, "max": y, "min": z}, ...}
Example:
scores = create_score_array(5, 3) # 5 students, 3 exams
print(scores)
struggling = find_struggling_students(scores, 70)
print(f"Struggling students: {struggling}")
curved = curve_scores(scores, 5) # Add 5 points
print(f"After curve: {curved}")
"""
import numpy as np
# Write your code here:
def create_score_array(num_students, num_exams):
# Your code here
    scores = np.random.randint(60, 101, size=(num_students, num_exams))
    return scores
def find_struggling_students(scores, threshold):
# Your code here
    averages = np.mean(scores, axis = 1)
    struggling = averages < threshold
    return struggling
def curve_scores(scores, points):
# Your code here
    curved = np.minimum(scores + points, 100)
    return curved
def get_exam_statistics(scores):
# Your code here
    stats = {}
    num_exams = scores.shape[1]
    for i in range(num_exams):
        exam_scores = scores[:, i]
        stats[f'exam_{i+1}'] = {
            'mean': np.mean(exam_scores),
            'max': np.max(exam_scores),
            'min': np.min(exam_scores)
        }
    return stats
# Test your functions
if __name__ == "__main__":
    # Create test scores
    scores = create_score_array(6, 4) # 6 students, 4 exams
    print("Original scores:\n", scores)
    # Find struggling students (average < 75)
    struggling = find_struggling_students(scores, 75)
    print(f"\nStruggling students (avg < 75): {struggling}")
    # Curve scores by 5 points
    curved = curve_scores(scores, 5)
    print("\nCurved scores:\n", curved)
    # Get statistics
    stats = get_exam_statistics(scores)
    for exam, data in stats.items():
        print(f"{exam}: mean={data['mean']:.1f}, max={data['max']}, min={data['min']}")

"""
Track student participation in school clubs.
Write these functions:
1. add_student_to_club(clubs_dict, club_name, student_name)
- Add student to a club (create club if doesn't exist)
- clubs_dict is a dictionary where keys are club names
- and values are sets of student names
2. get_students_in_multiple_clubs(clubs_dict)
- Find students who are in 2 or more clubs
- Return a set of student names
3. find_exclusive_members(clubs_dict, club1_name, club2_name)
- Find students in club1 but NOT in club2
- Return empty set if either club doesn't exist
4. *Bonus* merge_clubs(clubs_dict, old_club, new_club)
- Move all students from old_club to new_club
- Remove old_club from dictionary
- Return True if successful, False if old_club doesn't exist
Example:
clubs = {}
add_student_to_club(clubs, "Chess", "Alice")
add_student_to_club(clubs, "Chess", "Bob")
add_student_to_club(clubs, "Drama", "Alice")
add_student_to_club(clubs, "Drama", "Charlie")
print(get_students_in_multiple_clubs(clubs))
# Should print: {"Alice"}
"""
# Write your code here:
def add_student_to_club(clubs_dict, club_name, student_name):
# Your code here
    if club_name not in clubs_dict:
        clubs_dict[club_name] = set()
    clubs_dict[club_name].add(student_name)
    return True
def get_students_in_multiple_clubs(clubs_dict):
# Your code here
    student_count = {}
    for members in clubs_dict.values():
        for student in members:
            student_count[student] = student_count.get(student, 0) + 1
            multiple = {student for student, count in student_count.items() if count >= 2}
    return multiple
def find_exclusive_members(clubs_dict, club1_name, club2_name):
# Your code here
    if club1_name not in clubs_dict or club2_name not in clubs_dict:
        return set()
    exclusive = clubs_dict[club1_name] - clubs_dict[club2_name]
    return exclusive
# Bonus Question
def merge_clubs(clubs_dict, old_club, new_club):
# Your code here
    if old_club not in clubs_dict:
        return False
    if new_club not in clubs_dict:
        clubs_dict[new_club] = set()
        clubs_dict[new_club].update(clubs_dict[old_club])
        clubs_dict.pop(old_club)
        return True
    
# Test your functions
if __name__ == "__main__":
    clubs = {}
    # Add students to clubs
    add_student_to_club(clubs, "Math", "Alice")
    add_student_to_club(clubs, "Math", "Bob")
    add_student_to_club(clubs, "Science", "Alice")
    add_student_to_club(clubs, "Science", "Charlie")
    add_student_to_club(clubs, "Art", "David")
    print("Clubs:", clubs)
    print("In multiple clubs:", get_students_in_multiple_clubs(clubs))
    print("Math only:", find_exclusive_members(clubs, "Math", "Science"))
    # Test merge
    add_student_to_club(clubs, "Photography", "Eve")
    print(merge_clubs(clubs, "Photography", "Art"))
    print("After merge:", clubs)