# TODO: Create Person class with private _age
class Person:
    def __init__(self, name, age):
        self.name = name # Public
        self._age = age # Make age private
    def get_age(self):
    # Return the private age
        return self._age
# Test:
#person = Person("Bob", 25)
#print(person.get_age()) # Should print 25
# person._age = -5 # We shouldn't do this!

# TODO: Add set_age() with validation
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def get_age(self):
        return self._age
    def set_age(self, new_age):
    # Only allow age between 0 and 150
    # Print error if invalid
        if new_age < 0 or new_age > 150:
            print("Error: Invalid age.")
            return False
        else:
            self._age = new_age
            return True
# Test:
person = Person("Alice", 25)
print(person.set_age(30))
print(person.set_age(-5)) # Should print error


# TODO: Store SSN privately, show only last 4 digits
class Person:
    def __init__(self, name, ssn):
        self.name = name
        self._ssn = ssn # Store SSN privately
    def get_masked_ssn(self):
        # Return like: ***-**-6789
        return "***-**-" + self._ssn[-4:]
    def verify_ssn(self, ssn_to_check):
        # Return True if matches stored SSN
        if ssn_to_check == self._ssn:
            return True
        else:
            return False
ssn = "123-45-6789"
person = Person("Bob", ssn)
print(person.get_masked_ssn())
print(person.verify_ssn("098-76-5432"))

# TODO: Make area a property (calculated)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
    # Calculate and return area
        return self.width * self.height     
# Test:
rect = Rectangle(5, 3)
print(rect.area) # Should print 15 (no parentheses!)

# TODO: Extract domain from email
class Email:
    def __init__(self, address):
        self.address = address
    @property
    def username(self):
    # Return part before @
        return self.address.split("@")[0]
    @property
    def domain(self):
    # Return part after @
        return self.address.split("@")[1]
# Test:
email = Email("alice@gmail.com")
print(email.username) # alice
print(email.domain) # gmail.com

# TODO: Calculate age from birthdate
from datetime import datetime
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    @property
    def age(self):
    # Calculate age from birth_year
    # Use datetime.now().year
        current = datetime.now().year
        return current - self.birth_year
    @property
    def can_vote(self):
    # Return True if age >= 18
        if self.age >= 18:
            return True
        else:
            return False
# Test:
person = Person("Bob", 2000)
print(f"Age: {person.age}")
print(f"Can vote: {person.can_vote}")

# TODO: Create Score class (0-100 range)
class Score:
    def __init__(self, value=0):
        self._value = 0
        self.value = value # Use setter
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        # Check if between 0 and 100
        # Set if valid, print error if not
        if new_value >= 0 and new_value <= 100:
            self._value = new_value
            print("Score updated to", new_value)
            return True
        else:
            print("Error: Score must be between 0 and 100.")
            return False
            
# Test:
score = Score(85)
score.value = 95 # Should work
score.value = 105 # Should print error

# TODO: Username with format checking
class Username:
    def __init__(self, name):
        self._name = ""
        self.name = name
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
    # Check: 3-20 characters
    # Check: only letters, numbers, underscore
    # Set if valid
        if len(value) < 3 or len(value) > 20:
            print("Error")
            return False
        for char in value:
            if not (char.isalnum() or char == "_"):
                print("Error")
                return False
# Test:
user = Username("alice_123") # Should work
user.name = "ab" # Too short
user.name = "alice@123" # Invalid character

# TODO: Password with strength requirements
class Password:
    def __init__(self):
        self._value = None
    @property
    def value(self):
        # Never show actual password!
        return "*" * len(self._value) if self._value else None
    @value.setter
    def value(self, password):
        # Check: at least 8 characters
        # Check: has uppercase
        # Check: has lowercase
        # Check: has number
        # Store if valid
        if len(password) < 8:
            print("Error: Too short")
            return False
        if not any(c.isupper() for c in password):
            print("Error: Must have uppercase")
            return False
        if not any(c.islower() for c in password):
            print("Error: must have lowercase")
            return False
        if not any(c.isdigit() for c in password):
            print("Error: must have number")
            return False
        if not False:
            self._value = password
            print("Password set")
            return True
    def verify(self, password):
        # Check if matches stored password
        if password == self._value:
            return True
        else:
            return False
        
passwd = Password()
passwd.value = "abcdABCD123"
print(passwd.value)
print(passwd.verify("abcdABCD123"))

# TODO: Override area calculation
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0 # Base shape has no area
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
    # Override to return width * height
        return self.width * self.height
# Test:
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")

# TODO: Different grading for different students
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def calculate_grade(self):
    # Regular grading
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        else: return "F"
class HonorsStudent(Student):
    def calculate_grade(self):
    # Harder grading for honors
    # A: 95+, B: 85+, C: 75+
        if self.score >= 95: return "A"
        elif self.score >= 85: return "B"
        elif self.score >= 75: return "C"
        else: return "F"
# Test both student types
student = Student("Bob", 88)
honors = HonorsStudent("Bill", 95)
print(f"{student.name} grade: {student.calculate_grade()}")
print(f"{honors.name} grade: {honors.calculate_grade()}")

