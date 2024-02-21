# def hello(name):
#     print("THE HELLO FUNCTION IS RUNNING!")
    
#     def greet():
#         return "HELLO SADAF HOW HAVE YOU BEEN"
    
#     def welcome():
#         return " WELCOME TO THE NOTES "+name.upper()
    
#     if name == "sadaf":
#         return greet
#     else:
#         return welcome
    
# x = hello(name="jose")

# print(x())
# def hello():
#     return "HI SADAF!"

# def other(func):
#     print("HELLO")
#     print(func())
# other(hello)    

def new_decorator(func):
    def wrap_func():
        print("code here before executing func")
    func()
    print("func() has been called")
    
    return wrap_func


@new_decorator
def func_needs_decorator():
    print("this function is in need of a decorator!")
    
# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator() instead of this we can use a special key called @decorator
    
    