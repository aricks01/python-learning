def practice_1_beginner():
    """
    Beginner: Convert text to CSV
    """
    print("\n" + "="*50)
    print("EXERCISE 1.1: Text to CSV Converter")
    print("="*50)
    # Create a text file with data
    with open("employees.txt", "w") as employees:
        employees.write("John Smith 35 Engineer\n")
        employees.write("Jane Doe 28 Designer\n")
        employees.write("Bob Johnson 42 Manager\n")
        # TODO 1: Read text file and convert to CSV
    with open("employees.txt", "r") as employees:
        with open("employees.csv", "w") as employees_csv:
            # Write CSV header
            employees_csv.write("First,Last,Age,Job\n")
            # TODO: Read each line and convert                        
            for line in employees:
                parts = line.strip().split()
                print(parts)
                # parts[0] = first name, parts[1] = last name, etc.
                # TODO: Write as CSV line
                # Format: John,Smith,35,Engineer
                csv_line = employees_csv.write(parts[0] + "," + parts[1] + "," + parts[2] + "," + parts[3] + "\n") # Replace with comma-separated values
    # TODO 2: Read and verify CSV
    print("\nCSV Contents:")
    with open("employees.csv", "r") as employees_csv:
        # TODO: Read and display
        for line in employees_csv:
            print(line)
            
def practice_1_intermediate():
    """
    Intermediate: Process CSV data
    """
    print("\n" + "="*50)
    print("EXERCISE 1.2: Grade Calculator")
    print("="*50)
    # Create grades CSV
    with open("grades.csv", "w") as grades:
        grades.write("Student,Math,Science,English\n")
        grades.write("Alice,95,87,92\n")
        grades.write("Bob,78,85,88\n")
        grades.write("Charlie,92,94,85\n")
        grades.write("Diana,88,91,95\n")
    # TODO 1: Read CSV and calculate averages
    with open("grades.csv", "r") as grades:
        header = grades.readline().strip().split(",")
        print(f"Subjects: {header[1:]}")
        student_averages = []
        for line in grades:
            parts = line.strip().split(",")
            name = parts[0]
            # TODO: Convert grades to numbers
            grades = [] # Convert parts[1:] to integers
            for grade in parts[1:]:
                grades.append(int(grade))
            # TODO: Calculate average
            average = sum(grades)/len(grades) # Calculate average grade
            student_averages.append((name, average))
            print(f"{name}: {average:.1f}")
    # TODO 2: Save results to new CSV
    with open("averages.csv", "w") as averages:
        averages.write("Student,Average\n")
        # TODO: Write each student's average
        for name, avg in student_averages:
            averages.write(f"{name}: {avg:.1f}") # Write to file

def practice_1_advanced():
    """
    Advanced: JSON database system
    """
    print("\n" + "="*50)
    print("EXERCISE 1.3: JSON Database")
    print("="*50)
    import json
    # TODO 1: Create a product database in JSON
    products = {
        "inventory": [
            {"id": 1, "name": "Laptop", "price": 999.99, "stock": 5},
            {"id": 2, "name": "Mouse", "price": 29.99, "stock": 15},
            {"id": 3, "name": "Keyboard", "price": 79.99, "stock": 8}
        ],
        "last_updated": "2024-01-15",
        "store": "Tech Store"
    }
    # TODO: Save to JSON
    with open("products.json", "w") as products_file:
        json.dump(products, products_file, indent=2)
    print("Product database created")
    # TODO 2: Load and modify JSON
    with open("products.json", "r") as products_file:
        loaded_data = json.load(products_file)
    # Add a new product
    new_product = {
        "id": 4,
        "name": "Monitor",
        "price": 299.99,
        "stock": 3
    }
    # TODO: Add to inventory
    loaded_data['inventory'].append(new_product)
    # TODO 3: Update stock levels
    loaded_data['inventory'][3]['stock'] += 10 
        
    # TODO 4: Save updated data
    with open("products.json", "w") as products_file:
        # TODO: Save the modified data
        json.dump(loaded_data, products_file)
    # TODO 5: Generate report from JSON
    print("\nUpdated Inventory")
    with open("products.json", "r") as products_file:
        final_data = json.load(products_file)
        for item in final_data['inventory']:
            print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}, Stock: {item['stock']}")
# Run the exercise
practice_1_advanced()