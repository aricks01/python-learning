import DictionaryOperationsContactManagementSystem as CMS

def test_create_contact():
    """Test contact creation with valid and invalid data."""
    contactData = {
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
    newContact = CMS.add_contact(CMS.contactsDB, contactData)
    print("Addition Successful")
    print(newContact)
    
def test_search_functionality():
    """Test all search functions with various scenarios."""
    contactsDB = CMS.contactsDB
    newContact = CMS.add_contact(contactsDB, {
        'first_name': 'Jane',
        'last_name': 'Dawn',
        'phone': '098-765-4321',
        'email': 'jane.dawn@email.com',
        'address': {
            'street': '123 That St',
            'city': 'Thistown',
            'state': 'ST',
            'zip_code': '09876'
        },
        'category': 'personal',
        'notes': 'John is cool.'

        })
    result = CMS.search_contacts_by_name(contactsDB, 'Jane')
    assert newContact in result
    result = CMS.search_contacts_by_category(contactsDB, 'personal')
    assert newContact in result
    result = CMS.find_contact_by_phone(contactsDB, '098-765-4321')
    assert newContact in result
    print("Search Successful.")

def test_contact_operations():
    """Test add, update, delete operations."""
    contactsDB = CMS.contactsDB
    newContact = CMS.add_contact(contactsDB, {
        'first_name': 'Ben',
        'last_name': 'Franklin',
        'phone': '177-607-0004',
        'email': 'ben.frank@email.com',
        'address': {
            'street': '177 indep st',
            'city': 'Philadelphia',
            'state': 'PA',
            'zip_code': '45678'
        },
        'category': 'work',
        'notes': 'Do not let him near a kite.'
        })
    assert newContact in contactsDB
    update = {'email' : 'benjamin.frank@email.com'}
    CMS.update_contact(contactsDB, newContact, update)
    assert contactsDB[newContact]['email'] == 'benjamin.frank@email.com'
    CMS.delete_contact(contactsDB, newContact)
    if newContact not in contactsDB:
        print("Tests complete.")
    else:
        print("Test failed.")
    
def test_data_analysis():
    """Test statistics and duplicate detection."""
    contactsDB = {}
    newContact = CMS.add_contact(contactsDB, {
        'first_name': 'Jane',
        'last_name': 'Dawn',
        'phone': '177-607-0004',
        'email': 'jane.dawn@email.com',
        'address': {
            'street': '123 That St',
            'city': 'Thistown',
            'state': 'ST',
            'zip_code': '09876'
        },
        'category': 'family',
        'notes': 'John is cool.'

        })    
    newContact2 = CMS.add_contact(contactsDB, {
        'first_name': 'Ben',
        'last_name': 'Franklin',
        'phone': '177-607-0004',
        'email': 'ben.frank@email.com',
        'address': {
            'street': '177 indep st',
            'city': 'Philadelphia',
            'state': 'PA',
            'zip_code': '45678'
        },
        'category': 'work',
        'notes': 'Do not let him near a kite.'
        })
    
    data = CMS.generate_contact_statistics(contactsDB)
    assert data['totalContacts'] == 2
    duplicates = CMS.find_duplicate_contacts(contactsDB)
    assert (newContact in duplicate and newContact2 in duplicate for duplicate in duplicates['phoneDuplicates'])
    print("Test Passed.")
def run_all_tests():
    """Run all test functions and report results."""
    test_create_contact()
    test_search_functionality()
    test_contact_operations()
    test_data_analysis()
    print("\nAll tests passed.")
    
    

print(run_all_tests())