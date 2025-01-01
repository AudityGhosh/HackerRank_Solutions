# HackerRank Python Basic Certification Problem 2
# Problem Definition: 
# This code defines two geometric shapes (Rectangle and Circle), calculates their areas using respective formulas.
# Author: Audity Ghosh
# Date: 2025-01-01
# Description:
# - The `Rectangle` class calculates the area of a rectangle given its length and width.
# - The `Circle` class calculates the area of a circle given its radius.
# Approach:
# - Create classes for each shape with methods to calculate areas.
# - Use Python's math library for the circle's area.
# - Define a main function to demonstrate usage of these classes.
# Comments: The main function demonstrates the creation of rectangle and circle objects, calling the area methods.


import math

class Rectangle:
    def __init__(self, length, width):
        """
        Constructor to initialize the dimensions of the rectangle.
        :param length: Length of the rectangle.
        :param width: Width of the rectangle.
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Method to calculate the area of the rectangle.
        :return: Area of the rectangle (length * width).
        """
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        """
        Constructor to initialize the radius of the circle.
        :param radius: Radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """
        Method to calculate the area of the circle.
        :return: Area of the circle (π * radius^2).
        """
        return math.pi * (self.radius ** 2)


def main():
    """
    Main function to process multiple queries and calculate areas of different shapes.
    """
    # Read the number of queries
    q = int(input("Enter the number of queries: "))
    
    for _ in range(q):
        # Read each query
        query = input("Enter query: ").split()

        # Unpack the query dynamically
        shape_type, *params = query  # First item is shape_type, rest are parameters
        
        if shape_type == "Circle":
            radius = float(params[0])  # Only one parameter for Circle
            circ = Circle(radius)
            print(f"Circle Area: {circ.area():.2f}")
        
        elif shape_type == "Rectangle":
            length, width = map(float, params)  # Two parameters for Rectangle
            rect = Rectangle(length, width)
            print(f"Rectangle Area: {rect.area()}")

        else:
            print("Invalid query. Please provide valid input.")

if __name__ == "__main__":
    main()
