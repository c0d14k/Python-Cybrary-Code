## printing to output
## string and integers
## variables
## string formatting


string_variable = 'hello world' #string = 'text', or "text", or '''doc string''', or """doc string""" 
print string_variable

int_variable = 1234 #int = number values
print int_variable 

#you can add/subtract/divide/multiply integers with other integers.
#e.g.
print '1234 + 19 =', #comma after a string means DO NOT SEPERATE WITH A NEW LINE, rather, seperate with a whitespace 
print int_variable + 19
#output will be: 1234 + 19 = 1253

#you can also add to string with other strings e.g.
print string_variable + ', hello again!'
#output: hello world, hello again!

#you can add values stored as integers to string... wait? how? 
#the answer is conversion! that's right, you can convert int to string. and it goes as follows.
print 'I am going to write a number. that number is:', str(int_variable)


 

