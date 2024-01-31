languages = ["Python", "Ruby", "PHP", "JS", "Java"] # List
print(languages[0]) # Print index element
languages[1] = "Go" # Replace element
print(languages) 
print(languages[1:3]) #Sort elements
print(languages[:3]) # Sort elements from 0 default
print(languages[1:]) # Sort elements from last default

languages.insert(5, "Ruby") # Insert element
print(languages)

languages.remove("PHP") # Remove Element
print(languages)

print("JS" in languages) #Find element in array and return a boolean

print(len(languages)) # count the number of elements

languages.clear() # Erase the content of the array


