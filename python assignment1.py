#!/usr/bin/env python
# coding: utf-8

# # Python Assignment 1

# ### 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 

# *
# 'hello'
# -87.8
# -
# /
# +
# 6

# 1) * is a expression
# 
# 2) 'hello' is a value
# 
# 3) -87.8 is a value
# 
# 4) - is a expression
# 
# 5) / is a expression
# 
# 6) + is a expression
# 
# 7) 6 is a value

# ### 2. What is the difference between string and variable?

# String : 
# 
# Strings are basically values i.e., they are alphabetic letters,words or characters that can be stored in a single or double quotes on both sides of value. strings are immutable. Any value in strings can be accessed by [] square brackets. multi line strings are stored in triple quotes.
# 
# For Example:
# 
# Var1 = "i love ineuron"
# Here,"i love ineuron" is a string
# 
# characters inside this string can be accessed like,
# print(Var1[7:14])
# Output will be 'ineuron'
# 
# Variable: 
# 
# variable is a reserved memory location to store values (or) Variables are containers for storing data values.Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it. Variables do not need to be declared with any particular type, and can even change type after they have been set.
# 
# In the above given example, Var1 is a variable, and can be changed to different data types when required.
# 

# ### 3. Describe three different data types. 

# 1) Numeric data type:
# 
# In Python, numeric data type represent the data which has numeric value. Numeric value can be integer, floating number or even complex numbers. These values are defined as int, float and complex class in Python.
# 
# Integers – This value is represented by int class. It contains positive or negative whole numbers (without fraction or decimal). In Python there is no limit to how long an integer value can be.
# 
# Float – This value is represented by float class. It is a real number with floating point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
# 
# Complex Numbers – Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j. For example – 2+3j
# 
# 
# 
# 
# 
# 
# 
# 2) Sequence data type:
# 
# In Python, sequence is the ordered collection of similar or different data types. Sequences allows to store multiple values in an organized and efficient fashion. There are several sequence types in Python –
# 
# String
# 
# List
# 
# Tuple
# 
# 
# 
# 
# 
# 
# 
# 3) Boolean Data type:
# 
# Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false). But non-Boolean objects can be evaluated in Boolean context as well and determined to be true or false. It is denoted by the class bool.
# 
# Note – True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will throw an error.

# ### 4. What is an expression made up of? What do all expressions do?

# A) An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.
# 
# B)an expression is evaluated as per the precedence of its operators. So that if there is more than one operator in an expression, their precedence decides which operation will be performed first
# 
# There are different types of expressions. they are,
# 1) Arithmetic expressions
# 
# 2) Relational expressions
# 
# 3) String expressions
# 
# 4) Logical expressions
# 
# 5) Compound expressions
# 
# 
# 

# ### 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# A Python expression can be defined as any element in our program that evaluates to some value.
# 
# An expression evaluates to a value. A statement does something. Statements represent an action or command e.g print statements, assignment statements. Expression is a combination of variables, operations and values that yields a result value.
# 
# An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.
# 
# Expression Vs Statement
# 
# ★Expression
# Expressions always returns a value
# Functions are also expressions. Even a non returning function will still return
# Functions are also expressions. Even a non returning function will still return value, so it is an expression.
# Can print the result value
# 
# Examples Of Python Expressions: “Hello” + “World”, 4 + 5 etc.
# 
# ★Statement
# A statement never returns a value
# Cannot print any result
# 
# Examples Of Python Statements: Assignment statements, conditional branching, loops, classes, import, def, try, except, pass, del etc
# 
# ★Summary
# In simpler terms, we can say that anything that evaluates to something is a Python expression, while on the other hand, anything that does something is a Python statement. Curious to learn further? Follow our other articles in this blog to know more!
# 
# 

# ### 6. After running the following code, what does the variable bacon contain? 
# 
# bacon = 22
# 
# bacon + 1

# In[1]:


bacon =22
print (bacon+1)

# the variable bacon contains value 23


# ### 7. What should the values of the following two terms be?
# 
# 'spam' + 'spamspam'
# 
# 'spam' * 3

# In[2]:


print('spam' + 'spamspam')

print('spam' * 3)


# Both the statements gives same output values i.e,
# 
# spamspamspam
# 
# spamspamspam
# 

# ### 8. Why is eggs a valid variable name while 100 is invalid?

# eggs is a alphabetic variable or started with alphabet letter. here in python variable should start with alphabetic letters but is not allowed to start with numeric values as it causes complications in python operations.
# 
# As the later variable is made or started with number values that cannot be considered as variable and drops in error.

# ### 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# The int() , float() , and str( ) functions will evaluate to the 
# integer, floating-point number, and string versions of the value passed to them respectively.

# ### 10. Why does this expression cause an error? How can you fix it?
# 
# 'I have eaten' + 99 + 'burritos.'

# numerical(int & float) values cannot be added with strings, thats why the python compiler drops in an error.
# 
# 
# In order to add 99 to the above string statements, we need to convert the numerical value (99) to a string. This can be done by simply putting single/double quotes to 99 on both sides.
# like '99' or "99"
# 
# check the below code (fixed):

# In[4]:


print('I have eaten '+'99'+' burritos')


# In[ ]:




