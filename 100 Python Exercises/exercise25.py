#Question
'''
Make a script that prints out letters of English alphabet from a to z,
one letter per line in the terminal.

Hint: If you're lazy to type down all the letters, you can use the
ascii_lowercase property of the string module
'''
#Answer:
'''
import string

for letter in string.ascii_lowercase:
    print(letter)

Explanation:

string  is a built-in module and string.ascii_lowercase  returns a string
object containing all 26 letters of English alphabet. Then we simply
iterate through that string and print out the string items.
'''
