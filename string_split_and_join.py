# Say "Hello, World!" With Python
# Author: Audity Ghosh
# Date: 25 March, 2021
# Description:
# This function splits the input string by spaces and then joins it using a hyphen ("-").

def split_and_join(line):
    # Split the string at each space, and join the resulting list with a hyphen ("-")
    return "-".join(line.split(" "))