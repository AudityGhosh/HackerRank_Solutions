# Problem Definition:
# The task is to compute the average of a series of numbers provided as input. 
# The function takes an arbitrary number of arguments and calculates their average.

# Author: Audity Ghosh
# Date: January 1, 2025

# Description:
# The function avg() takes any number of numeric inputs and returns their average.
# The function works by iterating over the input arguments, summing them up, 
# and dividing by the number of arguments.

# Approach:
# 1. Define a function avg() to accept a variable number of arguments using *args.
# 2. Initialize a sum variable to accumulate the sum of the arguments.
# 3. Use a counter to track the number of arguments provided.
# 4. Iterate over the arguments, updating both the sum and the counter.
# 5. Return the average by dividing the sum by the number of arguments.
# 6. The main part of the code will handle user input and invoke the avg function.

def avg(*args):
    """
    Function to calculate the average of a variable number of arguments.
    
    :param args: A variable number of numeric values.
    :return: The average of the numbers.
    """
    summ = 0.0  # Initialize sum of arguments
    no_el = 0   # Initialize count of elements
    
    # Iterate through all the provided arguments
    for arg in args:
        no_el += 1   # Increment the element count
        summ += arg  # Add the current element to the sum
    
    # Return the average, ensuring no division by zero
    return summ / no_el if no_el != 0 else 0.0

# Main execution
if __name__ == "__main__":
    # Taking input from the user, mapping each input to an integer
    args = map(int, input("Enter numbers separated by spaces: ").split())
    
    # Call the avg function with the unpacked arguments and print the result
    print(f"The average is: {avg(*args)}")

    