# TODO: Combat system with different character types
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
    def attack(self):
        return 10 # Base damage
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage!")
class Warrior(Character):
    def attack(self):
    # Warriors do 2x damage
        return super().attack() * 2
    def take_damage(self, amount):
    # Warriors have armor, reduce damage by 3
        reduced_damage = max(0, amount - 3)
        super().take_damage(reduced_damage)
class Mage(Character):
    def __init__(self, name, health, mana):
    # Initialize parent AND mana
        super().__init__(name, health)
        self.mana = mana
    def attack(self):
    # If has mana, do 3x damage, else normal
        if self.mana:
            return super().attack() * 3
        else:
            return super().attack()
# Test combat
warrior = Warrior("Thor", 100)
mage = Mage("Gandalf", 80, 10)
damage = warrior.attack()
mage.take_damage(damage)
damage = mage.attack()
warrior.take_damage(damage)
print(f"{warrior.name} health: {warrior.health}")
print(f"{mage.name} health: {mage.health}")

# TODO: Extend Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def accelerate(self):
        self.speed += 10
        print(f"Speed: {self.speed} mph")
class SportsCar(Car):
    def __init__(self, brand, model, year, turbo):
        # Call parent init
        # Add turbo attribute
        super().__init__(brand, model, year)
        self.turbo = turbo
    def accelerate(self):
        # If turbo, speed += 20, else normal
        if self.turbo:
            self.speed += 20
            return self.speed
        else:
            return self.speed
# Test:
ferrari = SportsCar("Ferrari", "488", 2023, True)
print(ferrari.accelerate())

# TODO: Student hierarchy
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.gpa = 0.0
    def enroll(self, course):
        self.courses.append(course)
        print(f"Enrolled in {course}")
class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        # Initialize parent
        # Add thesis_topic
        # Add advisor attribute (starts None)
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
        self.advisor = None
    def set_advisor(self, advisor_name):
        # Set the advisor
        self.advisor = advisor_name
        print(f"Your advisor is {advisor_name}")
    def enroll(self, course):
        # Grad students can only take 500+ level courses
        # Check if course number >= 500
        if course >= 500:
            super().enroll(course)
        else:
            print("Error")
# Test:
grad = GraduateStudent("Alice", "G123", "AI Research")
grad.set_advisor("Dr. Smith")
grad.enroll(600)

# TODO: Three-level inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle: {brand}")
    def start(self):
        print("Starting engine...")
class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
        print(f"Car with {doors} doors")
    def start(self):
        super().start()
        print("Car ready to drive")
class ElectricCar(Car):
    def __init__(self, brand, doors, battery_size):
    # Initialize everything properly
        super().__init__(brand, doors)
        self.battery_size = battery_size
        print(f"Electric car with {battery_size} kWh battery")
    def start(self):
    # No engine noise for electric!
    # Should print different message
        super().start()
        print("Electric car is silent but ready to go!")
    def charge(self):
    # New method only for electric
        print("Charging the battery...")
# Test the chain
tesla = ElectricCar("Tesla", 4, 100)
tesla.start()
tesla.charge()

# TODO: Person who is both student and employee
class Student:
    def __init__(self):
        self.student_id = "S12345"
        self.gpa = 3.5
    def study(self):
        print("Studying hard!")
class Employee:
    def __init__(self):
        self.employee_id = "E67890"
        self.salary = 20000
    def work(self):
        print("Working hard!")
class StudentEmployee(Student, Employee):
    def __init__(self, name):
    # Initialize both parents
    # Add name attribute
        Student.__init__(self)
        Employee.__init__(self)
        self.name = name
# Test:
person = StudentEmployee("Alex")
person.study()
person.work()

# TODO: Vehicle for land and water
class LandVehicle:
    def __init__(self):
        self.speed_on_land = 60
    def drive(self):
        print(f"Driving at {self.speed_on_land} mph")
class WaterVehicle:
    def __init__(self):
        self.speed_on_water = 30
    def sail(self):
        print(f"Sailing at {self.speed_on_water} knots")
class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, name):
        # Initialize both
        # Track current mode
        LandVehicle.__init__(self)
        WaterVehicle.__init__(self)
        self.name = name
        self.mode = "Land"
    def switch_mode(self):
        # Toggle between land and water
        if self.mode == "Land":
            self.mode = "Water"
            print("Switching to water mode")
        else:
            self.mode = "Land"
            print("Switching to land mode")
vehicle = AmphibiousVehicle("AmphiCar")
vehicle.switch_mode()

# TODO: Handle method conflicts
class Camera:
    def __init__(self):
        self.megapixels = 12
    def capture(self):
        return "Photo taken!"
class Phone:
    def __init__(self):
        self.phone_number = "555-1234"
    def capture(self): # Same method name!
        return "Screenshot taken!"
class SmartPhone(Phone, Camera):
    def __init__(self, model):
    # Initialize both
        Camera.__init__(self)
        Phone.__init__(self)
        self.model = model
    def capture(self, mode="phone"):
    # Let user choose which capture to use
        if mode == "phone":
            return Phone.capture(self)
        elif mode == "camera":
            return Camera.capture(self)
        else:
            return "Error..."
# Test:
phone = SmartPhone("iPhone")
print(phone.capture())
# How to handle conflicting methods?