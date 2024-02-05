# Define a variable with a string value
phrase = "All ma fellas"

# Define a function that counts the number of words in a string
# Use the split method to separate the words by spaces
# Use the len function to get the length of the list of words
# Return a string with the number of words and the original string
def count(p):
    words = p.split()
    return "There are " + str(len(words)) + " words in " + p
        
# Call the count function with the phrase as argument and print the result
print(count(phrase))

# Define another function that counts the number of words in a string (DEPRECATED)
# Use the split method to separate the words by spaces
# Use a for loop to iterate over the list of words
# Use a variable to keep track of the number of words
# Increment the variable by one for each word
# Return a string with the number of words and the original string
def loop(w):
    number = 0
    for word in w.split():
        number += 1
    return "There are " + str(number) + " words in " + w
    
# Call the loop function with the phrase as argument and print the result
print(loop(phrase))
