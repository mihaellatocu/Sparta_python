"""
Create a list called 'shopping_list' with the following items:
eggs
bread
bananas
biscuits
milk
Print the list to the screen
Print the data type of 'shopping_list'
Print the first item in the list
Print the last item in the list
Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed
Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)
Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.
Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
olist' to check it's been removed.
Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'
"""

# shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk']
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0])
# print(shopping_list[-1])
# shopping_list[1] = "rice"
# print(shopping_list[1])
# shopping_list.append('carrots')
# print(shopping_list)
# print(len(shopping_list))
# shopping_list.extend(['toffee', 'coffee'])
# shopping_list += ['item1', 'item2', 'item3'] # to comment
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)

########################

"""
Use your code from the "Task: Python variable basics" (last subtask) where you asked the user for their name, age and DOB. 
Mix the name, age and DOB into one list user_details_list 
Print the user's name, age and DOB from the list 
Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list. 
Ask the user for their height in cm and save it to the variable height 
Save height as a float in the list, and print the height from the list. 
"""

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# DOB = int(input("Enter your DOB: "))
# user_details_list = [name, age, DOB]
# print(type(user_details_list))
# print(user_details_list)
# height = float(input("Enter your height in cm: "))
# user_details_list.append(height)
# print(user_details_list[-1])

###############################

# mixture = [1, 2, 3, "one", "two", "three"]
# print(mixture)
# print(mixture[1:3])
# print(mixture[::2])
# print(mixture[-1:-3:-1])

################################

"""
How are tuples similar to lists? 
- Can hold multiple items
- Can contain mixed data types (e.g. numbers, strings, etc.)
- Support indexing and slicing
- Can be iterated over with a for loop

Can be nested (a tuple can contain another tuple or list, and vice versa)

Are tuples immutable and what does this mean? 
- once a tuple is created, it cannot be changed. You can’t add, remove, or modify elements inside it.
What other data types are immutable? 
Other built-in immutable types include:
str (strings), int (integers), float, bool, complex
frozenset (an immutable version of a set)
bytes (immutable version of bytearray)
Mutable examples for comparison:
list, set, dict, bytearray
What are good use cases for tuples instead of lists? 
You want to store fixed data that shouldn’t change
→ e.g., coordinates (x, y), RGB colors (255, 128, 0), or a database record.
You want to use the data as a dictionary key or inside a set (lists can’t be used because they’re mutable).
You need slightly better performance (tuples are faster and smaller in memory).
What does the following piece of code do? 
"""

# essentials = ("bread", "eggs", "milk")
# print(essentials)
# print(essentials.count("bread"))

###########################



# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
# print("You are stranded on a desert island. You can take only THREE items.")
# essential_item1 = input("What is an essential item you would take? ")
# essential_item2 = input("What is an essential item you would take? ")
# essential_item3 = input("What is an essential item you would take? ")
# # save the items as a tuple
# essentials_tuple = (essential_item1, essential_item2, essential_item3)
# print(essentials_tuple)
# print("Here are your items as a tuple:", essentials_tuple)
# print("")
# print("I lied. You can take one more item.")
# essential_item4 = input("What is one more essential item you would take? ")
# # try to add the 4th item to the tuple
# # if you can't add the 4th item, work out how to save the 4th item to the tuple
# # YOUR CODE GOES HERE
# essentials_tuple = essentials_tuple + (essential_item4,)
# print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)


###########################

"""
Make a dictionary called "student_1" containing the following information: 
name: susan 
stream: tech 
completed_lessons: 4 (should be saved as an integer not a string) 
completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up" 
Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with? 
- In a dictionary, data is stored as key-value pairs — each value is associated with a unique key
Print the dictionary to the screen 
Print its data type to the screen to check it's a dictionary 
Print the value for the key-value pair having the key "stream" 
Print the value for 'completed_lesson_names' - check you can see the list of 3 items 
Print the data type for the value for 'completed_lesson_names' - check it is a list 
Print the first element/item in the list of 'completed_lesson_names' (should output "variables") 
Change the value of "completed_lessons" to 3 (an integer not string). 
Make sure you change was successful by printing your dictionary to the screen again. 
Delete "data_types" from the list under the key 'completed_lesson_names' 
Use the keys() method on your dictionary to list all the keys 
"""
# student_1 = {
#     "name": "susan",
#     "stream": "tech ",
#     "completed_lessons": "4",
#     "completed_lesson_names": ["variables", "data_types", "set up"]}
# print(student_1)
# print(type(student_1))
# print(student_1["stream"])
# print(student_1["completed_lesson_names"])#print value
# print(type(student_1["completed_lesson_names"])) # print type
# print(student_1["completed_lesson_names"][0]) #first item
# student_1["completed_lessons"] = 3 #reassign to int
# print(student_1)
# student_1["completed_lesson_names"].remove("data_types")
# print(student_1)
# print(student_1.keys())


####################
