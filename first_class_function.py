# """ Assign function to a variable"""

# def add(a,b):
#     c = a +b
#     return c

# f = add(4,5) #here it is copying outfut from function 
# g = add 

# """ #this is called fstring
# () means we want to execute function if we remove ();
# and we can assign function 
# to a var this is called first class function
# """
# print(f)
# print(g(4,5)) #here we are calling variable in which we assigned a function

# print(g) # g is still a variable which just hold add of function where it is store... 
# print(add) #add is function the address will remain same for variable g also


# """ Passing function as argument and return function as a result this process called 
# higher order function """

# def square(x):
#      return x * x

# def cube(x):
#      return x * x * x


# def my_map (func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(cube, [1, 2, 3, 4, 5])
# print(squares)
# def cube(x):
#      return x * x * x


# def logger (msg):
#     def log_message():
#        print('Log:', msg)
#     return log_message
# a = logger('Hi!')

# print(id(a))
# print(id(logger))
# print(logger)
# print(a)


# def html_tag(tag):

#     def wrap_text(msg):
#         print('<{0}>{1}</{0}>'.format(tag, msg))

#     return wrap_text

# print_h1 = html_tag('h1')
# print_h1('Test Headline!')
# print_h1('Another Headline!')

# print_p = html_tag('p')
# print_p('Test Paragraph!')

def outer_func():
    message = 'Hi'
    def inner_func():
         print (message)
    return inner_func()
outer_func()
"""
Closures closes over free variable
"""






    