my_list = [1, 2, 3, 2, 1, 4, 2]

# Using a for loop:

frequency_dict = {}
for element in my_list:
    # Check if element exists in the dictionary, initialize count to 0 if not
    frequency_dict[element] = frequency_dict.get(element, 0) + 1

print("Frequency dictionary using for loop:", frequency_dict)  # Output: {1: 2, 2: 3, 3: 1, 4: 1}

# Using a while loop:
index = 0
frequency_dict = {}
while index < len(my_list):
    element = my_list[index]
    frequency_dict[element] = frequency_dict.get(element, 0) + 1
    index += 1

print("Frequency dictionary using while loop:", frequency_dict)  # Output: {1: 2, 2: 3, 3: 1, 4: 1}
