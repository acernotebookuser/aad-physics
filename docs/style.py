# imports are done at the top of the file
import some_import
import some_other_import
import another_import

# indentation is 8 spaces. configure your IDE to work as such
def some_function():
        print("hello world")
        a = input("some input: ")
        
# the case convention for functions is fully snake_case
def this_is_the_case_convention():
        return

this_is_a_variable = 40 # variable names also follow the snake_case convention

# classes follow the PascalCase convention
class ThisIsAClass:
        def __init__(s):
                return
        
# DO NOT exceed 79 characters on a single line. if your code breaks this rule,
# you are almost certainly doing something wrong
here_is_a_very_very_very_very_very_very_very_very_very_long_line_of_code = 123

# look at the following code:
# <example>

# ===== another_function(a, b) =====
# this is a function which adds two numbers and returns the sum
def another_function(a, b):
        return a + b

# </example>
# notice how the comments explaining the function were totally worthless? if
# your comments look like those, DO NOT BOTHER ADDING THEM. they only cause
# unnecessary clutter. besides, your code should (ideally) be self-explanatory
# and not even require comments in the first place

# here is another awful example:
# <example>

#=============================#
# add one to the variable "x" #
#=============================#
x += 1

#=========================================================================#
# call the function "a_func()" and return the value into the variable "y" #
#=========================================================================#
y = a_func()

# </example>
# it needn't be said why this makes your code significantly worse.
# an argument: "but comments make my code look better!"
# if comments are really just that important to the code aesthetics, you are
# writing poor quality code
