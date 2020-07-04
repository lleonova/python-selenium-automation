# Amazon interview question:
# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

def first_unique_letter(string):
    string = string.lower()
    for char in string:
        if string.count(char) == 1:
            return char

print(first_unique_letter("Amazon"))