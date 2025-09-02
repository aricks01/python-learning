# About Contact Management System
The contact management system is a dictionary-based storage system for contacts. Basic operations can be performed on the contacts such as searching, deleting, and updating. 

The program is run through the user interface and menu options. All of the listed functions are available here.

# Function documentation with examples
def create_contact():
    Main function used in the add_contact function.
    Returns:
    dict: The generated contact dictionary based on user inputs
    Example: {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone': '123-456-7890',
        'email': 'john.doe@email.com',
        'address': {
            'street': '123 Any St',
            'city': 'Anytown',
            'state': 'PL',
            'zip_code': '12345'
        },
        'category': 'personal',
        'notes': 'John is cool.'
        }

def add_contact(contactsDB, contactData):
    Add a new contact to the database.
    Generate unique ID and add contact with proper validation.
    Args:
    contacts_db (dict): The main contacts database
    contact_data (dict): Contact information dictionary
    Returns:
    str: The generated contact ID, or None if addition failed

def display_contact(contactsDB, contactID):
    Display a formatted view of a single contact.
    Args:
    contacts_db (dict): The main contacts database
    contact_id (str): Unique identifier for the contact
    Returns:
    bool: True if contact found and displayed, False otherwise

def list_all_contacts(contactsDB):
    Display a summary list of all contacts (ID, name, phone).
    Args:
    contacts_db (dict): The main contacts database
    Returns:
    A formatted list of all contacts' ID, name, and phone number
    Example: 
    All Contacts:
    contact_01: John Doe 123-456-7890
    contact_02: Jane Doe 098-765-4321

def search_contacts_by_name(contactsDB, searchTerm):
    Search contacts by first or last name (case-insensitive partial match).
    Args:
    contacts_db (dict): The main contacts database
    search_term (str): Name to search for
    Returns:
    dict: Dictionary of matching contacts {contact_id: contact_data}
    Example:{
        'contact_01' : {'first_name': 'John',
                        'last_name': 'Doe',
                        'phone': '123-456-7890',
                        'email': 'john.doe@email.com',
                        'address': {
                            'street': '123 Any St',
                            'city': 'Anytown',
                            'state': 'PL',
                            'zip_code': '12345'
                        },
                        'category': 'personal',
                        'notes': 'John is cool.'}
    }

def search_contacts_by_category(contactsDB, category):
    Find all contacts in a specific category.
    Args:
    contacts_db (dict): The main contacts database
    category (str): Category to filter by
    Returns:
    dict: Dictionary of matching contacts
    Example:{
        'personal' : (['contact_01', 'contact_02'])
    }

def find_contact_by_phone(contactsDB, phoneNumber):
    Find contact by phone number (exact match).
    Args:
    contacts_db (dict): The main contacts database
    phone_number (str): Phone number to search for
    Returns:
    tuple: (contact_id, contact_data) if found, (None, None) if not found

def update_contact(contactsDB, contactID, fieldUpdates):
    Update specific fields of an existing contact.
    Automatically update last_modified timestamp.
    Args:
    contacts_db (dict): The main contacts database
    contact_id (str): Contact to update
    field_updates (dict): Dictionary of fields to update
    Returns:
    bool: True if update successful, False otherwise

def delete_contact(contactsDB, contactID):
    Remove a contact from the database with confirmation.
    Args:
    contacts_db (dict): The main contacts database
    contact_id (str): Contact to delete
    Returns:
    bool: True if deletion successful, False otherwise

def merge_contacts(contactsDB, contactID1, contactID2):
    Merge two contacts using parallel iteration functions, keeping the most recent information.
    Prompt user for conflicts in overlapping fields.
    Args:
    contacts_db (dict): The main contacts database
    contact_id1 (str): First contact ID
    contact_id2 (str): Second contact ID
    Returns:
    str: ID of the merged contact, or None if merge failed

def generate_contact_statistics(contactsDB):
    Generate comprehensive statistics about the contact database.
    Args:
    contacts_db (dict): The main contacts database
    Returns:
    dict: Statistics including:
    - total_contacts: int
    - contacts_by_category: dict
    - contacts_by_state: dict (from address)
    - average_contacts_per_category: float
    - most_common_area_code: str
    - contacts_without_email: int
    Example: {
        total_contacts: 2
        contacts_by_category: {'personal': 1, 'work': 1}
        contacts_by_state: {'PL': 2}
        average_contacts_per_category: 1
        most_common_area_code: '123'
        contacts_without_email: 1
    }


def find_duplicate_contacts(contactsDB):
    Identify potential duplicate contacts based on:
    - Same phone number
    - Same email address
    - Same first+last name combination
    Args:
    contacts_db (dict): The main contacts database
    Returns:
    dict: Dictionary with duplicate types as keys and lists of contact IDs as values
    Example: {
    'phone_duplicates': [['contact_001', 'contact_003']],
    'email_duplicates': [['contact_002', 'contact_005']],
    'name_duplicates': [['contact_001', 'contact_004']]
    }

def export_contacts_by_category(contactsDB, category):
    Export contacts from a specific category as a formatted string.
    Include all contact information in a readable format.
    Args:
    contacts_db (dict): The main contacts database
    category (str): Category to export
    Returns:
    str: Formatted string representation of all contacts in category
    
def main_menu():
    Display and handle the main menu for the contact management system.
    Should include options for:
    1. Add new contact
    2. Search contacts
    3. List all contacts
    4. Update contact
    5. Delete contact
    6. Generate statistics
    7. Find duplicates
    8. Export by category
    9. Exit

def run_contact_manager():
    Main function to run the contact management system.
    Initialize empty database and start the menu loop.

# Known Limitations
The program has known limitations in input validation and accepted tolerance. This could be improved by adding more validation points throughout the program. It is also limited in the amount of contact IDs that it can generate. This can easily be fixed by adjusting the bounds of the number generator.

# Sample Usage Scenarios
This program can be used as a basic storage system for up to 1000 contacts. It is easy to use and will cover most basic needs for contact storage and sorting functions.

#Example of expected program flow
contacts = {}

#Add a contact
contact_1 = add_contact(contactsDB, {
'first_name': 'Alice',
'last_name': 'Johnson',
'phone': '555-123-4567',
'email': 'alice@email.com',
'category': 'work'
})

#Search and display
results = search_contacts_by_name(contactsDB, 'Alice')
for contactID, contactData in results.items():
display_contact(contactsDB, contactID)

#Generate statistics
stats = generate_contact_statistics(contactsDB)
print(f"Total contacts: {stats['totalContacts']}")


