""""*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass an unspecified number of arguments to a function, so when writing the function definition, you do not need to know how many arguments will be passed to your function. *args is used to send a non-keyworded variable length argument list to the function"""

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob','python','eggs','test')


"""**kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function. Here is an example to get you going with it:"""

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key,value))

greet_me(name="yasoob")

"""Order of using *args **kwargs and formal args"""
"""some_func(fargs,*args,**kwargs)"""
"""*args must occur before **kwargs"""


"""Using *args and **kwargs to call a function"""
"""You can also use *args and **kwargs when calling a function. Here is an example:"""
def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)

args = ("two",3,5)
test_args_kwargs(*args)

kwargs = {"arg3":3,"arg2":"two","arg1":5}
test_args_kwargs(**kwargs)
