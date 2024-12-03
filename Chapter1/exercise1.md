# Exercise 1 : This exercise contain some questions

# Question 1 : In a print statement, what happens if you leave out one of the parentheses, or both?
if we write the print statement like : print('Hello World!' or print 'Hello World!' 
while executing, will show a SyntaxError, and it's because we didn't respect the syntax 
we use parentheses because the print is a function.



# Question 2 : If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
While trying to print a string, if we leave out one of the quotation marks, the program will show a SyntaxError because while using print, we must use quotation marks both or leave them both.


And the second case, if we leave out the quotation marks both, we have two cases, let me put an example:

    1- if I already defined a variable named for example "number" with a value of 20, then I printed print(number), the program will print the value of the variable "number" which is 20.
    
    2-And if we dont have that variable defined previously in the program, while trying to print it, the program will show us an error that the variable is not defined in the program.

An other case: we may try to print a String like print(Hello world! Im Hanan!)
the program will show an error that we maybe forget comma, thinking that we wanna print a sequence of variables, but actually we dont.



# Question 3 : You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
I'm using Python 3, when I execute 2++2 nothing happens, it's like I executed 2+2 
And when I execute 2+-2, it's like 2-2.



# Question 4 : In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?
When I try a number which start with zero, like 09 or 011, the program shows a SyntaxError
" SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers ".



# Question 5 : What happens if you have two values with no operator between them?
If I didn't use an operator between strings the system concatenate them, but with numerical values it shows SyntaxError that syntax is invalid.