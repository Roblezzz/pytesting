
def fizzbuzz():
    my_list = []
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            my_list.append("fizzbuzz")
        elif i % 3 == 0:
            my_list.append("fizz")
        elif i % 5 == 0:
            my_list.append("buzz")
        else: my_list.append(i)
        
    return my_list


print(fizzbuzz())

