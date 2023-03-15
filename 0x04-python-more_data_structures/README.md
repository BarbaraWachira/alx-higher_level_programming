What are sets and how to use them
What are the most common methods of set and how to use them
When to use sets versus lists
How to iterate into a set
What are dictionaries and how to use them
When to use dictionaries versus lists or sets
What is a key in a dictionary
How to iterate over a dictionary
What is a lambda function
What are the map, reduce and filter functions
 
0. Squared simple
mandatory
Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modifie

1. Search and replace
mandatory
Write a function that replaces all occurrences of an element by another in a new list.

Prototype: def search_replace(my_list, search, replace):
my_list is the initial list
search is the element to replace in the list
replace is the new element

2. Unique addition
mandatory
Write a function that adds all unique integers in a list (only once for each integer).

Prototype: def uniq_add(my_list=[]):

3. Present in both
mandatory
Write a function that returns a set of common elements in two sets.

Prototype: def common_elements(set_1, set_2):

4. Only differents
mandatory
Write a function that returns a set of all elements present in only one set.

Prototype: def only_diff_elements(set_1, set_2):

5. Number of keys
mandatory
Write a function that returns the number of keys in a dictionary.

Prototype: def number_keys(a_dictionary):

6. Print sorted dictionary
mandatory
Write a function that prints a dictionary by ordered keys.

Prototype: def print_sorted_dictionary(a_dictionary):

7. Update dictionary
mandatory
Write a function that replaces or adds key/value in a dictionary.

Prototype: def update_dictionary(a_dictionary, key, value):
key argument will be always a string
value argument will be any type

8. Simple delete by key
mandatory
Write a function that deletes a key in a dictionary.

Prototype: def simple_delete(a_dictionary, key=""):
key argument will be always a string

9. Multiply by 2
mandatory
Write a function that returns a new dictionary with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers

10. Best score
mandatory
Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):

11. Multiply by using map
mandatory
Write a function that returns a list with all values multiplied by a number without using any loops.

Prototype: def multiply_list_map(my_list=[], number=0):
Returns a new list:
Same length as my_list
Each value should be multiplied by number
Initial list should not be modified

12. Roman to Integer
Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0


