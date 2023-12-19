"""Map applies a function to all the items in an input_list. Here is the blueprint:"""
" map(function_to_apply,list_of_inputs) "

items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
print(squared)

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply,add]

for i in range(5):
    value = list(map(lambda x:x(i),funcs))
    print(value)
