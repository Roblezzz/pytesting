# Define sets representing student groups
group_a = {'Ana', 'Marcos', 'Carlos', 'Mario'}  # Group A students
group_b = {'Ana', 'Pedro', 'Carlos', 'Antonio'}  # Group B students
group_c = {'Ana', 'Antonio', 'Marcos', 'Pepe'}  # Group C students

# Combine all students from different groups into a single set
all_students = group_a.union(group_b).union(group_c)

# Iterate through each student in the combined set
for student in all_students:
    # Initialize an empty list to store group letters for the current student
    groups_in = []

    # Iterate through group letters (A, B, C) and their corresponding sets
    for letter, group in zip('ABC', [group_a, group_b, group_c]):
        # If the student is found in the current group, append the group letter
        if student in group:
            groups_in.append(letter)

    # Join the group letters into a string, separated by hyphens
    groups_str = '-'.join(groups_in)

    # Handle pluralization for "grupo" based on the number of groups
    plural = 's' if len(groups_in) > 1 else ''

    # Print the student's name, group information, and pluralized "grupo"
    print(f'{student} en grupo{plural}: {groups_str}')
    print(groups_in)

