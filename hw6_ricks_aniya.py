from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
    # TODO: Make this abstract
        pass
    
    @abstractmethod
    def perimeter(self):
    # TODO: Make this abstract
        pass
    
    def describe(self):
    # TODO: Return "This is a [class name]"
        return f"This is a {self.__class__.__name__}"

    @staticmethod
    def validate_positive(value, name):
    # TODO: Check if value > 0
    # Print error if not
    # Return True/False
        if value <= 0:
            print(f"Error: {name} must be positive.")
            return False
        else:
            return True
    
class Circle(Shape):
    def __init__(self, radius):
        # TODO: Validate radius
        # TODO: Store radius
        self.validate_positive(radius, "Radius")
        self.radius = radius
    
    def area(self):
        # TODO: Calculate circle area
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        # TODO: Calculate circumference
        return 2 * math.pi *self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        # TODO: Validate width and height
        # TODO: Store dimensions
        self.validate_positive(width, "Width")
        self.validate_positive(height, "Height")
        self.width = width
        self.height = height
    
    def area(self):
        # TODO: Calculate rectangle area
        return self.width * self.height
    
    def perimeter(self):
        # TODO: Calculate rectangle perimeter
        return 2 * (self.width + self.height)
    
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        # TODO: Validate all sides
        # TODO: Store sides
        self.validate_positive(side1, "Side 1")
        self.validate_positive(side2, "Side 2")
        self.validate_positive(side3, "Side 3")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Heron's formula (provided for you):
        # s = (a + b + c) / 2
        # area = sqrt(s * (s-a) * (s-b) * (s-c))
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        # TODO: Sum of all sides
        return (self.side1 + self.side2 + self.side3)
        
class ShapeCollection:
    def __init__(self):
        # TODO: Initialize shapes list
        self.shapes = []
    
    def add_shape(self, shape):
        # TODO: Add shape to list
        if shape:
            self.shapes.append(shape)
        return self.shapes
    
    def total_area(self):
        # TODO: Sum all shape areas
        #for shape in self.shapes:
        total = 0   
        for shape in self.shapes:
            total += shape.area()
        return total
    
    def total_perimeter(self):
        # TODO: Sum all shape perimeters
        total = 0   
        for shape in self.shapes:
            total += shape.perimeter()
        return total
    
# Test your code
if __name__ == "__main__":
    # Create shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    # Test individual shapes
    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f" {shape.describe()}")
        print(f" Area: {shape.area():.2f}")
        print(f" Perimeter: {shape.perimeter():.2f}")
        # Test collection (polymorphism!)
    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    print(f"\nCollection Totals:")
    print(f" Total Area: {collection.total_area():.2f}")
    print(f" Total Perimeter: {collection.total_perimeter():.2f}")
    # Test validation
    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print(" Correctly rejected negative radius")