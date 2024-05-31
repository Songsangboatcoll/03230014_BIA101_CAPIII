################################
# https://github.com/Songsangboatcoll/03230014_BIA101_CAPIII
# Chandri Maya Subba
# BBI A
# 03230014
################################
# REFERENCES
# https://www.geeksforgeeks.org/file-handling-python/
#https://docs.python.org/3/library/functions.html
#https://stackoverflow.com/
#https://docs.python.org/3/library/functions.html#open
#https://docs.python.org/3/library/stdtypes.html#str.isdigit
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#https://www.geeksforgeeks.org/extract-numbers-from-a-text-file-and-add-them-using-python/
#https://www.geeksforgeeks.org/python-extract-numbers-from-string/


# SOLUTION
# Your Solution Score: 477522
################################


###
# This is a program that calculates the sum of numbers from a given input file
# and returns the line-wise numbers that contribute to the sum
###


# This function calculates the sum of numbers and their line numbers from a given file
def read_input(filename):
     # Initialize the total sum to 0
    total_sum = 0
     # Initialize an empty list to store the line numbers
    line_numbers = []
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove any leading or trailing whitespaces from the line
            line = line.strip()
            # Check if the line is not empty
            if line:
                # Initialize variables to store the first and last digits of the line
                first_digit = None
                last_digit = None
                 # Iterate through each character in the line
                for char in line:
                    # Check if the character is a digit
                    if char.isdigit():
                        # If it is the first digit, store it
                        if first_digit is None:
                            first_digit = int(char)
                        # If it is not the first digit, store it as the last digit
                        else:
                            last_digit = int(char)
                # Check if both the first and last digits are not None
                if first_digit is not None and last_digit is not None:
                    # Concatenate the first and last digits to form a number
                    number = int(str(first_digit) + str(last_digit))
                    # Add the number to the total sum
                    total_sum += number
                    # Append the number to the list of line numbers
                    line_numbers.append(number)
                 # If the line does not contain both the first and last digits
                else:
                    # Append None to the list of line numbers
                    line_numbers.append(None)
 # Return the total sum and the list of line numbers
    return total_sum,line_numbers

#This will print the solution
def print_solution(filename):
    total_sum,line_numbers = read_input(filename)
    print("Total sum of from the given input file", filename,'is ',total_sum)
    print("Line-wise numbers:",line_numbers)

filename = "014.txt" 
print_solution(filename)




