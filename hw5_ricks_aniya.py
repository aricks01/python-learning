class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount:
            if amount <= self._balance:
                self._balance -= amount
                return self._balance
            else:
                print("Insufficient funds")
        else:
            print("Enter a positive amount.")
    
    @property     
    def balance(self):
        return self._balance
    
    def __str__(self):
        return f"Account #{self.account_number} - Owner: {self.owner} - Balance: ${self._balance:.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance, interest_rate):
        # TODO: Call parent constructor
        # TODO: Store interest_rate
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        # TODO: Calculate and add interest
        # Return interest amount
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest
    
    def withdraw(self, amount):
        # TODO: Check minimum balance of $100
        # Use parent's withdraw if ok
        if self._balance - amount < 100:
            print("Cannot go below $100 minimum")
        else:
            super().withdraw(amount)
# Test your code
if __name__ == "__main__":
    # Regular account
    regular = BankAccount("1001", "Alice", 500)
    print(regular)
    regular.deposit(100)
    print(f"After deposit: ${regular.balance}")
    regular.withdraw(200)
    print(f"After withdrawal: ${regular.balance}")
    print("\n" + "="*40 + "\n")
    # Savings account
    savings = SavingsAccount("2001", "Bob", 1000, 0.02)
    print(savings)
    interest = savings.add_interest()
    print(f"Interest earned: ${interest:.2f}")
    print(f"New balance: ${savings.balance}")
    # Try to go below minimum
    savings.withdraw(950) # Should fail
    savings.withdraw(500) # Should work
    print(f"Final balance: ${savings.balance}")
    
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # TODO: Initialize private _grades list
        self._grades = []
    def add_grade(self, grade):
        # TODO: Add grade if valid (0-100)
        if grade >= 0 and grade <= 100:
            self._grades.append(grade)
        else:
            print("Error: Invalid grade")
    @property
    def gpa(self):
        # TODO: Return average or 0.0
        if len(self._grades) == 0:
            return 0.0
        else:
            return sum(self._grades) / len(self._grades)
    def get_letter_grade(self):
        # TODO: Return letter grade based on GPA
        gpa = self.gpa
        if gpa:
            if gpa >= 90:
                return 'A'
            elif gpa >= 80:
                return 'B'
            elif gpa >= 70:
                return 'C'
            elif gpa >= 60:
                return 'D'
            elif gpa < 60:
                return 'F'
        else:
            return 'N/A'
        
    def __str__(self):
        # TODO: Return formatted string
        return f"{self.name} (ID: {self.student_id}) - GPA: {self.gpa:.1f}"

class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        # TODO: Call parent constructor
        # TODO: Store thesis_topic
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
        
    def get_letter_grade(self):
        # TODO: Override with stricter grading
        gpa = self.gpa
        if gpa:
            if gpa >= 90:
                return 'A'
            elif gpa >= 80:
                return 'B'
            elif gpa < 80:
                return 'F'
        else:
            return 'N/A'
        
class HonorsStudent(Student):
    def __init__(self, name, student_id, honors_thesis=None):
        # TODO: Call parent constructor
        # TODO: Store honors_thesis
        super().__init__(name, student_id)
        self.honors_thesis = honors_thesis
        
    @property
    def is_eligible_for_honors(self):
        # TODO: Check if GPA >= 87.5
        if self.gpa >= 87.5:
            return True
        else:
            return False
        
    def set_thesis(self, topic):
        # TODO: Set if eligible
        if self.is_eligible_for_honors:
            self.honors_thesis = topic
        else:
            print("Not eligible for honors thesis")
            
class StudentRoster:
    def __init__(self):
        # TODO: Initialize student list
        self._students = []
    def add_student(self, student):
        # TODO: Add to list
        self._students.append(student)
    def find_student(self, student_id):
        # TODO: Search and return student
        for student in self._students:
            if student.student_id == student_id:
                return student
            else:
                return None
                            
    def list_honor_roll(self):
        # TODO: Print students with GPA >= 85
        for student in self._students:
            if student.gpa >= 85:
                print(student)
                
    def class_average(self):
    # TODO: Return average GPA
        if len(self._students) == 0:
            return 0.0
        else:
            total_gpa = sum(student.gpa for student in self._students)
            return total_gpa / len(self._students)
        
        
# Test your code
if __name__ == "__main__":
    # Create roster
    roster = StudentRoster()
    # Add different types of students
    s1 = Student("Alice", "001")
    s1.add_grade(92)
    s1.add_grade(88)
    s1.add_grade(95)
    s2 = GraduateStudent("Bob", "002", "Machine Learning")
    s2.add_grade(85)
    s2.add_grade(82)
    s3 = HonorsStudent("Carol", "003")
    s3.add_grade(95)
    s3.add_grade(98)
    s3.add_grade(92)
    roster.add_student(s1)
    roster.add_student(s2)
    roster.add_student(s3)
    # Test functionality
    print("All Students:")
    for student in [s1, s2, s3]:
        print(f" {student} - Grade: {student.get_letter_grade()}")
        print("\nHonor Roll:")
        roster.list_honor_roll()
        print(f"\nClass Average: {roster.class_average():.1f}")
        # Test honors thesis
        s3.set_thesis("Advanced Algorithms")
        print(f"\nCarol's thesis: {s3.honors_thesis}")