def get_file_stats(filename):
    """
    Get statistics about a text file.
    Parameters:
    filename (str): Name of the file to analyze
    Returns:
    dict: Dictionary with 'lines', 'words', and 'characters' counts
    Returns None if file doesn't exist
    Example:
    If file contains:
    "Hello world
    Python is great"
    get_file_stats("file.txt") returns:
    {'lines': 2, 'words': 5, 'characters': 26}
    """
    # YOUR CODE HERE
    # Hint: Use try-except for file handling
    # Hint: Use readlines() to get all lines
    # Hint: Use split() to count words
    # Hint: Use len() for character count
    try:
        with open(filename, 'r') as file:
            # Read all lines
            filename_content = file.readlines()
            # Count lines
            line_count = len(filename_content)
             # Count words (split each line and count)
            word_count = sum(len(line.split()) for line in filename_content)
            # Count characters (total length of all lines)
            char_count = sum(len(line) for line in filename_content)
        return {
            'lines': line_count, # Replace with actual count
            'words': word_count, # Replace with actual count
            'characters': char_count # Replace with actual count
        }
    except FileNotFoundError:
        return None
    
class Student:
    """
    A class to represent a student and their grades.
    """
    def __init__(self, name, student_id):
        """
        Initialize a student with name and ID.
        Start with an empty list of grades.
        Parameters:
        name (str): Student's name
        student_id (str): Student's ID number
        """
        # YOUR CODE HERE
        # Create instance variables for name, student_id, and grades (empty list)
        self.name = name
        self.student_id = student_id
        self.grades = []
        
    def add_grade(self, grade):
        """
        Add a grade to the student's record.
        Only add if grade is between 0 and 100.
        Parameters:
        grade (float): Grade to add
        Returns:
        bool: True if grade was added, False otherwise
        """
        # YOUR CODE HERE
        # Check if 0 <= grade <= 100
        # If yes, append to grades list and return True
        # If no, return False
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        else:
            return False
        
        
    def calculate_average(self):
        """
        Calculate the student's average grade.
        Returns:
        float: Average of all grades
        Returns 0 if no grades exist
        """
        # YOUR CODE HERE
        # Check if grades list is empty
        # If empty, return 0
        # Otherwise, return sum(grades) / len(grades)
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0        
    
    def get_status(self):
        """
        Get student's pass/fail status.
        Returns:
        str: "Passing" if average >= 70, "Failing" otherwise
        "No grades" if no grades recorded
        """
        # YOUR CODE HERE
        if not self.grades:
            return 'No grades'
        average = self.calculate_average()
        if average >= 70:
            return 'Passing'
        else:
            return 'Failing'

def safe_get_element(my_list, index, default_value=None):
    """
    Safely get an element from a list at the given index.
    Parameters:
    my_list: List to access (might not be a list!)
    index: Index to access (might not be valid!)
    default_value: Value to return if access fails
    Returns:
    Element at index if successful
    default_value if any error occurs
    Examples:
    safe_get_element([1, 2, 3], 1, -1) returns 2
    safe_get_element([1, 2, 3], 10, -1) returns -1
    safe_get_element("not a list", 0, -1) returns -1
    safe_get_element([1, 2, 3], "bad", -1) returns -1
    """
    # YOUR CODE HERE
    # Use try-except to handle:
    # - IndexError (index out of range)
    # - TypeError (not a list or bad index type)
    # - Any other unexpected errors
    try:
        # Try to access the element
        if isinstance(my_list, list):
            return my_list[index]
        else:
            raise TypeError
        
    except IndexError:
        # Handle index out of range
        return default_value
    
    except TypeError:
        # Handle wrong types
        return default_value
    
    except Exception:
        # Handle any other error
        return default_value

def recursive_power(x, n):
    """
    Calculate x raised to the power n using recursion.
    Assume n is a non-negative integer.
    Parameters:
    x (float): Base number
    n (int): Exponent (non-negative)
    Returns:
    float: x to the power of n
    Examples:
    recursive_power(2, 3) returns 8 (2*2*2)
    recursive_power(5, 2) returns 25 (5*5)
    recursive_power(10, 0) returns 1 (anything to power 0 is 1)
    recursive_power(3, 1) returns 3
    """
    # YOUR CODE HERE
    # Remember: x^n = x * x^(n-1)
    # Base case: What is x^0?
    # Recursive case: Multiply x by recursive_power(x, n-1)
    # Base case: if n == 0
    if n == 0:
        return 1
    # Recursive case:
    return x * recursive_power(x, n-1)

def analyze_sales(sales_data):
    """
    Analyze sales data using map, filter, and lambda functions.
    Parameters:
    sales_data: List of dictionaries with 'product', 'quantity', 'price'
    Returns:
    Dictionary with:
    - 'total_revenue': Sum of all sales (quantity * price)
    - 'high_value': List of products with revenue > 100
    - 'low_stock': List of products with quantity < 10
    - 'average_price': Average price of all products
    Example:
    sales_data = [
    {'product': 'Widget', 'quantity': 5, 'price': 25.00},
    {'product': 'Gadget', 'quantity': 15, 'price': 10.00},
    {'product': 'Tool', 'quantity': 3, 'price': 50.00}
    ]
    Returns:
    {
    'total_revenue': 425.0,
    'high_value': ['Widget', 'Gadget', 'Tool'],
    'low_stock': ['Widget', 'Tool'],
    'average_price': 28.33
    }
    """
    # Step 1: Calculate revenue for each item
    # Add 'revenue' key to each dictionary
    # Hint: revenue = quantity * price
    with_revenue = list(map(lambda item: {**item, 'revenue': item['quantity'] * item['price']}, sales_data))
    # Step 2: Calculate total revenue
    # YOUR CODE HERE
    # Sum all revenue values
    total_revenue = sum(item['revenue'] for item in with_revenue)
    # Step 3: Filter high-value items (revenue > 100)
    # YOUR CODE HERE
    # Use filter to find items with revenue > 100
    high_value_items = list(filter(lambda item: item['revenue'] > 100, with_revenue)) # Replace with filter
    # Step 4: Filter low-stock items (quantity < 10)
    # YOUR CODE HERE
    low_stock_items = list(filter(lambda item: item['quantity'] < 10, with_revenue)) # Replace with filter
    # Step 5: Calculate average price
    # YOUR CODE HERE
    average_price = sum(item['price'] for item in sales_data) / len(sales_data) # Replace with calculation
    
    return {
    'total_revenue': total_revenue,
    'high_value': [item['product'] for item in high_value_items],
    'low_stock': [item['product'] for item in low_stock_items],
    'average_price': round(average_price, 2) if sales_data else 0
    }
