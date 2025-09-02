import time
import datetime
import random

contactData = {}
contactsDB = {}


def create_contact():
    currentTime = datetime.datetime.now()
    customTime = currentTime.strftime("%Y-%d-%m")

    #collect information for new contact
    firstName = (input("Enter first name: "))
     #validate input
    while len(firstName) == 0:
        print("Invalid input")
        firstName = (input("Enter first name: "))
    lastName = (input("Enter last name: "))
     #validate input
    while len(lastName) == 0:
        print("Invalid input")
        lastName = (input("Enter last name: "))
    phoneNum = (input("Enter phone number (use format xxx-xxx-xxxx): "))
    #validate input
    while len(phoneNum) == 0:
        print("Invalid input")
        phoneNum = (input("Enter phone number (use format xxx-xxx-xxxx): "))
    emailAddress = (input("Enter email address: "))
    streetAddress = (input("Enter street address: "))
    cityName = (input("Enter city name: "))
    stateName = (input("Enter state abbreviation (ex. TX): "))
    zipCode = (input("Enter zip code: "))
    categoryType = (input("Enter category type (personal, work, family): "))
    meetingNotes = (input("Enter any notes: "))
    creationDate = customTime
    modifiedDate = customTime
    
    #format contact information
    contact = {
    'first_name': firstName,
    'last_name':lastName,
    'phone': phoneNum,
    'email': emailAddress,
    'address': {
    'street': streetAddress,
    'city': cityName,
    'state': stateName,
    'zip_code': zipCode
    },
    'category': categoryType, # 'personal', 'work', 'family'
    'notes': meetingNotes,
    'created_date': creationDate,
    'last_modified': modifiedDate
    }
    
    return contact

def add_contact(contactsDB, contactData):
      
    #newContact = create_contact()
    contactID = str(random.randint(0,1000))
    newContact = contactData
    #contactData = newContact
    contactsDB['contact_'+ contactID] = contactData
    if contactID not in contactsDB:
        contactData = newContact
        return 'contact_'+ contactID
    else:
        return "Addition failed. None."
    
def display_contact(contactsDB, contactID):
    contactID = str(input("Enter your contact ID: "))
    if contactID in contactsDB:
        print(f"Contact data:{contactsDB[contactID]}")
        return True
    else:
        print("Invalid ID")
        return False
    
def list_all_contacts(contactsDB):
    if len(contactsDB) == 0:
        print("No contacts to display")
        return
    else:
        print("All Contacts:\n")
        #maybe use dict.items()
        for contactID in contactsDB:
            contact = contactsDB[contactID]
            name = contact.get('first_name') + " " + contact.get('last_name')
            print(contactID, ":", name, " ", contact['phone'], "\n")
    
def search_contacts_by_name(contactsDB, searchTerm):
    results = {}
    searchTerm = searchTerm.lower()
    for contactID in contactsDB:
        contact = contactsDB[contactID]
        firstName = contact['first_name'].lower()
        lastName = contact['last_name'].lower()
        if searchTerm in firstName or searchTerm in lastName:
            results[contactID] = contact
    if results != {}:
        return results
    else:
        return None

def search_contacts_by_category(contactsDB, category):
    results = {}
    for contactID in contactsDB:
        contact = contactsDB[contactID]
        if contact['category'].lower() == category.lower():
            results[contactID] = contact
    if results != {}:    
        return results
    else:
        return None

def find_contact_by_phone(contactsDB, phoneNumber):
    for contactID in contactsDB:
        contact = contactsDB[contactID]
        if contact['phone'] == phoneNumber:
            return (contactID, contactsDB[contactID])
    else:
        return (None, None)

def update_contact(contactsDB, contactID, fieldUpdates):
    currentTime = datetime.datetime.now()
    customTime = currentTime.strftime("%Y-%d-%m")
    if contactID not in contactsDB:
        print("Contact not found.")
        return False
    contact = contactsDB[contactID]
    for key in fieldUpdates:
        if key == 'address':
            for addressKey in fieldUpdates['address']:
                contact['address'][addressKey] = fieldUpdates['address'][addressKey]
        else:
            contact[key] = fieldUpdates[key]
    contact['last_modified'] = customTime
    print("Update successful.")
    return True

def delete_contact(contactsDB, contactID):
    if contactID in contactsDB:
        contactID = contactsDB.pop(contactID)
        print(f"Removed contact: {contactID}")
        return True
    else:
        print("Invalid contact ID")
        return False
        
def merge_contacts(contactsDB, contactID1, contactID2):
    contactID1 = contactsDB[contactID1]
    contactID2 = contactsDB[contactID2]
    allKeys = set(contactID1.keys()) | set(contactID2.keys())
    newContact = {}
    
    for key in allKeys:
        val1 = contactID1.get(key, 'MISSING')
        val2 = contactID2.get(key, 'MISSING')
        
        if val1 == 'MISSING':
            newContact[key] = f"{val2}"
        elif val2 == 'MISSING':
            newContact[key] = f"{val1}"
        elif val1 == val2:
            newContact[key] = f"{val1}"
        else:
            newContact[key] = f"{val1}, {val2}"
            
    newContactID = str(random.randint(0,1000))
    contactsDB["contact_" + newContactID] = newContact
    return "Your new contact ID is contact_" + newContactID
    
def generate_contact_statistics(contactsDB):
    from collections import Counter
    statistics = {
        'totalContacts' : len(contactsDB),
        'contactsByCategory' : {},
        'contactsByState' : {},
        'averageContactsPerCategory' : 0.0,
        'mostCommonAreaCode' : ' ',
        'contactsWithoutEmail' : 0
    }
    if len(contactsDB) == 0:
       return statistics
   
    categoryCounter = Counter()
    stateCounter = Counter()
    areaCodes = []
    noEmailCount = 0
    
    for contactData in contactsDB.values():
        categoryCounter[contactData['category'].lower()] +=1
        stateCounter[contactData['address']['state']] += 1
        if "-" in contactData['phone']:
            areaCode = contactData['phone'].split('-')[0]
            areaCodes.append(areaCode)
        if len(contactData['email']) == 0:
            noEmailCount += 1
        
    statistics['contactsByCategory'] = dict(categoryCounter)
    statistics['contactsByState'] = dict(stateCounter)
    statistics['averageContactsPerCategory'] = round(len(contactsDB) / len(categoryCounter), 2)
    statistics['contactsWithoutEmail'] = noEmailCount
    if areaCodes != []:        
        statistics['mostCommonAreaCode'] = Counter(areaCodes).most_common(1)[0][0]
    return statistics  

def find_duplicate_contacts(contactsDB):
    duplicatesDB = {
        'phoneDuplicates' : [],
        'emailDuplicates' : [],
        'nameDuplicates' : []
    }
    
    phones = {}
    emails = {}
    names = {}
    
    for contactID, contactData in contactsDB.items():
        phoneNum = contactData['phone']
        email = contactData['email']
        firstName = contactData['first_name'].lower()
        lastName = contactData['last_name'].lower()
        name = firstName, lastName
        if phoneNum in phones:
            duplicatesDB['phoneDuplicates'].append(([phones[phoneNum]], contactID))
        else:
            phones[phoneNum] = contactID
        if email in emails:
            duplicatesDB['emailDuplicates'].append(([emails[email]], contactID))
        else:
            emails[email] = contactID
        if name in names:
            duplicatesDB['nameDuplicates'].append(([names[name]], contactID))
        else:
            names[name] = contactID
    return duplicatesDB
    
def export_contacts_by_category(contactsDB, category):
    if len(contactData['category']) == 0:
        print("no category found")
        
    for contactID, contactData in contactsDB.items():
        if contactData['category'].lower() == category.lower():
            print(category + " Contacts \n ------------")
            print("Contact ID: ", contactID)
            firstName = contactData['first_name']
            lastName = contactData['last_name']
            name = firstName + " " + lastName
            print("Name: ", name)
            phone = contactData['phone']
            print("Phone Number: ", phone)
            email = contactData['email']
            print("Email: ", email)
            #street state city zip
            address = contactData['address']['street'], contactData['address']['state'], contactData['address']['city'], contactData['address']['zip_code']
            print("Address: ", address)
            print("\n ------------")
        else:
            print("No contacts found in category ", category)
        
def main_menu():
    print("----Main Menu Options----")
    print("1. Add new contact")
    print("2. Search contacts")
    print("3. List all contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Generate statistics")
    print("7. Find duplicates")
    print("8. Export by category")
    print("9. Exit")
    choice = input("Please select a menu option *number only: ")
    return choice

def run_contact_manager():
    options = ['1','2','3','4','5','6','7','8','9']
    choice = main_menu()
    while True:
        if choice not in options:
            print("Invalid entry.")
            return run_contact_manager()
        else:
            if choice == "1":
                newContact = add_contact(contactsDB, contactData)
                print(newContact)
                time.sleep(1)
                return run_contact_manager()
            elif choice == "2":
                select = input("1. Search by name\n2. Search by category\n3. Search by phone\nPlease select a menu option *number only: ")
                if select == "1":
                    #search by name logic
                    searchTerm = input("Enter your search term: ")
                    print(search_contacts_by_name(contactsDB, searchTerm))
                    time.sleep(1)
                    return run_contact_manager()
                elif select == "2":
                    #search by category logic
                    category = input("Enter a category: ")
                    print(search_contacts_by_category(contactsDB, category))
                    time.sleep(1)
                    return run_contact_manager()
                elif select == "3":
                    #search by phone logic
                    phoneNumber = input("Enter a phone number: ")
                    print(find_contact_by_phone(contactsDB, phoneNumber))
                    time.sleep(1)
                    return run_contact_manager()
            elif choice == "3":
                contacts = list_all_contacts(contactsDB)
                print(contacts)
                time.sleep(1)
                return run_contact_manager()
            elif choice == "4":
                contactID = input("Enter a contact ID: ")
                fieldUpdates = {} 
                key = input("Enter a field to update (first_name, last_name, phone, email, address, category, notes): ")
                if key == 'address':
                    addressField = input("Enter which address field to update (street, city, state, zip_code): ")
                    value = input("Enter new value: ")
                    fieldUpdates['address'] = {}
                    fieldUpdates['address'][addressField] = value
                else:
                    value = input("Enter new value: ")
                    fieldUpdates[key] = value
                update_contact(contactsDB, contactID, fieldUpdates)
                display_contact(contactsDB, contactID)
                time.sleep(1)
                return run_contact_manager()
            elif choice == "5":
                contactID = input("Enter a contact ID: ")
                print(delete_contact(contactsDB, contactID))
                time.sleep(1)
                return run_contact_manager()
            elif choice == "6":
                stats = generate_contact_statistics(contactsDB)
                print(stats)
                time.sleep(1)
                return run_contact_manager()
            elif choice == "7":
                print(find_duplicate_contacts(contactsDB))
                time.sleep(1)
                return run_contact_manager()
            elif choice == "8":
                category = input("Enter a category: ")
                print(export_contacts_by_category(contactsDB, category))
                time.sleep(1)
                return run_contact_manager()
            elif choice == "9":
                print("Exiting menu.")
                return False


#finish testing & debugging the menu options. Specifically, exporting by category, generating statistics, and updating contact.

#updating contact is working for all but address. finish figuring out formatting within the address dictionary




    




